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

    # this function hasn't been used
    def isObjectTouch(self, other): # inputs two gameObjects
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        x2, y2 = other.getLocation()
        w2, h2 = other.getSize()
        if x1 + w1 > x2 and x1 < x2 + w2 and (y1 + h1 == y2 or y1 == y2 + h2):
            return True
        elif y1 + h1 > y2 and y1 < y2 + h2 and (x1 + w1 == x2 or x1 == x2 + w2):
            return True
        return False
    
    def isSetCollide(self, set): # a set contains gameObjects
        for item in set:
            if self.isObjectCollide(item):
                return item
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
    
    def testExceedEdge(self, other): # check if object is on the edge of another
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        x2, y2 = other.getLocation()
        w2, h2 = other.getSize()
        if x1 + w1 >= x2 + w2 and y1 + h1 == y2 and \
            x1 >= x2 and x1 <= x2 + w2:
            # print('reach right edge')
            return True
        elif x1 <= x2 and y1 + h1 == y2 and \
            x1 + w1 >= x2 and x1 + w1 <= x2 + w2:
            # print('reach left edge')
            return True
        else:
            return False

    # this function hasn't been used
    def findDistance(self, other): # find the distance between two centers
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        x2, y2 = other.getLocation()
        w2, h2 = other.getSize()
        cx1, cy1 = (x1 + w1)/2, (y1 + h1)/2
        cx2, cy2 = (x2 + w2)/2, (y2 + h2)/2
        return (((cx1 - cx2)**2 + (cy1 - cy2)**2)**0.5)

    # app methods
    def withinCanvasRange(self, app):
        oX, oY = self.getLocation()
        oW, oH = self.getSize()
        if oX < 0 or oY < 0 or oX + oW > app.width or oY + oH > app.height:
            return False
        return True

    def pointWithinCanvasRange(x, y, app):
        if x < 0 or y < 0 or x > app.width or y > app.height:
            return False
        return True

    def withinReasonableRange(self, app):
        oX, oY = self.getLocation()
        oW, oH = self.getSize()
        if oX < 50 or oY < 50 or oX + oW > app.width - 50 or \
            oY + oH > app.height - 50:
            return False
        return True

    def drawGameObject(self, canvas):
        x1, y1 = self.x, self.y
        w1, h1 = self.w, self.h
        canvas.create_rectangle(x1, y1, x1 + w1, y1 + h1, fill = self.color)