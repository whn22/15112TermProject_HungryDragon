class NightFury():
    def __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF,
                 health, magic, physicalStrength):
        # self.location = (x, y)
        self.x = x
        self.y = y
        # image (Collision box drawing)
        self.width = w
        self.height = h
        # properties
        self.color = color
        self.speed = speed
        self.jumpHeight = jumpHeight
        self.gravity = gravity
        self.ATK = ATK
        self.DEF = DEF
        # changable data
        self.HP = health
        self.MP = magic
        self.PS = physicalStrength
        # default data
        self.isDead = False
        self.direction = 'Right'
        self.eaten = []
        self.jumpYs = []
        self.fallYs = []
        self.dashRXs = []
        self.dashLXs = []
    
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

    def getMP(self):
        return self.MP

    def getPS(self):
        return self.PS
    
    # # methods with terrain (collision methods)
    # def getMyRoof(self, terrain):
    #     return terrain.getRoof(self)
    
    # def getMyFloor(self, terrain):
    #     return terrain.getFloor(self)

    # move methods
    def goLeft(self, terrain):
        self.x -= self.speed
        if terrain.isLegalLocation(self) == True:
            pass
        else:
            self.x += self.speed

    def goRight(self, terrain):
        self.x += self.speed
        # print(terrain.isLegalLocation(self))
        if terrain.isLegalLocation(self) == True:
            pass
        else:
            self.x -= self.speed

    # def jump(self, terrain):
    #     if self.jumpYs:
    #         return
    #     g = self.gravity
    #     u = self.jumpHeight # initial speed
    #     y = self.y
    #     while True:
    #         if y > terrain - self.height:
    #             self.jumpYs.pop()
    #             break
    #         y -= u
    #         if u > -self.jumpHeight:
    #             u -= g
    #         self.jumpYs.append(y)
    #     self.jumpYs.append(terrain - self.height)
    #     # print (jumpYs, 'jump')

    def jump(self, terrain):
        if self.jumpYs or self.fallYs:
            return
        u = self.jumpHeight # initial speed
        # v = 0
        g = self.gravity
        y = self.y
        while u > 0:
            test = terrain.isLegalLocation2(self.x, y, self.width, self.height)
            if test != True:
                self.fallYs.pop()
                tx, ty = test # location of colliding box
                tw, th = terrain.getSpecificBlockSize(self, tx, ty)
                self.fallYs.append(ty + th)
                break
            y -= u
            u -= g
            self.jumpYs.append(y)
        # print(self.jumpYs, 'jump')

    # def falling(self, terrain, HEIGHT):
    #     floor = terrain.getFloor(self, HEIGHT)
    #     # print(self.y + self.height, floor)
    #     # print(self.fallYs, self.y == floor - self.height)
    #     if self.fallYs or self.y == floor - self.height:
    #         return
    #     u = 0 # initial falling speed
    #     v = self.jumpHeight # Maximum falling speed
    #     g = self.gravity
    #     y = self.y
    #     while True:
    #         # print(y + self.height, floor)
    #         if y + self.height > floor:
    #             self.fallYs.pop()
    #             break
    #         y += u
    #         print(u, v)
    #         if u < v:
    #             u += g
    #         self.fallYs.append(y)
    #     if floor != HEIGHT:
    #         self.fallYs.append(floor - self.height)
    #     print(self.fallYs)

    def falling(self, terrain):
        if self.jumpYs or self.fallYs:
            return
        u = 0 # initial falling speed
        v = self.jumpHeight # Maximum falling speed
        g = self.gravity
        y = self.y
        while True:
            # print(y + self.height, floor)
            test = terrain.isLegalLocation2(self.x, y, self.width, self.height)
            if test != True:
                self.fallYs.pop()
                tx, ty = test # location of colliding box
                self.fallYs.append(ty)
                break
            y += u
            print(u, v)
            if u < v:
                u += g
            self.fallYs.append(y)
        print(self.fallYs)

    def dashL(self):
        if self.dashLXs:
            return
        if self.PS - 30 <= 0:
            return
        self.PS -= 30
        x = self.x
        for i in range(7):
            x -= self.speed
            self.dashLXs.append(x)
        for i in range(7):
            x -= self.speed/2
            self.dashLXs.append(x)
        # print (dashXs, 'dashL')

    def dashR(self):
        if self.dashRXs:
            return
        if self.PS - 30 <= 0:
            return
        self.PS -= 30
        x = self.x
        for i in range(7):
            x += self.speed
            self.dashRXs.append(x)
        for i in range(7):
            x += self.speed/2
            self.dashRXs.append(x)
        # print (dashXs, 'dashR')

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

    def doJump(self):
        # print(self.fallYs, self.jumpYs)
        # if self.fallYs == [] and self.jumpYs:
        if self.jumpYs:
            jumpY = self.jumpYs.pop(0)
            self.y = jumpY
    
    def doFalling(self):
        # print(self.fallYs, self.jumpYs)
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY

    def doDashLeft(self):
        if self.dashLXs:
            dashLX = self.dashLXs.pop(0)
            self.x = dashLX

    def doDashRight(self):
        if self.dashRXs:
            dashRX = self.dashRXs.pop(0)
            self.x = dashRX
    
    # def isLegalLocation(self, terrain):
    #     blocks = terrain.getBlocks()
    #     blocksLocations = terrain.getBlocksLocation()
    #     # nfx, nfy = self.getLocation()
    #     # nfw, nfh = self.getSize()
    #     for loc in blocksLocations:
    #         tx, ty = loc
    #         tw, th = blocks[loc]
    #         if self.x + self.width > tx and self.y + self.height > ty and \
    #             self.x < tx + tw and self.y < ty + th:
    #             self.jumpYs = []
    #             self.dashRXs = []
    #             self.dashLXs = []
    #             return False
    #     return True
