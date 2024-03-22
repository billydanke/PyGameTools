import PyGameComponents
import EventManager
import Clock
import Weather
import ColorCircle

class MainMenu():
    def __init__(self):
        self.width = 800
        self.height = 480
        self.color = (255,255,255,0)

        self.universalMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])
        self.lightMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])
        self.shelfMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])
        self.accessoryMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])
        self.clockMenu = PyGameComponents.Menu(0,0,self.width,self.height,self.color,[])

        # ----- Header Bar -----
        self.universalMenu.addContentItem(PyGameComponents.Entity('Images/mountainBlurred.jpg',0,0,800,480))
        self.universalMenu.addContentItem(PyGameComponents.Rectangle(0,0,800,50,(50,50,50,200)))
        self.universalMenu.addContentItem(Clock.Clock(400,25,30,(255,255,255),False,False,'arial',True))
        self.universalMenu.addContentItem(Weather.WeatherDisplay(675,5,40,20,11,27))
        
        # ----- Side Buttons -----
        self.universalMenu.addContentItem(PyGameComponents.Rectangle(10,60,150,100, (255,100,100), 100, id="lightingButtonRectangle"))
        self.universalMenu.addContentItem(PyGameComponents.Button('Images/transparentButton.png','Images/transparentButton.png',10,60,None,self.LoadLightMenu, 150, 100))
        #self.universalMenu.addContentItem(PyGameComponents.Text(85,107.5,"Lighting",'arial',20,(255,255,255),True))
        self.universalMenu.addContentItem(PyGameComponents.Entity('Images/SideButtonIcons/HueLightingIcon.png', 48, 75, 72,72, "hueLightingIcon"))

        self.universalMenu.addContentItem(PyGameComponents.Rectangle(10,165,150,100, (255,100,100), 100, id="shelfButtonRectangle"))
        self.universalMenu.addContentItem(PyGameComponents.Button('Images/transparentButton.png','Images/transparentButton.png',10,165,None,self.LoadShelfMenu, 150, 100))
        #self.universalMenu.addContentItem(PyGameComponents.Text(85,212.5,"Shelf",'arial',20,(255,255,255),True))
        self.universalMenu.addContentItem(PyGameComponents.Entity('Images/SideButtonIcons/ShelfLightingIcon.png', 48, 180, 72,72, "shelfLightingIcon"))

        self.universalMenu.addContentItem(PyGameComponents.Rectangle(10,270,150,100, (255,100,100), 100, id="accessoryButtonRectangle"))
        self.universalMenu.addContentItem(PyGameComponents.Button('Images/transparentButton.png','Images/transparentButton.png',10,270,None,self.LoadAccessoryMenu, 150, 100))
        #self.universalMenu.addContentItem(PyGameComponents.Text(85,317.5,"Accessory Lights",'arial',20,(255,255,255),True))
        self.universalMenu.addContentItem(PyGameComponents.Entity('Images/SideButtonIcons/AccessoryLightingIcon.png', 48, 285, 72,72, "accessoryLightingIcon"))

        self.universalMenu.addContentItem(PyGameComponents.Rectangle(10,375,150,100, (255,100,100), 100, id="clockButtonRectangle"))
        self.universalMenu.addContentItem(PyGameComponents.Button('Images/transparentButton.png','Images/transparentButton.png',10,375,None,self.LoadClockMenu, 150, 100))
        #self.universalMenu.addContentItem(PyGameComponents.Text(85,422.5,"Clock & Alarm",'arial',20,(255,255,255),True))
        self.universalMenu.addContentItem(PyGameComponents.Entity('Images/SideButtonIcons/ClockIcon.png', 48, 390, 72,72, "clockIcon"))

        self.universalMenu.addContentItem(PyGameComponents.Line((160,50),(160,480), 3, (255,255,255), True))

        # ----- Main Window Background Rectangles -----
        self.universalMenu.addContentItem(PyGameComponents.Rectangle(170,60, 620, 410, (255,100,100), 100, 0, 20))
        self.universalMenu.addContentItem(PyGameComponents.Rectangle(170,60, 620, 410, (255,100,100), 255, 5, 20))

        # ----- Lighting Menu Contents -----
        self.lightMenu.addContentItem(PyGameComponents.Text(480,90,"Phillips Hue Lighting", 'arial', 30, (255,255,255), True))
        self.lightMenu.addContentItem(PyGameComponents.Circle(600,285,155,(100,100,100)))
        self.lightMenu.addContentItem(ColorCircle.ColorCircle(600,285,300,10))
        self.lightMenu.disableWithContents()

        # ----- Shelf Menu Contents -----
        self.shelfMenu.addContentItem(PyGameComponents.Text(480,90,"LED Shelf Control", 'arial', 30, (255,255,255), True))

        # ----- Accessory Lighting Menu Contents -----
        self.accessoryMenu.addContentItem(PyGameComponents.Text(480,90,"Accessory Lighting", 'arial', 30, (255,255,255), True))

        # ----- Clock & Alarms Menu Contents -----
        self.clockMenu.addContentItem(PyGameComponents.Text(480,90,"Clock & Alarms", 'arial', 30, (255,255,255), True))

    def LoadLightMenu(self):
        self.DisableAllMenus()
        self.lightMenu.enableWithContents(EventManager.screen)
        self.SetSideButton('lightingButtonRectangle',255)
        self.SetSideButtonIcon('hueLightingIcon', 'Images/SideButtonIcons/HueLightingIconSelected.png')

    def LoadShelfMenu(self):
        self.DisableAllMenus()
        self.shelfMenu.enableWithContents(EventManager.screen)
        self.SetSideButton('shelfButtonRectangle',255)
        self.SetSideButtonIcon('shelfLightingIcon', 'Images/SideButtonIcons/ShelfLightingIconSelected.png')

    def LoadAccessoryMenu(self):
        self.DisableAllMenus()
        self.accessoryMenu.enableWithContents(EventManager.screen)
        self.SetSideButton('accessoryButtonRectangle',255)
        self.SetSideButtonIcon('accessoryLightingIcon', 'Images/SideButtonIcons/AccessoryLightingIconSelected.png')

    def LoadClockMenu(self):
        self.DisableAllMenus()
        self.clockMenu.enableWithContents(EventManager.screen)
        self.SetSideButton('clockButtonRectangle',255)
        self.SetSideButtonIcon('clockIcon', 'Images/SideButtonIcons/ClockIconSelected.png')


    def SetSideButton(self, id, alpha):
        for i,item in enumerate(self.universalMenu.contents):
            if(type(item) == PyGameComponents.Rectangle):
                if(item.id == id):
                    x = self.universalMenu.contents[i].x
                    y = self.universalMenu.contents[i].y
                    width = self.universalMenu.contents[i].surf.get_width()
                    height = self.universalMenu.contents[i].surf.get_height()
                    color = self.universalMenu.contents[i].color

                    self.universalMenu.contents[i] = PyGameComponents.Rectangle(x,y,width,height,color,alpha,id=id)

    def SetSideButtonIcon(self, id, source):
        for i,item in enumerate(self.universalMenu.contents):
            if(type(item) == PyGameComponents.Entity):
                if(item.id == id):
                    item.changeSrc(source)

    def DisableAllMenus(self):
        self.lightMenu.disableWithContents()
        self.shelfMenu.disableWithContents()
        self.accessoryMenu.disableWithContents()
        self.clockMenu.disableWithContents()

        self.SetSideButton('lightingButtonRectangle',100)
        self.SetSideButton('shelfButtonRectangle',100)
        self.SetSideButton('accessoryButtonRectangle',100)
        self.SetSideButton('clockButtonRectangle',100)

        self.SetSideButtonIcon('hueLightingIcon', 'Images/SideButtonIcons/HueLightingIcon.png')
        self.SetSideButtonIcon('shelfLightingIcon', 'Images/SideButtonIcons/ShelfLightingIcon.png')
        self.SetSideButtonIcon('accessoryLightingIcon', 'Images/SideButtonIcons/AccessoryLightingIcon.png')
        self.SetSideButtonIcon('clockIcon', 'Images/SideButtonIcons/ClockIcon.png')

    def DisableForIdle(self):
        self.DisableAllMenus()
        self.universalMenu.disableWithContents()

    def EnableFromIdle(self):
        self.universalMenu.enableWithContents(EventManager.screen)