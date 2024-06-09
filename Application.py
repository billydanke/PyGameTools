import EventManager
import PyGameComponents
import pygame

pygame.init()

exampleCircle = PyGameComponents.Circle(100,150,30,(255,100,100))
exampleCircleHollow = PyGameComponents.Circle(200,150,32,(100,255,100),5)
exampleRectangle = PyGameComponents.Rectangle(100,300,50,100,(255,255,255),100,3,10)
exampleLine = PyGameComponents.Line((400,400),(450,450),2,(255,255,255),True)

menu = PyGameComponents.Menu(0,0,EventManager.windowSize[0],EventManager.windowSize[1],(30,30,30),[])

menu.addContentItem(exampleCircle) # Note that order you add content items to the menu is the draw order
menu.addContentItem(exampleCircleHollow)
menu.addContentItem(exampleRectangle)
menu.addContentItem(exampleLine)

menu.isDrawn = True

def draw():

    menu.draw(EventManager.screen)
    pygame.display.flip()

def logicLoop():
    EventManager.logicClock.tick(60) # Fps limiter. Currently, this is set to 60fps.
    EventManager.EventManager.Check()

    # This is where you can add whatever logic needs to happen every frame
    if(exampleCircle.x <= 1000):
        exampleCircle.x += 1
    else:
        exampleCircle.x = 100


    draw()


# Logic Loop
while EventManager.running:
    logicLoop()

# Done! Time to quit.
pygame.quit()

# End the program
quit()