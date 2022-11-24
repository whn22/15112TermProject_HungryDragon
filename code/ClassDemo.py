from cmu_112_graphics import *

class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def getBounds(self):
        (x0, y1) = (self.x, self.height/2 - self.y)
        (x1, y0) = (x0 + self.width, y1 - self.height)
        return x0, y0, x1, y1
    
    def intersectionObject(self, other):
        (ax0, ay0, ax1, ay1) = self.getBounds()
        (bx0, by0, bx1, by1) = other.getBounds()
        pass

class Button():
    def __init__(self, x, y, width, height):
        self.x0 = x
        self.y0 = y
        self.width = width
        self.height = height



