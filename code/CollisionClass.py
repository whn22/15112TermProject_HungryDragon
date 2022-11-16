class Collision():
    def isRectangleCollide1(rect1, rect2): # inputs two rects
        x1, y1 = rect1.getLocation()
        w1, h1 = rect1.getSize()
        x2, y2 = rect2.getLocation()
        w2, h2 = rect2.getSize()
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return (rect1, rect2)
        return False
    
    # def isPolygonCollide(rect1, rect2):
    def isRectangleCollide2(x1, y1, w1, h1, x2, y2, w2, h2): # input coordinates
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return True
        return False
    
    def isRectangleCollide3(rect1, x2, y2, w2, h2): # one kind each
        x1, y1 = rect1.getLocation()
        w1, h1 = rect1.getSize()
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return True
        return False