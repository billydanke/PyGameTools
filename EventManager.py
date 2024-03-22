import pygame
from datetime import datetime

buttonList = []
windowSize = (1280,720)
screen = pygame.display.set_mode(windowSize)
running = True
logicClock = pygame.time.Clock()
lastInteractionTimestamp = datetime.now()

class EventManager():
    def __init__(self):
        pass

    def Check():

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