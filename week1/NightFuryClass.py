class NightFury():
    def __init__(self, x, y, h, w, color, speed, jumpHeight, gravity, ATK, DEF,
                 health, magic, physicalStrength):
        # image (Collision box drawing)
        self.x = x
        self.y = y
        # self.location = (x, y)
        self.height = h
        self.width = w
        self.color = color
        # properties
        self.speed = speed
        self.jumpHeight = jumpHeight
        self.gravity = gravity
        self.ATK = ATK
        self.DEF = DEF
        # status
        self.isDead = False
        self.direction = 'Right'
        self.eaten = []
        self.HP = health
        self.MP = magic
        self.PS = physicalStrength
    
    # set methods
    def resetLocation(self, x, y):
        self.x, self.y = x, y
    
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
        return self.height, self.width
    
    def getColor(self):
        return self.color
    
    def getSpeed(self):
        return self.speed
    
    def getIsDead(self):
        return self.isDead

    def getHP(self):
        return self.HP

    def getMP(self):
        return self.MP

    def getPS(self):
        return self.PS

    # move methods
    def goLeft(self):
        self.x -= self.speed

    def goRight(self):
        self.x += self.speed

    def jump(self, ground):
        g = self.gravity # acceleration/gravity
        u = self.jumpHeight # initial speed
        y = self.y
        jumpYs = []
        jumping = True
        while jumping:
            if y > ground - self.height:
                jumping = False
                break
            y -= u
            u -= g
            jumpYs.append(y)
        jumpYs.append(ground - self.height)
        # print (jumpYs, 'jump')
        return jumpYs

    def dashL(self):
        if self.PS - 30 <= 0:
            return []
        self.PS -= 30
        dashXs = []
        x = self.x
        for i in range(7):
            x -= self.speed
            dashXs.append(x)
        for i in range(7):
            x -= self.speed/2
            dashXs.append(x)
        # print (dashXs, 'dashL')
        return dashXs

    def dashR(self):
        if self.PS - 30 <= 0:
            return []
        self.PS -= 30
        dashXs = []
        x = self.x
        for i in range(7):
            x += self.speed
            dashXs.append(x)
        for i in range(7):
            x += self.speed/2
            dashXs.append(x)
        # print (dashXs, 'dashR')
        return dashXs

    # attack methods
    def leftSlash(self):
        pass

    def rightSlash(self):
        pass

    def quickFarAttack(self):
        pass

    def accumulateFarAttack(self):
        pass

    # timerfired methods
    def isKilled(self):
        if self.HP <= 0:
            self.isDead = True

    def regainPS(self): 
        # max PS is 100, regain 0.5 per period
        if self.PS < 100:
            self.PS += 0.5
