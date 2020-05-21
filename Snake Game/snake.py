import pygame
import pygame.gfxdraw
import time
import random

pygame.init()

display = pygame.display.set_mode(size=(800,600))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

clock  = pygame.time.Clock()

size = 1
xArray = [400]
yArray = [300]
bodyxArray = []
bodyyArray = []

xPosition = 400
yPosition = 300

xDelta = 0
yDelta = 0

score = 0

foodx = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
foody = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
foodExists = True

pygame.display.update()
pygame.display.set_caption("Snake Game by Robert Gan")

font_style = pygame.font.SysFont(None, 50)

def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x,y])

# def draw(x,y, color):
#     pygame.gfxdraw.box(display, [x,y,10,10], color)

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
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
    
    if xPosition >= 800 or xPosition <0 or yPosition >= 600 or yPosition < 0:
            gameOver = True 
            xDelta = 0
            yDelta = 0
    
    if xPosition == foodx and yPosition == foody:
        print("Eaten")
        score += 1
        size += 1
        foodx = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
        foody = int(round(random.randrange(0, 800 - 10) / 10.0) * 10.0)
#         pygame.gfxdraw.box(display,[foodx,foody,10,10],blue)

    xPosition += xDelta
    yPosition += yDelta
    
    if xDelta !=0 or yDelta != 0:
        xArray.insert(0,xPosition)
        yArray.insert(0,yPosition)
    
    xArray = xArray[:size]
    yArray = yArray[:size]
    bodyxArray = xArray[1:size]
    bodyyArray = yArray[1:size]

    display.fill((0,0,0))
    pygame.gfxdraw.box(display,[foodx,foody,10,10],blue)
    pygame.display.flip()
    
    for i in range(len(xArray)):
        pygame.draw.rect(display,red,[xArray[i],yArray[i],10,10])
        
    for i in range(len(bodyxArray)):
        if xPosition == bodyxArray[i] and yPosition == bodyyArray[i]:
            gameOver = True

    message("Score: " + str(score), red, 0, 0)
    pygame.display.update()
    pygame.display.flip()

    clock.tick(30)

message("Game Over", red, 325, 200)
# pygame.display.update()
pygame.display.flip()
time.sleep(3)
pygame.quit()
quit()                         