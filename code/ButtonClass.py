from GameObjectClass import GameObject

class Button(GameObject):
    def __init__(self, x, y, w, h, ID, color, text, textSize):
        super().__init__(x, y, w, h, color)
        self.ID = ID
        self.text = text
        self.textSize = textSize
        self.isClicked = False
        self.isMouseOn = False
    
    def checkMouseOn(self, x, y):
        if self.withinRange(x, y):
            self.isMouseOn = True
        else:
            self.isMouseOn = False

    def checkMouseClicked(self, x, y):
        if self.withinRange(x, y):
            self.isClicked = True
        else:
            self.isClicked = False

    def callFunction(self, f, p): # p should be tuple if multiple parameters
        if self.isClicked == True:
            f(p)
            self.isClicked = False
    
    def mouseClicked(self, x, y, f, p):
        self.checkMouseClicked(x, y)
        self.callFunction(f, p)

    def drawButton(self, canvas):
        x, y = self.getLocation()
        w, h = self.getSize()
        c = self.color
        if self.isMouseOn == False or self.isClicked == True:
            canvas.create_rectangle(x, y, x + w, y + h, 
                                    fill = None, outline = c)
            canvas.create_text(x + w/2, y + h/2, text = self.text,
                                    font = f'Arial {self.textSize}', 
                                    fill = c)
        elif self.isMouseOn == True:
            canvas.create_rectangle(x, y, x + w, y + h, 
                                    fill = c, outline = 'black')
            canvas.create_text(x + w/2, y + h/2, text = self.text,
                                    font = f'Arial {self.textSize}', 
                                    fill = 'black')
    
    # this hasn't been used
    def drawButtonWait(self, canvas): # for customized key settings
        x, y = self.getLocation()
        w, h = self.getSize()
        c = self.color
        canvas.create_rectangle(x, y, x + w, y + h, 
                                fill = c, outline = 'black')
        canvas.create_text(x + w/2, y + h/2, text = 'press a key',
                                font = f'Arial {self.textSize}', 
                                fill = 'black')