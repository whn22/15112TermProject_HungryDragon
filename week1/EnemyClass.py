class Enemy():
    def __init__(self, x, y, w, h, color, speed, gravity, ATK, health):
        # self.location = (x, y)
        self.x = x
        self.y = y
        # image (Collision box drawing)
        self.width = w
        self.height = h
        # properties
        self.color = color
        self.speed = speed
        self.gravity = gravity
        self.ATK = ATK
        # changable data
        self.HP = health
        # default data
        self.isDead = False
        self.direction = 'Right'
        self.fallYs = []
    
    # set methods
    def resetLocation(self, tuple):
        self.x, self.y = tuple
    
    def resetX(self, x):
        self.x = x
    
    def resetY(self, y):
        self.y = y
    
    def resetDirection(self, str): # Left or Right
        self.direction = str
    
    def resetDefaultMove(self):
        self.fallYs = []

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
    def isKilled(self):
        if self.HP <= 0:
            self.isDead = True
    
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