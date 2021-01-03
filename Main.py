import sys
import pygame
import time
import random
import math
from pathlib import Path
import shelve

from Settings import Settings
from GameState import GameState
from Button import *
from BoxedCat import BoxedCat, Cat_Symbol, Multiply
from Scoreboard import Scoreboard
from Cursor import Cursor_Paw

state = GameState()
settings = Settings()

pygame.init()
pygame.display.set_caption("Catch Mitao!")
screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))

bg0 = pygame.image.load('images/bg0.png')

time_left = 0
fade_time_fish = 0
fade_time_level = 0

score = 0

Path("data").mkdir(parents=True, exist_ok=True)
d = shelve.open('data/score')
if  not 'high_score' in d:
    d['high_score'] = 0
    high_score = 0
else:
    high_score = d['high_score']

msg_fade_minus = Msg_Fade_Minus(screen,settings)
msg_fade_plus = Msg_Fade_Plus(screen,settings)

sb = Scoreboard(screen,settings,score,high_score,state,msg_fade_minus)

play_button = MainScreenButton(screen, "Play", screen.get_rect().centerx-250, 350, 230, 300, settings)
exit_button = MainScreenButton(screen, "Exit", screen.get_rect().centerx, 350,480, 300, settings)
about_button = MainScreenButton(screen, "About", screen.get_rect().centerx+250, 350, 710, 300, settings)
return_button = Return_Button(screen, settings)
void_button = Void_High_Score(screen, sb, settings)
home_button = Home_Button(screen, sb)
fish_fade = Fish_Fade(screen, msg_fade_minus)
game_over = Game_Over(screen, settings)


pygame.mixer.pre_init()
pygame.mixer.init()
cat_meow = pygame.mixer.Sound("music/cat_meow.wav")
pop = pygame.mixer.Sound("music/pop.wav")

pygame.mouse.set_visible(False)


cat_symbol = Cat_Symbol(screen)
multiply = Multiply(screen)


d.close()

stopped = False

elapsed_time = 0
while True:
    
    if state.active:
        fade_time_home = 0

        mouse_x, mouse_y = pygame.mouse.get_pos()
        cursor_paw = Cursor_Paw(screen)
        start_time = time.time()
        if state.home_flag == True:
            if fade_time_home >= 0:
                screen.fill(settings.bg_color)
                game_over.draw(settings)
                fade_time_home -= elapsed_time
            elif fade_time_home <  0:
                state.active = False
                state.home_flag = False
                break
        else:
            settings.generation_time = 0.7 * (0.9 ** (score // 750))
            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boxed_cat in state.cats:
                        if boxed_cat.cat.rect.collidepoint(mouse_x, mouse_y):
                            state.cats.remove(boxed_cat)

                            #produce the sound
                            pygame.mixer.Channel(0).play(cat_meow)

                            #deal with score
                            d = shelve.open('data/score') 

                            #update score
                            get_score = 50
                            score = score + get_score
                            sb.prep_score(settings,score)
                            #update high score
                            if score > high_score:
                                high_score = score

                            sb.prep_high_score(settings,high_score)
                            
                            #update documented high_score                        
                            if d['high_score'] < high_score:
                                d['high_score'] = high_score   
                            d.close()
                            

                    
                    #clear button to reset all scores to 0
                    if void_button.msg_text_rect.collidepoint(pygame.mouse.get_pos()):
                        high_score = 0
                        score = 0
                        sb.prep_high_score(settings,high_score)
                        sb.prep_score(settings,score)
                        d = shelve.open('data/score') 
                        d['high_score'] = 0
                        d.close()

                    #when press home button, restart the game
                    if home_button.rect.collidepoint(pygame.mouse.get_pos()):
                        state.active = False
                        state.break_flag = True
                        state.initiate(sb,play_button,settings,screen,state)
                        pygame.mixer.music.stop()
                        score = 0                           
                        break

            if state.break_flag == True:
                state.break_flag = False
                continue
            
            
            #control the animation of each boxed cat(distance, time)  
            time_left -= elapsed_time
            
            
            if time_left < 0:
                # test += 1
                while True:
                    min_distance = 100000000
                    x = random.randint(100,1100)
                    y = random.randint(200,700)
                    for boxed_cat in state.cats:
                        distance = math.sqrt((x-boxed_cat.cat_position[0])**2 + (y-boxed_cat.cat_position[1])**2)
                        min_distance = min(min_distance, distance)

                    if min_distance > 200:
                        #state.cat_id = state.cat_id + 1
                        boxed_cat = BoxedCat(screen, x, y)
                        state.cats.append(boxed_cat)
                        break
                  
                time_left = settings.generation_time

            for boxed_cat in state.cats:
                if not boxed_cat.is_animating:
                    boxed_cat.animate(0.5)
                boxed_cat.update(state)

            #draw boxed cats, add 'screen.fill' to product the animation effect
            screen.fill(settings.bg_color)

            
            for boxed_cat in state.cats:
                boxed_cat.draw()
            
            #show level and number of boxed cat
            sb.prep_level(settings,score,msg_fade_minus)
            sb.prep_cat(state, settings)

            #prep fish part 1
            if state.fish == []:
                sb.prep_fish(state,screen)
            else:
                if len(state.cats) > 4:
                    if state.fish_left > 1:
                        state.fish_left -= 1
                        
                        state.cats = []

                        fade_time_fish = 0.5
                        
                        state.fade_flag_fish = True
                        
                        state.fish = []
                        
                        sb.prep_fish(state,screen)

                        continue

                    elif state.fish_left <= 1: 
                        fade_time_home = 3
                        state.initiate(sb,play_button,settings,screen,state)
                        score = 0
                        state.home_flag = True

            # prep fish part 2: show 'fish+1' on screen
            if state.fade_flag_fish == True:
                if fade_time_fish >= 0:
                    msg_fade_minus.draw(settings)
                    fish_fade.draw()
                    fade_time_fish -= elapsed_time
                elif fade_time_fish <  0:
                    state.fade_flag_fish = False


            for fish in state.fish:
                fish.draw()

            #'level-1'  initiate the level-1 settings
            if score % 750 == 0 and score != 0:
                if state.enter_level_flag == True:
                    state.fade_flag_level = True
                    fade_time_level = 0.5
                    
            #test then disable the previous part immediately to avoid initiating again the level settings 
            if score % 750 == 0 and score != 0:
                state.enter_level_flag = False
            else:
                state.enter_level_flag = True
            
            #draw 'level-1' on screen in the fade time
            if state.fade_flag_level == True:
                if fade_time_level >= 0:
                    msg_fade_plus.draw(settings)
                    fade_time_level -= elapsed_time
                elif fade_time_level < 0:
                    state.fade_flag_level = False

            #draw
            sb.draw_score()
            cat_symbol.draw()
            multiply.draw()
            void_button.draw()
            home_button.draw()
            cursor_paw.draw_paw()

            end_time = time.time()
            elapsed_time = end_time - start_time
    else:
        cursor_paw = Cursor_Paw(screen)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if state.about_flag == False:  
            for event in pygame.event.get():
                for button in (play_button,exit_button,about_button):
                    #if mouse on button, change font and color
                    if button.msg_text_rect.collidepoint(mouse_x, mouse_y):

                        button.msg_text = settings.button_font_new.render(button.msg, True, settings.button_text_color_new,settings.button_color)
                        if button.pop_flag == True:
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound(pop))
                            button.pop_flag = False
                    else:
                        button.msg_text = settings.button_font.render(button.msg, True, settings.button_text_color,settings.button_color)
                        button.pop_flag = True
                       
                    #if button down, change font and color
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if play_button.msg_text_rect.collidepoint(mouse_x, mouse_y):
                            state.active = True
                            pygame.mixer.music.stop()
                            stopped = True
                            break
                        if exit_button.msg_text_rect.collidepoint(mouse_x,mouse_y):
                            sys.exit()

                        if about_button.msg_text_rect.collidepoint(mouse_x,mouse_y):
                            state.about_flag = True


            #draw buttons        
            screen.blit(bg0, (0, 0))
            play_button.draw(settings)
            exit_button.draw(settings)
            about_button.draw(settings)
            
                   
        else:
            screen.blit(bg0, (0, 0))
            return_button.draw(settings)
            
            #if mouse on button, change font and color
            if return_button.msg_text_rect.collidepoint(mouse_x, mouse_y):

                return_button.msg_text = settings.return_button_font.render(return_button.msg, True, settings.button_text_color_new,settings.button_color)
                if return_button.pop_flag == True:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(pop))
                    return_button.pop_flag = False
            else:
                return_button.msg_text = settings.return_button_font.render(return_button.msg, True, settings.button_text_color,settings.button_color)
                return_button.pop_flag = True

            #if button down, change font and color
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button.return_rect.collidepoint(mouse_x,mouse_y):
                        state.about_flag = False

            cursor_paw.draw_paw()


        cursor_paw.draw_paw()

    pygame.display.flip()
    if not pygame.mixer.music.get_busy():
        music = 'music/bg_music.wav' if state.active else 'music/pre_music.wav'
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

