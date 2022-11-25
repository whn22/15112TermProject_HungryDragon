class GameObject():
    def __init__(self, x, y, w, h, color):
        self.initLocation = x, y
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    
    # set methods
    def resetLocation(self, tuple):
        self.x, self.y = tuple
    
    def resetInitLocation(self):
        self.x, self.y = self.initLocation
    
    # get methods
    def getLocation(self):
        return self.x, self.y
    
    def getSize(self):
        return self.w, self.h
    
    # collision methods
    def isObjectCollide(self, other): # inputs two gameObjects
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        x2, y2 = other.getLocation()
        w2, h2 = other.getSize()
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return True
        return False
    
    def testCollide(self, x2, y2, w2, h2): # test temperary location (falling)
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return True
        return False
    
    def withinRange(self, x, y): # test if a point is in the object (button)
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        if x1 + w1 > x and x1 < x and y1 + h1 > y and y1 < y:
            return True
        return False