import EventManager
import PyGameComponents
import EyeBall
import pygame
import FaceTracking

width = EventManager.windowSize[0]
height = EventManager.windowSize[1]

pygame.init()
pygame.display.set_caption("Eyeball Tracking Demo")

menu = PyGameComponents.Menu(0,0,width,height,(150,150,150,255),[])

eyeball = EyeBall.EyeBall(width/2,height/2,150)

menu.addContentItem(PyGameComponents.Rectangle(220,10,360,height-20,(50,50,50),255,0,20))
menu.addContentItem(PyGameComponents.Rectangle(220,10,360,height-20,(200,200,200),255,10,20))
menu.addContentItem(eyeball)

menu.isDrawn = True

def draw():

    menu.draw(EventManager.screen)

    pygame.display.flip()

def logicLoop():
    EventManager.logicClock.tick(33)
    EventManager.EventManager.Check()

    faceRect = FaceTracking.getFacePosition()

    if(faceRect is not None):
        x = faceRect[0] + faceRect[2]/2
        y = faceRect[1] + faceRect[3]/2

        px = x / 1920.0
        py = y / 1080.0

        #print(px,py)

        eyeball.setLookPosition(px,py)
    else:
        pass
        #eyeball.setLookPosition(0.5,0.5)

    draw()


# Logic Loop
while EventManager.running:
    logicLoop()

# Done! Time to quit.
pygame.quit()

# End the program
quit()