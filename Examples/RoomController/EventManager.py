import pygame
from datetime import datetime
import Location
import Weather
import asyncio

buttonList = []
screen = pygame.display.set_mode((800,480))
running = True
isIdle = False
currentLocation = Location.getCurrentCity()
logicClock = pygame.time.Clock()
lastInteractionTimestamp = datetime.now()

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
        # Button hover effects
        #for b in buttonList:
        #    if b.rect.collidepoint(pygame.mouse.get_pos()) and b.isDrawn:
        #        b.color = ()

        # Idle Time Check
        global lastInteractionTimestamp
        global isIdle
        currentTime = datetime.now()
        timeDifference = currentTime - lastInteractionTimestamp

        if(timeDifference.seconds > 10 and not isIdle):
            print("Idle!")
            isIdle = True

        # Weather Update Check
        Weather.ClockTick()

        if(Weather.timeSinceLastWeatherCall > Weather.refreshMinutes * 60000):
                asyncio.run(Weather.UpdateWeather())
                Weather.timeSinceLastWeatherCall = 0

        # Event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
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