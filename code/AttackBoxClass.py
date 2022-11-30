from GameObjectClass import GameObject

class AttackBox(GameObject):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.leftSlashBox = {}
        self.rightSlashBox = {}
        self.longAtkBox = None

    def createLeftSlashBox(self):
        c = self.color
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        x += w/2
        box1 = GameObject(x - 60, y - 15, 60, h + 30, c)
        box2 = GameObject(x - 85, y - 7, 85, h + 14, c)
        box3 = GameObject(x - 100, y, 100, h, c)
        box4 = GameObject(x - 112, y + 7, 112, h - 14, c)
        box5 = GameObject(x - 120, y + 15, 120, h - 30, c)
        self.leftSlashBox = {box1, box2, box3, box4, box5}

    def createRightSlashBox(self):
        c = self.color
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        x += w/2
        box1 = GameObject(x, y - 15, 60, h + 30, c)
        box2 = GameObject(x, y - 7, 85, h + 14, c)
        box3 = GameObject(x, y, 100, h, c)
        box4 = GameObject(x, y + 7, 112, h - 14, c)
        box5 = GameObject(x, y + 15, 120, h - 30, c)
        self.rightSlashBox = {box1, box2, box3, box4, box5}

    def createLongAtkBox(self):
        # create initial location, not include the shoot path.
        c = self.color
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        x += w/2
        self.longAtkBox = GameObject(x, y + h * 0.3, 10, 10, c) # not very good data

    # draw methods
    def drawLeftSlash(self, canvas):
        leftSlash = self.leftSlashBox
        # print(leftSlash)
        for box in leftSlash:
            x, y = box.getLocation()
            w, h = box.getSize()
            canvas.create_rectangle(x, y, x + w, y + h, fill = None, 
                                    outline = self.color)

    def drawRightSlash(self, canvas):
        rightSlash = self.rightSlashBox
        # print(rightSlash)
        for box in rightSlash:
            x, y = box.getLocation()
            w, h = box.getSize()
            canvas.create_rectangle(x, y, x + w, y + h, fill = None, 
                                    outline = self.color)
                
    def drawLongAtkBox(self, canvas):
        x, y = self.longAtkBox.getLocation()
        w, h = self.longAtkBox.getSize()
        canvas.create_rectangle(x, y, x + w, y + h, fill = None, 
                                outline = self.color)