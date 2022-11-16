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
        self.slashAttack = [] # how long the attack will last [1, 2, 3, 4, 5, 6]
    
    def __str__(self):
        return f'NightFury:\n\
                x = {self.x}\n\
                y = {self.y}\n\
                width = {self.width}\n\
                height = {self.height}\n\
                color = {self.color}\n\
                speed = {self.speed}\n\
                jumpHeight = {self.jumpHeight}\n\
                gravity = {self.gravity}\n\
                ATK = {self.ATK}\n\
                DEF = {self.DEF}\n\
                HP = {self.HP}\n\
                MP = {self.MP}\n\
                PS = {self.PS}\n\
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
    
    def resetDefaultMove(self):
        self.jumpYs = []
        self.fallYs = []
        self.dashRXs = []
        self.dashLXs = []

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
    
    def getSlashAttack(self):
        return self.slashAttack

    # move methods
    def goLeft(self, terrain):
        self.x -= self.speed
        test = terrain.isLegalLocation(self)
        if test == True:
            pass
        else:
            tx, ty = test
            tw, th = terrain.getSpecificBlockSize(tx, ty)
            self.x = tx + tw

    def goRight(self, terrain):
        self.x += self.speed
        test = terrain.isLegalLocation(self)
        if test == True:
            pass
        else:
            tx, ty = test
            # tw, th = terrain.getSpecificBlockSize(tx, ty)
            self.x = tx - self.width

    def jump(self, terrain):
        if self.jumpYs or self.fallYs:
            return
        u = self.jumpHeight # initial speed
        # v = 0
        g = self.gravity
        y = self.y
        while u > 0:
            y -= u
            u -= g
            self.jumpYs.append(y)
            test = terrain.isLegalLocation2(self.x, y, self.width, self.height)
            if test != True:
                self.jumpYs.pop()
                tx, ty = test # location of colliding box
                tw, th = terrain.getSpecificBlockSize(tx, ty)
                self.jumpYs.append(ty + th)
                break
        # print(self.jumpYs, 'jump')

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
    # def leftSlash(self):
    #     if self.slashAttack == []:
    #         self.slashAttack = [1, 2, 3, 4, 5, 6]

    # def rightSlash(self):
    #     if self.slashAttack == []:
    #         self.slashAttack = [1, 2, 3, 4, 5, 6]

    def slash(self):
        if self.slashAttack == []:
            self.slashAttack = [1, 2, 3, 4, 5, 6]

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
        if self.jumpYs:
            jumpY = self.jumpYs.pop(0)
            self.y = jumpY
    
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
                # tx, ty = test # location of colliding box
                # self.fallYs.append(ty)
                break
        # print(self.fallYs)

    def doFalling(self):
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY

    def doLeftDash(self): # terrain
        if self.dashLXs:
            dashLX = self.dashLXs.pop(0)
            self.x = dashLX
            # test = terrain.isLegalLocation(self)
            # if test == True:
            #     pass
            # else:
            #     tx, ty = test
            #     tw, th = terrain.getSpecificBlockSize(tx, ty)
            #     self.x = tx + tw
            #     self.dashLXs = []

    def doRightDash(self): # terrain
        if self.dashRXs:
            dashRX = self.dashRXs.pop(0)
            self.x = dashRX
            # test = terrain.isLegalLocation(self)
            # if test == True:
            #     pass
            # else:
            #     tx, ty = test
            #     # tw, th = terrain.getSpecificBlockSize(tx, ty)
            #     self.x = tx - self.width
            #     self.dashRXs = []
    
    def doSlash(self):
        if self.slashAttack:
            frame = self.slashAttack.pop(0)
        # if frame == 3:
        #     nfX, nfY = self.getLocation()
        #     nfW, nfH = self.getSize()
        #     nfX += nfW/2
        #     canvas.create_polygon(nfX, nfY - 20, 
        #                             nfX - 60, nfY - 15, 
        #                             nfX - 100, nfY, 
        #                             nfX - 120, nfY + 15, 
        #                             nfX - 120, nfY + nfH - 15, 
        #                             nfX - 100, nfY + nfH, 
        #                             nfX - 60, nfY + nfH + 15, 
        #                             nfX, nfH + nfY + 20, 
        #                             fill = None, outline = 'blue')
