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
screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
pygame.display.set_caption("Catch Mitao!")

bg0 = pygame.image.load('images/bg0.png')
icon = pygame.image.load('images/icon.png')

duration = 0
time_left = 0
fade_time_fish = 0
fade_time_level = 0

cat_position = {0:(600,400)}
cat_sequence = 0

score = 0
get_score = 50

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

play_button = Play_Button(screen, settings)
exit_button = Exit_Button(screen, settings)
about_button = About_Button(screen, settings)
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


music_flag = True
about_flag = False
three_button_flag = True
break_flag = True
generate_flag = False
fade_flag_fish = False
home_flag = False
fade_flag_level = False
enter_level_flag = True

while True:
    
    if state.active:

        fade_time_home = 0
        music_flag = True

        #produce bg music
        
        pygame.mixer.music.load('music/bg_music.wav')
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cursor_paw = Cursor_Paw(screen)
            start_time = time.time()
            if home_flag == True:
                if fade_time_home >= 0:
                    screen.fill(settings.bg_color)
                    game_over.draw(settings)
                    fade_time_home -= duration
                    pygame.display.flip()
                elif fade_time_home <  0:
                    state.active = False
                    home_flag = False
                    break
            elif home_flag == False:
                
                settings.generation_time = 0.7 * (0.9**(score // 750))
                for event in pygame.event.get():

                    if event.type  == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for cat in state.cats:
                            if cat.cat.rect.collidepoint(mouse_x, mouse_y):
                                state.cats.remove(cat)
                                cat_position.pop(cat.sequence)

                                #produce the sound
                                pygame.mixer.Channel(0).play(cat_meow)

                                #deal with score
                                d = shelve.open('data/score') 

                                #update score

                                score = score + get_score
                                #print(score)
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
                            break_flag = True
                            state.initiate(sb,play_button,settings,screen,state)
                            cat_position = {0:(600,400)}
                            score = 0
                            
                            break

                if break_flag == True:
                    break_flag = False
                    break
                
                #control the animation of each boxed cat(distance, time)  
                time_left -= duration
                
                
                if time_left < 0:
                    
                    while generate_flag == False:
                        distance_list = []
                        x = random.randint(100,1100)
                        y = random.randint(200,700)
                        for each_pair in cat_position.values():
                            distance = math.sqrt((x-each_pair[0])**2 + (y-each_pair[1])**2)
                            distance_list.append(distance)
         
                        if min(distance_list) > 200:
                            cat = BoxedCat(screen, x, y) 
                            cat_sequence = cat_sequence + 1
                            cat.sequence = cat_sequence
                            cat_position[cat.sequence] = (x,y)
                            state.cats.append(cat)
                            generate_flag == True
                            break
                      
                    time_left = settings.generation_time

                for cat in state.cats:
                    if not cat.is_animating:
                        cat.animate(0.5)
                    cat.update(state,cat_position)


                #draw boxed cats, add 'screen.fill' to product the animation effect
                screen.fill(settings.bg_color)

                for cat in state.cats:
                    cat.draw()
                
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
                            
                            fade_flag_fish = True

                            cat_position = {0:(600,400)}
                            
                            state.fish = []
                            
                            sb.prep_fish(state,screen)

                            continue

                        elif state.fish_left <= 1: 
                            fade_time_home = 3
                            state.initiate(sb,play_button,settings,screen,state)
                            cat_position = {0:(600,400)}
                            score = 0
                            home_flag = True

                
                              
                           
                # prep fish part 2: show 'fish+1' on screen
                if fade_flag_fish == True:
                    if fade_time_fish >= 0:
                        msg_fade_minus.draw(settings)
                        fish_fade.draw()
                        fade_time_fish -= duration
                    elif fade_time_fish <  0:
                        fade_flag_fish = False


                for fish in state.fish:
                    fish.draw()



                #'level-1'  initiate the level-1 settings
                if score % 750 == 0 and score != 0:
                    if enter_level_flag == True:
                        fade_flag_level = True
                        fade_time_level = 0.5
                        
                #test then disable the previous part immediately to avoid initiating again the level settings 
                if score % 750 == 0 and score != 0:
                    enter_level_flag = False
                else:
                    enter_level_flag = True
                
                #draw 'level-1' on screen in the fade time
                if fade_flag_level == True:
                    if fade_time_level >= 0:
                        msg_fade_plus.draw(settings)
                        fade_time_level -= duration
                    elif fade_time_level < 0:
                        fade_flag_level = False

                #draw
                sb.draw_score()
                cat_symbol.draw()
                multiply.draw()
                void_button.draw()
                home_button.draw()
                cursor_paw.draw_paw()



                pygame.display.flip()
                

            end_time = time.time()
            duration = end_time - start_time


    else:

        pygame.mixer.music.load('music/pre_music.wav')
        pygame.mixer.music.play()

       
        while pygame.mixer.music.get_busy() and music_flag:

            cursor_paw = Cursor_Paw(screen)
                
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if about_flag == False:  
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
                                music_flag = False
                                break
                            if exit_button.msg_text_rect.collidepoint(mouse_x,mouse_y):
                                sys.exit()

                            if about_button.msg_text_rect.collidepoint(mouse_x,mouse_y):
                                about_flag = True


                #draw buttons        
                screen.blit(bg0, (0, 0))
                play_button.draw(settings)
                exit_button.draw(settings)
                about_button.draw(settings)
                screen.blit(icon, (220,300))
                screen.blit(icon, (480,300))
                screen.blit(icon, (710,300))
                       
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
                            about_flag = False

                cursor_paw.draw_paw()
                pygame.display.flip()


            cursor_paw.draw_paw()
            pygame.display.flip()

