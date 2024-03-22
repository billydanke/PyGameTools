import PyGameComponents
import EventManager
import pygame
import math
import ColorMath

class PointSelector():
    def __init__(self,x,y,circleCenterX,circleCenterY,circleSize,selectorSize,initialColor):
        self.x = x
        self.y = y
        self.circleCenterX = circleCenterX
        self.circleCenterY = circleCenterY
        self.circleSize = circleSize
        self.selectorSize = selectorSize
        self.colorRGB = initialColor
        self.colorHSV = None

        self.selectorCircle = PyGameComponents.Circle(self.x,self.y,self.selectorSize,(50,50,50),0)
        self.colorDisplayCircle = PyGameComponents.Circle(self.x,self.y,self.selectorSize*0.8,self.colorRGB,0)

        self.isDrawn = True
        self.followCursor = False

    def findAngle(self,point1,point2,isDegrees=False):
        angle = math.atan2(point1[1]-point2[1],point1[0]-point2[0])

        if(isDegrees):
            angle = angle*(180/math.pi)

        return angle

    def drag(self):
        if(self.followCursor):
            mousePosition = pygame.mouse.get_pos()
            
            if(math.dist(mousePosition,[self.circleCenterX,self.circleCenterY]) < self.circleSize/2):
                self.x = mousePosition[0]
                self.y = mousePosition[1]
                self.selectorCircle.setPosition(self.x,self.y)
                self.colorDisplayCircle.setPosition(self.x,self.y)
                self.setColor()
            else:
                angle = self.findAngle(mousePosition,[self.circleCenterX,self.circleCenterY])

                heightFromCenter = self.circleSize/2 * math.sin(angle)
                widthFromCenter = self.circleSize/2 * math.cos(angle)

                self.x = self.circleCenterX + widthFromCenter
                self.y = self.circleCenterY + heightFromCenter
                self.selectorCircle.setPosition(self.x,self.y)
                self.colorDisplayCircle.setPosition(self.x,self.y)
                self.setColor()

    def setColor(self):
        self.colorHSV = ColorMath.calculateHSV((self.circleCenterX,self.circleCenterY),self.circleSize/2,(self.x,self.y),255,255)
        self.colorRGB = ColorMath.HSV2RGB(self.colorHSV[0],self.colorHSV[1],self.colorHSV[2])
        self.colorDisplayCircle.color = self.colorRGB

    def draw(self,screen):
        if(self.isDrawn):
            self.drag()
            self.selectorCircle.draw(screen)
            self.colorDisplayCircle.draw(screen)


class ColorCircle():
    def __init__(self,x,y,circleSize,selectorSize):
        self.x = x
        self.y = y
        self.circleSize = circleSize
        self.selectorSize = selectorSize

        self.selectedPoint = (self.x+self.circleSize/2, self.y+self.circleSize/2)

        self.colorWheelEntity = PyGameComponents.Button('Images/colorCircle.png','Images/colorCircle.png',self.x - self.circleSize/2,self.y - self.circleSize/2, self.toggleSelectorDrag, self.toggleSelectorDrag, self.circleSize,self.circleSize)
        self.selector = PointSelector(self.x,self.y,self.x,self.y,self.circleSize,self.selectorSize,(255,255,255))

        self.isDrawn = True

    def toggleSelectorDrag(self):
        if(self.selector.followCursor == False):
            self.selector.followCursor = True
        else:
            self.selector.followCursor = False

    def draw(self,screen):
        if(self.isDrawn):
            self.colorWheelEntity.draw(screen)
            self.selector.draw(screen)