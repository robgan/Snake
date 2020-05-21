import pygame
import pygame.gfxdraw
import time
import random

pygame.init()

#Create display
display = pygame.display.set_mode(size=(800,600))
#Colors
red = (255,0,0)
blue = (0,0,255)
#Clock functionality
clock  = pygame.time.Clock()
#Creating arrays for future use
size = 1
xArray = [400]
yArray = [300]
bodyxArray = []
bodyyArray = []
#Initializing the starting position, direction of motion, and score
xPosition = 400
yPosition = 300

xDelta = 0
yDelta = 0

score = 0
#Initializing the food location randomly
foodx = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
foody = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)

pygame.display.update()
pygame.display.set_caption("Snake Game by Robert Gan")

font_style = pygame.font.SysFont(None, 50)
#Method to create a textbox
def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x,y])

gameOver = False
#Loop that controls the game functions
while not gameOver:
    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            gameOver = True
        #Controls using the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xDelta = -10
                yDelta = 0
            elif event.key == pygame.K_RIGHT:
                xDelta = 10
                yDelta = 0
            elif event.key == pygame.K_UP:
                xDelta = 0
                yDelta = -10
            elif event.key == pygame.K_DOWN:
                xDelta = 0
                yDelta = 10
    #Making the edges of the screen out of bounds
    if xPosition >= 800 or xPosition <0 or yPosition >= 600 or yPosition < 0:
            gameOver = True 
            xDelta = 0
            yDelta = 0
    #Checks if the snake eats the food and then creates a new food
    if xPosition == foodx and yPosition == foody:
        print("Eaten")
        score += 1
        size += 1
        foodx = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
        foody = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
    #Changes the position of the snake
    xPosition += xDelta
    yPosition += yDelta
    #Adding the position of the snake to an array
    if xDelta !=0 or yDelta != 0:
        xArray.insert(0,xPosition)
        yArray.insert(0,yPosition)
    #Cutting the array down to a specific size that denotes the entire snake and the body of the snake
    xArray = xArray[:size]
    yArray = yArray[:size]
    bodyxArray = xArray[1:size]
    bodyyArray = yArray[1:size]
    #Draw the food
    display.fill((0,0,0))
    pygame.gfxdraw.box(display,[foodx,foody,10,10],blue)
    pygame.display.flip()
    #Draw the snake
    for i in range(len(xArray)):
        pygame.draw.rect(display,red,[xArray[i],yArray[i],10,10])
    #If snake runs into itself the game is over
    for i in range(len(bodyxArray)):
        if xPosition == bodyxArray[i] and yPosition == bodyyArray[i]:
            gameOver = True
    #Score display
    message("Score: " + str(score), red, 0, 0)
    pygame.display.update()
    pygame.display.flip()

    clock.tick(30)
#Game over message and automatic quit
message("Game Over", red, 325, 200)
pygame.display.flip()
time.sleep(3)
pygame.quit()
quit()                         