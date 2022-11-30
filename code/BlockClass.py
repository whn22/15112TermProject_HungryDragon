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