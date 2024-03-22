import PyGameComponents
import EventManager

class Clock():
    def __init__(self,x,y,fontSize,textColor,is24H=False,showSeconds=False,font='arial',isBold=False):
        self.x = x
        self.y = y
        self.fontSize = fontSize
        self.textColor = textColor
        self.font = font
        self.isBold = isBold
        self.is24H = is24H
        self.showSeconds = showSeconds
        self.timeString = EventManager.EventManager.GetTime(self.is24H,self.showSeconds)
        self.textComponent = PyGameComponents.Text(self.x,self.y,self.timeString,self.font,self.fontSize,self.textColor,self.isBold)

        self.isDrawn = True

    def UpdateTime(self):
        self.timeString = EventManager.EventManager.GetTime(self.is24H)
        self.textComponent.changeText(self.timeString)

    def draw(self,screen):
        if(self.isDrawn):
            self.UpdateTime()
            self.textComponent.draw(screen)