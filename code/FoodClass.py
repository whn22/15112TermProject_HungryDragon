from GameObjectClass import GameObject

class Food(GameObject):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    # draw function
    def drawFood(self, canvas):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        canvas.create_rectangle(x, y, x + w, y + h, 
                                fill = self.color, outline = self.color)
                            
    def drawFoodSet(allFood, canvas):
        for food in allFood:
            food.drawFood(canvas)