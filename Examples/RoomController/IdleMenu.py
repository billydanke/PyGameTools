import PyGameComponents
import EventManager
import Clock
import Weather

class IdleMenu():
    def __init__(self):
        self.width = 800
        self.height = 480
        self.color = (255,255,255,0)

        self.displayMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])

        # ----- Background Rectangle -----
        self.displayMenu.addContentItem(PyGameComponents.Rectangle(0,0,self.width,self.height,(0,0,0)))

        # ----- Button to Wake -----
        self.displayMenu.addContentItem(PyGameComponents.Button('Images/transparentButton.png','Images/transparentButton.png', 0,0, None, self.WakeFromIdle, self.width,self.height))

        # ----- Display Clock -----
        self.displayMenu.addContentItem(Clock.Clock(self.width/2, self.height/2 - 20, 40, (255,255,255), False, False, 'arial', True))

        # ----- Display Weather -----
        self.displayMenu.addContentItem(Weather.WeatherDisplay(self.width/2 - 70, self.height/2 + 5, 60, 30, 10,40, 5))

        # ----- Display Next Alarm -----

        # ----- Display Wakeup Notice -----
        self.displayMenu.addContentItem(PyGameComponents.Text(self.width/2, self.height - 30, "Tap Anywhere to Wake", 'arial', 25, (100,100,100)))

        self.WakeFromIdle()

    def WakeFromIdle(self):
        EventManager.isIdle = False
        self.displayMenu.disableWithContents()

    def EnterIdle(self):
        self.displayMenu.enableWithContents(EventManager.screen)
