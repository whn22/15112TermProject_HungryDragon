from GameObjectClass import GameObject

class AttackBox(GameObject):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

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
        return {box1, box2, box3, box4, box5}

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
        return {box1, box2, box3, box4, box5}