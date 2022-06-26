# the simple game making: snakes-xenia
from asyncio.windows_events import NULL
import pygame
from pygame import *
import random
pygame.init()



font = pygame.font.SysFont(None, 30)
def textScreen(text, color, x, y):
    screenText = font.render(text, True, color)
    gameWindow.blit(screenText, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_length, snake_width):
    for x,y in snake_list:

         pygame.draw.rect(gameWindow, white, [x, y, snake_length, snake_width ])



#colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
 

screen_width = 720
screen_height = 480
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes-Xeina")
pygame.display.update()




clock = pygame.time.Clock()

def gameLoop():

    exitGame = False
    gameOver = False
    snake_x = 75
    snake_y = 80
    snake_length = 10
    snake_width = 10
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(50,screen_width/2 )
    food_y = random.randint(50, screen_height/2 )
    score = 0
    velocity = 3
    snake_list =[]
    snake_size = 1

    # with open("hiscore.txt", "r") as f:
    #     hiscore = f.read()
        

    while exitGame != True:

        if gameOver:
            gameWindow.fill(black)
            textScreen("Game Over. Press 'Enter' to Continue", white, 180, 200)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
                    else:
                        NULL
        else:        
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exitGame = True

                elif event.type == pygame.KEYDOWN:
                    # print(event)
                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity 
                        velocity_y = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            velocity_y = velocity 
                            velocity_x = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            velocity_x = -velocity 
                            velocity_y = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            velocity_y = -velocity  
                            velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y                  
            
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score = score+10
                food_x = random.randint(50,screen_width/2 )
                food_y = random.randint(50, screen_height/2 )
                snake_size = snake_size + 5
                
                # if score > int(hiscore):
                #     hiscore = score

                # print(f"Score: {score}")
                # textScreen(s, red, 5, 5)
            gameWindow.fill(black)
            textScreen("Score:"+str(score) , red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10 ])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_size:
                del snake_list[0]

            if head in snake_list[:-1]:
                gameOver = True
            

            if snake_x<0 or snake_x > screen_width or snake_y<0 or snake_y > screen_height:
                gameOver =  True
                print("GAME OVER.... TRY HARDER")

            plot_snake(gameWindow, black, snake_list, snake_length, snake_width)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()
gameLoop()
