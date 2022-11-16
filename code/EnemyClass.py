import random

class Enemy():
    def __init__(self, x, y, w, h, color, speed, DMG, health):
        # self.location = (x, y)
        self.x = x
        self.y = y
        # image (Collision box drawing)
        self.width = w
        self.height = h
        # properties
        self.color = color
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
                width = {self.width}\n\
                height = {self.height}\n\
                color = {self.color}\n\
                speed = {self.speed}\n\
                ATK = {self.DMG}\n\
                HP = {self.HP}\n\
                isDead = {self.isDead}\n\
                direction = {self.direction}\n'
    
    # set methods
    def resetLocation(self, tuple):
        self.x, self.y = tuple
    
    def resetX(self, x):
        self.x = x
    
    def resetY(self, y):
        self.y = y
    
    def resetDirection(self, str): # Left or Right
        self.direction = str

    # get methods
    def getDirection(self):
        return self.direction

    def getLocation(self):
        return self.x, self.y
    
    def getSize(self):
        return self.width, self.height
    
    def getColor(self):
        return self.color
    
    def getSpeed(self):
        return self.speed
    
    def getIsDead(self):
        return self.isDead

    def getHP(self):
        return self.HP

    # move methods
    def goLeft(self, terrain):
        self.x -= self.speed
        if terrain.isLegalLocation(self) == True:
            pass
        else:
            self.x += self.speed

    def goRight(self, terrain):
        self.x += self.speed
        if terrain.isLegalLocation(self) == True:
            pass
        else:
            self.x -= self.speed

    # timerfired methods
    # def isKilled(self):
    #     if self.HP <= 0:
    #         self.isDead = True
    #     self.HP = 0
    
    # health methods:
    def beAttacked(self, player):
        if self.isDead == False:
            self.HP -= player.getATK()
            if self.HP <= 0:
                self.isDead = True
                self.HP = 0

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
        if terrain.isLegalLocation(self) == True:
            pass
        else:
            self.idlePath = []

class WalkEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, gravity, DMG, health):
        super().__init__(self, x, y, w, h, color, speed, DMG, health)
        # properties
        self.gravity = gravity
        # default data
        self.fallYs = []

    def resetDefaultMove(self):
        self.fallYs = []

    def falling(self, terrain):
        if self.jumpYs or self.fallYs:
            return
        u = 1 # initial falling speed
        v = self.jumpHeight # Maximum falling speed
        g = self.gravity
        y = self.y
        while True:
            y += u
            if u < v:
                u += g
            self.fallYs.append(y)
            test = terrain.isLegalLocation2(self.x, y, self.width, self.height)
            if test != True:
                self.fallYs.pop()
                break

    def doFalling(self):
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY
        
    def walkIdle(self, terrain):
        if self.fallYs == [] and terrain.isLegalLocation(self) == True:
            self.x += self.speed
        elif self.fallYs:
            pass