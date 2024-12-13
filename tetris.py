import pygame
import sys
from tetrisgame import Game
from tetriscolor import colors

pygame.init() #initailizes the pygame module

title_font=pygame.font.Font(None,40)
score_surface=title_font.render("Score",True,(colors.white))

next_surface=title_font.render("Next",True,(colors.white))
score_rect=pygame.Rect(320,55,170,60)

game_over_surface=title_font.render("Game Over",True,colors.white)
next_rect=pygame.Rect(320,215,170,180)


screen=pygame.display.set_mode((500,620))#creates the display surface
pygame.display.set_caption("Python Tetris")#Giving title

clock=pygame.time.Clock()
game=Game()

GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,250) 
#What to do during Game loop
#Event Handling
#Updating Positons
#Drawing Objects
while True:
    for event in pygame.event.get():#Gets all the events the pygame recognizes
        if event.type==pygame.QUIT:
            pygame.quit#what is this
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if game.gameover==True:
                game.gameover=False
                game.reset()
            if event.key==pygame.K_LEFT and game.gameover==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.gameover==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.gameover==False:
                game.move_down()
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.gameover==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.gameover==False:
            game.move_down()

    #displaying the screen
    score_value_surface=title_font.render(str(game.score),True,colors.white)

    screen.fill(colors.dark_blue)
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface,(375,180,50,50))
    
    if game.gameover==True:
        screen.blit(game_over_surface,(320,450,50,50))

    pygame.draw.rect(screen,colors.light_blue,score_rect,0,10)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
    pygame.draw.rect(screen,colors.light_blue,next_rect,0,10)
    game.draw(screen)
    

    pygame.display.update()
    clock.tick(60)

   

    #pygame.display.set_mode is display surface and can only be called once per game and is used by calling update function
    #surface we can have many in the game
    #Rect Rectangles are used for positioning, collision detection and for drawing objects.

