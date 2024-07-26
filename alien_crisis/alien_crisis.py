import sys
import pygame
from game_settings import Game_settings
from spacecraft import Spacecraft
import get_action
from alien_spacecraft import Alien



def game():
    count=0
    killnumber=0
    lifes=5
    pygame.init()
    game_settings=Game_settings()
    normal_back = pygame.image.load("background.jpeg")
    red_back=pygame.image.load("redbackground.jpg")
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Alien Crisis')
    spacecraft = Spacecraft(game_settings,screen.get_rect(),"sun ship.png")
    mk_action=[-1,-1,-1,-1,-1,-1,-1,-1]
    aliengroup=[]
    red=False
    font = pygame.font.Font('Varelmo.ttf',50)
    while True:
        red_overlay = pygame.Surface((game_settings.screen_width, game_settings.screen_height))
        red_overlay.set_alpha(0)  # 设置透明度（0-255）
        red_overlay.fill((255,0,0))
        if red:
            background_image=red_back
        else:
            background_image=normal_back
        screen.blit(background_image, (0, 0))
        mk_action=get_action.check_events(mk_action)
        
        if lifes>0:
            # spacecraft.update()
            pass
            
            

            spacecraft.move(screen,mk_action[0],mk_action[1])
            spacecraft.fire(screen,mk_action[2:],count)
            
            if count%100==0:
                aliengroup.append(Alien(game_settings,screen.get_rect(),"alienship.png"))
            spacecraft.draw(screen)
            

            for n in range(len(aliengroup)-1,-1,-1):
                i=aliengroup[n]
                i.move(spacecraft)
                i.draw(screen)
                if spacecraft.test(i):
                    del aliengroup[n]
                    killnumber+=1
                if spacecraft.testcollide(i):
                    if count>100:
                        lifes-=1
                        count=0
                        red=True
                if count>50:
                    red=False
                
                    
                
            

                    
            killnumbertext=font.render(str(killnumber),True,(255,0,0))
            killnumbertextRect =killnumbertext.get_rect() 
            killnumbertextRect.bottomleft = (20,70)
            screen.blit(killnumbertext,killnumbertextRect)
                
            lifetext=font.render(str(lifes),True,(255,0,0))
            lifetextRect =lifetext.get_rect() 
            lifetextRect.bottomright = (1180,70)
            screen.blit(lifetext,lifetextRect)
            
            
            
            
            
            
        else:
            if count%250<125:
                font = pygame.font.Font('Varelmo.ttf',50)
                gameovertext=font.render("Game Over",True,(255,0,0))
                gameovertextRect =gameovertext.get_rect() 
                gameovertextRect.center = (600,250)
                screen.blit(gameovertext,gameovertextRect)
                
                
            font = pygame.font.Font('Varelmo.ttf',30)

            retext=font.render("Play Again(R)",True,(255,0,0))
            retextRect =retext.get_rect() 
            retextRect.center = (600,350)
            screen.blit(retext,retextRect)
            
            quittext=font.render("Quit Game(Q)",True,(255,0,0))
            quitrtextRect =quittext.get_rect() 
            quitrtextRect.center = (600,450)
            screen.blit(quittext,quitrtextRect)
            
            if mk_action[7]==1:
                game()
            if mk_action[6]==1:
                sys.exit()
                
        pygame.display.flip()
        count+=1
        if count==10000:
                count=0
        
            
            
        
        


    
game()
    
    