import sys
import pygame
import time
import random
import math
from pathlib import Path
import shelve

from Settings import settings
from GameState import GameState
from Button import *
from BoxedCat import BoxedCat
from Scoreboard import Scoreboard
from Cursor import Cursor_Paw

pygame.init()
pygame.display.set_caption("Catch Mitao!")
screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

state = GameState()

Path("data").mkdir(parents=True, exist_ok=True)
d = shelve.open('data/score')
if  not 'high_score' in d:
    d['high_score'] = 0
    state.high_score = 0
else:
    state.high_score = d['high_score']
d.close()

scoreboard = Scoreboard(screen)
play_button = MainScreen_Button(screen, "Play", screen.get_rect().centerx - 250, 350)
exit_button = MainScreen_Button(screen, "Exit", screen.get_rect().centerx, 350)
about_button = MainScreen_Button(screen, "About", screen.get_rect().centerx + 250, 350)
return_button = Return_Button(screen, "This is my first game. Hope you enjoy it!", 600, 350)
fish_notification = Note_Fish(screen)
level_notification = Note_Msg(screen,"Level + 1")
over_notification = Note_Msg(screen, "Oops! No fish left!")
cursor_paw = Cursor_Paw(screen)

is_running = True
elapsed_time = 0
generation_timer = 0

while is_running:
    start_time = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if state.stage == 'home':
        bg0 = pygame.image.load('images/bg0.png')
        screen.blit(bg0, (0, 0))
        
        for button in (play_button, exit_button, about_button):
            if button.text_button.check_hovering(mouse_x, mouse_y):
                if not button.text_button.hovering:
                    pop = pygame.mixer.Sound("music/pop.wav")
                    pygame.mixer.Channel(1).play(pop)
                    button.text_button.hovering = True 
            else:
                button.text_button.hovering = False
            button.draw()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.text_button.check_hovering(mouse_x, mouse_y):
                    state.stage = 'play'
                    pygame.mixer.music.stop()
                    break
                if exit_button.text_button.check_hovering(mouse_x, mouse_y):
                    is_running = False
                    break
                if about_button.text_button.check_hovering(mouse_x, mouse_y):
                    state.stage = 'about'
                    break
    elif state.stage == 'about':
        bg0 = pygame.image.load('images/bg0.png')
        screen.blit(bg0, (0, 0))

        if return_button.text_button.check_hovering(mouse_x, mouse_y):
            if not return_button.text_button.hovering:
                pygame.mixer.Channel(1).play(pop)
                return_button.text_button.hovering = True
        else:
            return_button.text_button.hovering = False
        return_button.draw(settings)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.text_button.check_hovering(mouse_x,mouse_y):
                    state.stage = 'home'
                    break
    elif state.stage == 'over':
        screen.fill(settings.bg_color)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                is_running = False
                break
        
        over_notification.update(elapsed_time)
        over_notification.draw()

        if over_notification.timer == 0:
            state.stage = 'home'
            pygame.mixer.music.stop()
        
    elif state.stage == 'play':
        screen.fill(settings.bg_color)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for boxed_cat in state.cats:
                    if boxed_cat.cat.rect.collidepoint(mouse_x, mouse_y):
                        state.cats.remove(boxed_cat)
                        cat_meow = pygame.mixer.Sound("music/cat_meow.wav")
                        pygame.mixer.Channel(0).play(cat_meow)

                        state.score += 50
                        state.high_score = max(state.high_score, state.score)
                        if state.score % 750 == 0:
                            level_notification.timer = 0.5
                if scoreboard.void_button.rect.collidepoint(mouse_x, mouse_y):
                    state.high_score = 0
                    state.score = 0
                if scoreboard.home_button.rect.collidepoint(mouse_x, mouse_y):
                    state.stage = 'home'
                    state.reset()
                    pygame.mixer.music.stop()                          
                    break
        
        generation_timer -= elapsed_time
        if generation_timer < 0:
            while True:
                min_distance = 100000000
                x = random.randint(100, 1100)
                y = random.randint(200, 700)
                for boxed_cat in state.cats:
                    distance = math.sqrt((x - boxed_cat.cat_position[0]) ** 2 + (y - boxed_cat.cat_position[1]) ** 2)
                    min_distance = min(min_distance, distance)

                if min_distance > 200:
                    boxed_cat = BoxedCat(screen, x, y)
                    state.cats.append(boxed_cat)
                    break
            generation_timer = 0.7 * (0.9 ** (state.score // 750))

        for boxed_cat in state.cats:
            boxed_cat.update(state)
            boxed_cat.draw()
        
        if len(state.cats) >= 5:
            state.fish_left -= 1
            if state.fish_left > 0:
                state.cats = []
                fish_notification.timer = 0.5
            elif state.fish_left < 1:
                over_notification.timer = 3
                state.reset()
                state.stage = 'over'

        fish_notification.update(elapsed_time)
        fish_notification.draw()

        level_notification.update(elapsed_time)
        level_notification.draw()

        scoreboard.draw(state.score, state.high_score, len(state.cats), state.fish_left)
        
    cursor_paw.draw_paw(mouse_x, mouse_y)
    pygame.display.flip()
    
    if not pygame.mixer.music.get_busy():
        music = 'music/bg_music.wav' if state.stage in ['play', 'over'] else 'music/pre_music.wav'
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    end_time = time.time()
    elapsed_time = end_time - start_time


d = shelve.open('data/score') 
d['high_score'] = state.high_score
d.close()
