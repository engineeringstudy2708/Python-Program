import pygame,sys

import time

import random

pygame.init()

red=(255,0,0)
black=(100,0,0)
white=(255,255,255)

window_width=600
window_height=400
score=0


gameDisplay=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("The Snake Game")
clock=pygame.time.Clock()

FPS=5 #Frame per second //It also manage the speed of a game change

blockSize=20

nopixel=0

def myquit():
    pygame.quit()
    sys.exit()


font=pygame.font.SysFont(None,25,bold=True,italic=True) #Sysfont(name,size,bold=True/False,italic=True/False)

#def drawGrid():
#    sizeGrd=window_width//blocksize

def snake(blockSize,snakelist):

    for size in snakelist:   
        
        pygame.draw.rect(gameDisplay,black,[size[0]+5,size[1],blockSize,blockSize],0) #rect(screen,color,sizeofrect,width (width==0 fill thr rect,width >0 draw a outline rect ,width<0 nothing will draw

def message_to_screen(msg,color):

    screen_txt=font.render(msg,True,color,black) # draw text on a surface render(text,antialias(means quality of msg),color,background=None) 
    
    gameDisplay.blit(screen_txt,[window_width*0.2,window_height*0.4]) #blit() draw one image on another #(blit(msg_to_screen,(x,y))


#Heart of the game
    
def gameLoop():
    
    gameExit=False
    gameOver=False
    global score
    lead_x=window_width/2
    lead_y=window_height/2

    change_pixels_of_x=0
    change_pixels_of_y=0

    snakelist=[]

    snakeLength=1
    
    print("Kishan game")
    randomAppleX=round(random.randrange(0,window_width-blockSize)/10.0)*10.0
    randomAppleY=round(random.randrange(0,window_height-blockSize)/10.0)*10.0

    while not gameExit:
        
        while gameOver==True:
            gameDisplay.fill(white)
            message_to_screen("Game Over,press C to Play Again or Q to quit",red)
            message_to_screen(score,red)
            pygame.display.update()

            for event in pygame.event.get():
                
                if (event.type==pygame.QUIT):
                    gameOver=False
                    gameExit=True
                    
                if (event.type==pygame.KEYDOWN):
                    if (event.key==pygame.K_q):
                        gameOver=False
                        gameExit=True
                    if (event.key==pygame.K_c):
                        gameLoop()

        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                gameExit=True
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_ESCAPE):
                    myquit()

                leftArrow=event.key==pygame.K_LEFT
                rightArrow=event.key==pygame.K_RIGHT
                upArrow=event.key==pygame.K_UP
                downArrow=event.key==pygame.K_DOWN

                if(leftArrow):
                    change_pixels_of_x=-blockSize
                    change_pixels_of_y=nopixel
                elif(rightArrow):
                    change_pixels_of_x=blockSize
                    change_pixels_of_y=nopixel
                elif(upArrow):
                    change_pixels_of_y=-blockSize
                    change_pixels_of_x=nopixel
                elif(downArrow):
                    change_pixels_of_y=blockSize
                    change_pixels_of_x=nopixel
            if (lead_x >= window_width or lead_x<0 or lead_y >=window_height or lead_y<0):
                gameOver=True
                    
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill(white )

        AppleThickness=20

        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness]) #print the apples position (x,y,thickness.thickness)

        pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        
        allspriteslist=[]
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)

        
        if(len(snakelist) > snakeLength ):
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if (eachSegment == allspriteslist):
                gameOver=True

        snake(blockSize,snakelist)

        pygame.display.update()
                    
        if (lead_x >=randomAppleX and lead_x<=randomAppleX+AppleThickness):
                
            if (lead_y >=randomAppleY and lead_y<=randomAppleY+AppleThickness):

                randomAppleX=round(random.randrange(0,window_width-blockSize)/10.0)*10.0
                randomAppleY=round(random.randrange(0,window_height-blockSize)/10.0)*10.0
                snakeLength +=1
                score+=1
               
        clock.tick(FPS)
        message_to_screen(print("Score :",score),red)
        #pygame.display.update()
    pygame.quit()

    quit()


gameLoop()

                      

                        
                    
