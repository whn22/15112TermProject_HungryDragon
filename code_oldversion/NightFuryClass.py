from GameObjectClass import GameObject
from CollisionClass import Collision
from AttackBoxClass import AttackBox
import time # sleep()

class NightFury(GameObject):
    def __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF,
                 health, magic, physicalStrength):
        super().__init__(x, y, w, h, color)
        self.initLocation = (x, y)
        # properties
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
        self.immune = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.isDead = False
        self.direction = 'Right'
        self.eaten = []
        self.jumpYs = []
        self.fallYs = []
        self.dashLXs = []
        self.dashRXs = []
        # attack collision box
        self.slashFrames = [] # how long the attack will last [1, 2, 3, 4, 5, 6]
        attackBox = AttackBox(self.x, self.y, self.w, self.h)
        self.leftSlashBox = attackBox.createLeftSlashBox()
        self.rightSlashBox = attackBox.createRightSlashBox()
    
    def __str__(self):
        return f'NightFury:\n\
                x = {self.x}\n\
                y = {self.y}\n\
                width = {self.w}\n\
                height = {self.h}\n\
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

    # reset methods
    def resetDefaultMoveX(self):
        self.dashRXs = []
        self.dashLXs = []

    def resetDefaultMoveY(self):
        self.jumpYs = []
        self.fallYs = []

    def resetImmune(self):
        self.immune = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def goLeft(self, terrain):
        self.x -= self.speed
        for block in terrain:
            test = self.isObjectCollide(block)
            if test == False:
                pass
            else:
                tx, ty = block.getLocation()
                tw, th = block.getSize()
                self.x = tx + tw

    def goRight(self, terrain):
        self.x += self.speed
        for block in terrain:
            test = self.isObjectCollide(block)
            if test == False:
                pass
            else:
                tx, ty = block.getLocation()
                self.x = tx - self.w

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
            for block in terrain:
                test = self.isObjectCollide(block)
                if test == True:
                    self.jumpYs.pop()
                    tx, ty = block.getLocation()
                    tw, th = block.getSize()
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
        for i in range(5):
            x -= self.speed * 5
            self.dashLXs.append(x)
        for i in range(5):
            x -= self.speed * 2
            self.dashLXs.append(x)
        # print (dashXs, 'dashL')

    def dashR(self):
        if self.dashRXs:
            return
        if self.PS - 30 <= 0:
            return
        self.PS -= 30
        x = self.x
        for i in range(5):
            x += self.speed * 5
            self.dashRXs.append(x)
        for i in range(5):
            x += self.speed * 2
            self.dashRXs.append(x)
        # print (dashXs, 'dashR')

    def slash(self):
        if self.slashFrames == []:
            if self.direction == 'Left':
                self.slashFrames = [1, 2, 3, 4, 5, 6]
            if self.direction == 'Right':
                self.slashFrames = [7, 8, 9, 10, 11, 12]

    def quickFarAttack(self):
        pass

    def accumulateFarAttack(self):
        pass

    # timerfired methods
    def isKilled(self):
        if self.HP <= 0:
            self.isDead = True
            self.HP = 0

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
            for block in terrain:
                test = self.isObjectCollide(block)
                if test == True:
                    self.fallYs.pop()
                    tx, ty = block.getLocation()
                    self.fallYs.append(ty - self.h)
                    break
        # print(self.fallYs)

    def doFalling(self):
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY

    def doLeftDash(self, terrain): # terrain
        if self.dashLXs:
            dashLX = self.dashLXs.pop(0)
            self.x = dashLX
            for block in terrain:
                test = self.isObjectCollide(block)
                if test == True:
                    self.dashLXs = []
                    tx, ty = block.getLocation()
                    tw, th = block.getSize()
                    self.x = tx + tw

    def doRightDash(self, terrain): # terrain
        if self.dashRXs:
            dashRX = self.dashRXs.pop(0)
            self.x = dashRX
            for block in terrain:
                test = self.isObjectCollide(block)
                if test == True:
                    self.dashRXs = []
                    tx, ty = block.getLocation()
                    self.x = tx - self.w

    def refreshSlashLocation(self):
        self.leftSlashBox = AttackBox.createLeftSlashBox(\
                            self.x, self.y, self.w, self.h)
        self.rightSlashBox = AttackBox.createRightSlashBox(\
                            self.x, self.y, self.w, self.h)
    
    def doLeftSlash(self, enemies):
        if self.slashFrames and self.slashFrames[0] < 7:
            frame = self.slashFrames.pop(0)
            if frame == 3:
                for enemy in enemies:
                    for box in self.leftSlashBox:
                        test = self.isObjectCollide(box)
                        if test:
                            enemy.beAttacked(self)
                            break

    def doRightSlash(self, enemies):
        if self.slashFrames and self.slashFrames[0] > 6:
            frame = self.slashFrames.pop(0)
            if frame == 9:
                for enemy in enemies:
                    for box in self.rightSlashBox:
                        test = self.isObjectCollide(box)
                        if test:
                            enemy.beAttacked(self)
                            break
    
    def loseHealth(self, enemies):
        if self.immune == []:
            for enemy in enemies:
                if self.isObjectCollide(enemy):
                    self.HP -= enemy.DMG
                    self.resetImmune()
                    if self.HP < 0:
                        self.isDead = True
                        self.HP = 0
                    break
    
    def unImmune(self):
        if self.immune:
            self.immune.pop()
        
    def respawn(self):
        if self.isDead == True:
            self.HP = 100
            self.isDead = False
            self.resetInitLocation()
            self.resetDefaultMoveX()
            self.resetDefaultMoveY()
    
    # draw function
    def drawSelf(self, canvas):
        nfX, nfY = self.getLocation()
        nfW, nfH = self.getSize()
        nfColor = self.color
        # this rectangle is collision box
        canvas.create_rectangle(nfX, nfY, nfX + nfW, nfY + nfH, 
                                fill = None, outline = nfColor)

    def drawPSbar(self, canvas):
        ps = self.PS
        nfX, nfY = self.getLocation()
        canvas.create_rectangle(nfX - 5, nfY - 10, nfX + ps/100 * 30 - 5, 
                                nfY - 7, fill = 'orange')

    def drawHPbar(self, canvas):
        hp = self.HP
        nfX, nfY = self.getLocation()
        canvas.create_rectangle(nfX - 5, nfY - 20, nfX + hp/100 * 30 - 5, 
                                nfY - 17, fill = 'red')

    def drawLeftSlash(self, canvas):
        leftSlash = self.leftSlashBox
        for rect in leftSlash:
            x, y = rect
            w, h = leftSlash[rect]
            canvas.create_rectangle(x, y, x + w, y + h, fill = None, 
                                    outline = 'blue')

    def drawRightSlash(self, canvas):
        rightSlash = self.rightSlashBox
        for rect in rightSlash:
            x, y = rect
            w, h = rightSlash[rect]
            canvas.create_rectangle(x, y, x + w, y + h, fill = None, 
                                    outline = 'blue')

    # def drawRespawn(self, canvas):
    #     for i in range(3):
    #         time.sleep(1)
    #         print(1)
    #         canvas.create_text(self.w/2, self.h/2, 
    #                             text = f'You die. Respawn in {3 - i} s', 
    #                             font = 'Arial 18 bold', fill = 'black')

    def drawNightFury(self, canvas):
        # if self.isDead:
        #     drawRespawn(self, canvas)
        # else:
        self.drawSelf(canvas)
        self.drawPSbar(canvas)
        self.drawHPbar(canvas)
        if self.slashFrames:
            if self.direction == 'Left':
                self.drawLeftSlash(canvas)
            elif self.direction == 'Right':
                self.drawRightSlash(canvas)