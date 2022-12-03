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
        self.hold = False

    def findDiff(self, app):
        self.dx, self.dy = self.x - app.nightFury.x,\
                           self.y - app.nightFury.y

    # if key pressed "Space"
    def move(self, app):
        backup = self.x, self.y
        # self.findDiff(app)
        # print(self.dx, self.dy)
        self.resetLocation((app.nightFury.x + self.dx, 
                            app.nightFury.y + self.dy))
        for block in app.terrain:
            if type(block) == Platform and self.isObjectCollide(block):
                self.x, self.y = backup
                self.hold = False
        if self.withinCanvasRange(app) == False:
            self.x, self.y = backup
    
class Platform(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)