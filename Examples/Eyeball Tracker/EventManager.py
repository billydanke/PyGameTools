import pygame
from datetime import datetime
import FaceTracking

buttonList = []
windowSize = (800,600)
screen = pygame.display.set_mode(windowSize)
running = True
isIdle = False
logicClock = pygame.time.Clock()
lastInteractionTimestamp = datetime.now()

FaceTracking.StartCamera()

class EventManager():
    def __init__(self):
        pass
    
    def GetTime(is24H = True,showSeconds=False):
        if(is24H):
            if(showSeconds):
                return(datetime.now().strftime("%H:%M:%S"))
            else:
                return(datetime.now().strftime("%H:%M"))
        else:
            if(showSeconds):
                return(datetime.now().strftime("%I:%M:%S %p"))
            else:
                return(datetime.now().strftime("%I:%M %p"))

    def Check():

        # Idle Time Check
        global lastInteractionTimestamp
        global isIdle
        currentTime = datetime.now()
        timeDifference = currentTime - lastInteractionTimestamp

        if(timeDifference.seconds > 10 and not isIdle):
            print("Idle!")
            isIdle = True

        # Event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
                FaceTracking.CloseCamera()
            if event.type == pygame.MOUSEBUTTONDOWN:
                lastInteractionTimestamp = datetime.now()
                if event.button == 1:
                    for b in buttonList:
                        if b.rect.collidepoint(pygame.mouse.get_pos()) and b.isDrawn:
                            b.pressDown()
            if event.type == pygame.MOUSEBUTTONUP:
                lastInteractionTimestamp = datetime.now()
                if event.button	== 1:
                    for b in buttonList:
                        if b.pressed:
                            b.pressUp()