from GameObjectClass import GameObject

class Block(GameObject):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    # draw function
    def drawBlock(self, canvas):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        canvas.create_rectangle(x, y, x + w, y + h, 
                                fill = None, outline = self.color)
                            
    def drawBlockSet(terrain, canvas):
        for block in terrain:
            block.drawBlock(canvas)
        
class MovBlock(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.dx = -1
        self.dy = -1

    def findDiff(self, app):
        self.dx, self.dy = self.x - app.nightFury.x, self.y - app.nightFury.y

    # if key pressed "Space"
    def move(self, app):
        if self.isObjectTouch(app.nightFury):
            backup = self.x, self.y
            self.resetLocation(app.nightFury.x + self.dx, 
                                app.nightFury.y + self.dy)
            if self.withinCanvasRange(app) == False:
                self.x, self.y = backup