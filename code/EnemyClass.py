import random
from GameObjectClass import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, w, h, color, speed, DMG, health):
        super().__init__(x, y, w, h, color)
        # properties
        self.speed = speed
        self.DMG = DMG
        # changable data
        self.HP = health
        # default data
        self.isDead = False
        self.direction = 'Right'

    def __repr__(self):
        return f'Enemy:\n\
                x = {self.x}\n\
                y = {self.y}\n\
                width = {self.w}\n\
                height = {self.h}\n\
                color = {self.color}\n\
                speed = {self.speed}\n\
                ATK = {self.DMG}\n\
                HP = {self.HP}\n\
                isDead = {self.isDead}\n\
                direction = {self.direction}\n'
    
    # set methods
    def resetDirection(self, str): # Left or Right
        self.direction = str
    
    def changeDirection(self):
        if self.direction == 'Right':
            self.direction = 'Left'
        elif self.direction == 'Left':
            self.direction = 'Right'

    # get methods
    def getDirection(self):
        return self.direction

    def getHP(self):
        return self.HP
    
    # health methods:
    def beAttacked(self, player):
        if self.isDead == False:
            self.HP -= player.ATK
            if self.HP <= 0:
                self.isDead = True
                self.HP = 0
    
    # draw methods:
    def drawEnemy(self, canvas):
        if self.isDead == True:
            return
        x, y = self.getLocation()
        w, h = self.getSize()
        c = self.color
        hp = self.HP
        # this rectangle is collision box
        canvas.create_rectangle(x, y, x + w, y + h, 
                                fill = None, outline = c)
        # draw HP bar above head
        canvas.create_rectangle(x - 5, y - 10, x + hp/50 * 20 - 5, y - 9, 
                                fill = 'lime', outline = 'lime')

class FlyEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, DMG, health):
        super().__init__(x, y, w, h, color, speed, DMG, health)
        self.idlePath = []

    def resetDefaultMove(self):
        self.idlePath = []
    
    def createIdlePath(self):
        chooseX = random.choice([self.speed, -self.speed])
        chooseY = random.choice([self.speed, -self.speed])
        for i in range(30):
            self.idlePath.append((chooseX, chooseY))

    def flyIdle(self, terrain):
        if self.idlePath == []:
            self.createIdlePath()
        dx, dy = self.idlePath.pop(0)
        self.x += dx
        self.y += dy
        for block in terrain:
            if self.isObjectCollide(block) == False:
                pass
            else:
                self.idlePath = []
                break

class WalkEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, gravity, DMG, health):
        super().__init__(self, x, y, w, h, color, speed, DMG, health)
        # properties
        self.gravity = gravity
        # default data
        self.fallYs = []

    def resetDefaultMove(self):
        self.fallYs = []

    # def falling(self, terrain):
    #     if self.jumpYs or self.fallYs:
    #         return
    #     u = 1 # initial falling speed
    #     v = self.jumpHeight # Maximum falling speed
    #     g = self.gravity
    #     y = self.y
    #     while True:
    #         y += u
    #         if u < v:
    #             u += g
    #         self.fallYs.append(y)
    #         test = terrain.isLegalLocation2(self.x, y, self.w, self.h)
    #         if test != True:
    #             self.fallYs.pop()
    #             break

    def doFalling(self):
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY
        
    # def walkIdle(self, terrain):
    #     if self.fallYs == [] and terrain.isLegalLocation(self) == True:
    #         if self.direction == 'Right':
    #             self.x += self.speed
    #         elif self.direction == 'Left':
    #             self.x -= self.speed
    #     elif self.fallYs:
    #         self.fallYs = []
    #         self.changeDirection()

    # draw function