import pygame
import PyGameComponents
import EventManager

class EyeBall():
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.isDrawn = True
        self.outerFrame = PyGameComponents.Circle(self.x,self.y,self.radius,(100,100,100),int(self.radius*0.05))
        self.cornia = PyGameComponents.Circle(self.x,self.y,self.radius,(0,0,0))
        self.redGlow = PyGameComponents.Entity('Images/redGlow.png',int(self.x-self.radius*0.6),int(self.y-self.radius*0.6),self.radius*2*0.8,self.radius*2*0.8)
        self.iris = PyGameComponents.Circle(self.x,self.y,self.radius*0.6,(255,0,0))
        self.pupil = PyGameComponents.Circle(self.x,self.y,self.radius*0.3,(255,100,100))

    def setLookPosition(self,px,py):

        if(px > 1): px = 1
        if(py > 1): py = 1

        eyePX = self.x / EventManager.windowSize[0]
        eyePY = self.y / EventManager.windowSize[1]

        offsetPX = eyePX - px
        offsetPY = py - eyePY

        self.redGlow.x = int(self.x-self.radius*0.8) + int(offsetPX*self.radius*0.8)
        self.redGlow.rect.x = int(self.x-self.radius*0.8) + int(offsetPX*self.radius*0.8)
        self.redGlow.y = int(self.y-self.radius*0.8) + int(offsetPY*self.radius*0.8)
        self.redGlow.rect.y = int(self.y-self.radius*0.8) + int(offsetPY*self.radius*0.8)


        self.iris.x = self.x + int(offsetPX*self.radius*0.8)
        self.iris.y = self.y + int(offsetPY*self.radius*0.8)

        self.pupil.x = self.iris.x + int(offsetPX*self.radius*0.5)
        self.pupil.y = self.iris.y + int(offsetPY*self.radius*0.5)


    def draw(self,screen):
        if(self.isDrawn):
            self.cornia.draw(screen)
            self.redGlow.draw(screen)
            self.iris.draw(screen)
            self.pupil.draw(screen)
            self.outerFrame.draw(screen)