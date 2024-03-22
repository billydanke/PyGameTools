import MainMenu
import IdleMenu
import EventManager
import pygame
import time

pygame.init()

mainMenu = MainMenu.MainMenu()
mainMenu.DisableAllMenus()

idleMenu = IdleMenu.IdleMenu()

def draw():
    if(not EventManager.isIdle):
        if(not mainMenu.universalMenu.isDrawn):
            mainMenu.EnableFromIdle()

        mainMenu.universalMenu.draw(EventManager.screen)
        mainMenu.lightMenu.draw(EventManager.screen)
        mainMenu.shelfMenu.draw(EventManager.screen)
        mainMenu.accessoryMenu.draw(EventManager.screen)
        mainMenu.clockMenu.draw(EventManager.screen)
    else:
        if(not idleMenu.displayMenu.isDrawn):
            mainMenu.DisableForIdle()
            idleMenu.EnterIdle()

        idleMenu.displayMenu.draw(EventManager.screen)

    pygame.display.flip()

def logicLoop():
    EventManager.logicClock.tick(33)
    EventManager.EventManager.Check()
    draw()


# Logic Loop
while EventManager.running:
    logicLoop()

# Done! Time to quit.
pygame.quit()

# End the program
quit()