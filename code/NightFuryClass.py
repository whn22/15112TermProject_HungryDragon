from GameObjectClass import GameObject
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
        self.maxHP = health
        self.HP = health
        self.maxMP = magic
        self.MP = magic
        self.PS = physicalStrength
        # default data
        self.immune = list(range(1, 15))
        self.isDead = False
        self.direction = 'Right'
        self.eaten = []
        self.jumpYs = []
        self.lenJ = 0
        self.fallYs = []
        self.lenF = 0
        self.dashLXs = []
        self.dashRXs = []
        # attack collision box
        self.slashFramesL = [] # how long the attack will last: 15
        self.slashFramesR = [] 
        self.slashFrame = -1
        self.shootFrames = []
        self.aiming = False
        self.shooting = False
        self.shot = None
        self.refS = -1
        self.refE = -1
        self.attackBox = AttackBox(self.x, self.y, self.w, self.h, 'aquamarine')

        # self.leftSlashBox = attackBox.createLeftSlashBox()
        # self.rightSlashBox = attackBox.createRightSlashBox()
    
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

################################################################################
    # reset methods
    def resetDefaultMoveX(self):
        self.dashRXs = []
        self.dashLXs = []

    def resetDefaultMoveY(self):
        self.jumpYs = []
        self.fallYs = []

    def resetImmune(self):
        self.immune = list(range(1, 15))

    # control methods
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

    def jump(self):
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
        self.lenJ = len(self.jumpYs)

    def dashL(self):
        if self.dashLXs:
            return
        if self.PS - 30 <= 0:
            return
        self.PS -= 30
        x = self.x
        for i in range(6):
            x -= self.speed * 5
            self.dashLXs.append(x)
        for i in range(6):
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
        for i in range(6):
            x += self.speed * 5
            self.dashRXs.append(x)
        for i in range(6):
            x += self.speed * 2
            self.dashRXs.append(x)
        # print (dashXs, 'dashR')

    def slash(self):
        if self.slashFramesL == [] and self.direction == 'Left':
            self.slashFramesL = list(range(0, 15))
        if self.slashFramesR == [] and self.direction == 'Right':
            self.slashFramesR = list(range(0, 15))

    # mousePressed, True, mouseReleased, False
    def aim(self, x, y):
        # px, py = -1, -1 # the coordinate of path (px, py)
        # print(x, y)
        if self.aiming == True and self.shootFrames == []:
            # find shoot path: y = ax + b
            sx, sy = self.attackBox.longAtkBox.getLocation()
            dx = x - sx
            dy = y - sy
            if dx != 0:
                a = dy/dx # gradient
                b = y - a*x # intersection
            else:
                return
            # sx, sy means shoot x, shoot y
            self.refS = (sx, sy)
            if dx < 0:
                self.refE = (-sx * 500, -(a * sx * 500 + b))
            else:
                self.refE = (sx * 500, a * sx * 500 + b)
    
    def shoot(self, x, y, enemies, terrain, app):
        if self.shooting == True and self.shootFrames == []:
            sx, sy = self.attackBox.longAtkBox.getLocation()
            dx = x - sx
            dy = y - sy
            a = dy/dx # gradient
            b = y - a*x # intersection
            # sx, sy means shoot x, shoot y
            while True:
                if dx < 0:
                    sx -= 30
                    sy = a * sx + b
                    self.shootFrames.append((sx, sy))
                    # print(sx, sy)
                else:
                    sx += 30
                    sy = a * sx + b
                    self.shootFrames.append((sx, sy))
                    # print(sx, sy)
                for enemy in enemies:
                    if enemy.testCollide(sx, sy, 10, 10) or \
                        GameObject.pointWithinCanvasRange(sx, sy, app) == False:
                        # self.shootFrames.pop()
                        # print(self.shootFrames)
                        return
                for block in terrain:
                    if block.testCollide(sx, sy, 10, 10) or \
                        GameObject.pointWithinCanvasRange(sx, sy, app) == False:
                        self.shootFrames.pop()
                        # print(self.shootFrames)
                        return

    def drawAim(self, canvas):
        # print(self.refS, self.refE, '!!!!!!!!!!')
        # if self.refS == None or self.refE == None:
        if self.aiming == False:
            return
        x1, y1 = self.refS
        x2, y2 = self.refE
        canvas.create_line(x1, y1, x2, y2, fill = 'turquoise')
    
    def getShot(self, enemies, app):
        if self.shootFrames:
            frame = self.shootFrames.pop(0)
            if self.shootFrames == []:
                self.shooting = False
            x, y = frame
            self.shot = GameObject(x, y, 10, 10, 'aquamarine')
            for enemy in enemies:
                if self.shot.isObjectCollide(enemy):
                    enemy.beAttacked(self, app)
                    return

    def drawShoot(self, canvas):
        # print(self.shootFrames)
        if self.shot and self.shooting == True:
            self.shot.drawGameObject(canvas)
        else:
            self.shot = None

    def accumulateFarAttack(self):
        pass

################################################################################
    # timerfired methods
    def isKilled(self):
        if self.HP <= 0:
            self.isDead = True
            self.HP = 0

    def regainPS(self): 
        # max PS is 100, regain 0.5 per period
        if self.PS < 100:
            self.PS += 0.5

    def doJump(self, terrain): # apply jumping coordinates, test legal
        if self.jumpYs:
            jumpY = self.jumpYs.pop(0)
            self.y = jumpY
            for block in terrain:
                if self.isObjectCollide(block):
                    self.jumpYs = []
                    tx, ty = block.getLocation()
                    tw, th = block.getSize()
                    self.jumpYs.append(ty + th)
                    break
    
    def falling(self, terrain): # generate falling coordinates if suspend.
        if len(self.jumpYs) > 1 or self.fallYs:
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
                if block.testCollide(self.x, y, self.w, self.h):
                    self.fallYs.pop()
                    tx, ty = block.getLocation()
                    self.fallYs.append(ty - self.h)
                    self.lenF = len(self.fallYs)
                    return

    def doFalling(self): # if there are falling coordinates, apply them.
        if self.jumpYs == [] and self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY

    def doLeftDash(self, terrain): # apply dash coordinates, test legal
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

    def doRightDash(self, terrain):
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
        self.attackBox = AttackBox(self.x, self.y, self.w, self.h, 'aquamarine')
        self.attackBox.createLeftSlashBox()
        self.attackBox.createRightSlashBox()
        self.attackBox.createLongAtkBox()
    
    def doLeftSlash(self, app):
        if self.slashFramesL and self.direction == 'Left':
            self.slashFrame = self.slashFramesL.pop(0)
            if self.slashFrame == 2:
                for enemy in app.enemies:
                    for box in self.attackBox.leftSlashBox:
                        if box.isObjectCollide(enemy):
                            enemy.beAttacked(self, app)
                            break

    def doRightSlash(self, app):
        if self.slashFramesR and self.direction == 'Right':
            self.slashFrame = self.slashFramesR.pop(0)
            if self.slashFrame == 2:
                for enemy in app.enemies:
                    for box in self.attackBox.rightSlashBox:
                        if box.isObjectCollide(enemy):
                            enemy.beAttacked(self, app)
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
                    return
    
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
    
    # timerFired app
    def nightFuryHorizontal(self, app):
        backupX = self.x
        # keypressed
        if app.nfGoLeft == True:
            self.direction = 'Left'
            self.goLeft(app.terrain)
            if not self.withinCanvasRange(app):
                self.goRight(app.terrain)
        elif app.nfGoRight == True:
            self.direction = 'Right'
            self.goRight(app.terrain)
            if not self.withinCanvasRange(app):
                self.goLeft(app.terrain)
        self.doLeftDash(app.terrain)
        self.doRightDash(app.terrain)
        # check legal
        for block in app.terrain:
            if block.isObjectCollide(self) == False \
                and self.withinCanvasRange(app):
                pass
            else:
                # print('here')
                self.resetDefaultMoveX()
                self.x = backupX
                break

    def nightFuryVertical(self, app):
        backupY = self.y
        self.falling(app.terrain)
        self.doFalling()
        # keypressed
        self.doJump(app.terrain) #()
        # check legal
        for block in app.terrain:
            if block.isObjectCollide(self) == False \
                and self.withinCanvasRange(app):
                pass
            else:
                # print('here')
                self.resetDefaultMoveY()
                self.y = backupY
                break

    def nightFuryTimerFired(self, app):
        self.nightFuryHorizontal(app)
        self.nightFuryVertical(app)
        # test default
        self.respawn()
        self.refreshSlashLocation()
        self.isKilled()
        self.regainPS()
        self.loseHealth(app.enemies)
        self.unImmune()
        # keypressed
        self.doLeftSlash(app)
        self.doRightSlash(app)
        self.getShot(app.enemies, app)

################################################################################
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
                                nfY - 9, fill = 'cyan', outline = 'cyan')

    def drawHPbar(self, canvas):
        hp = self.HP
        nfX, nfY = self.getLocation()
        canvas.create_rectangle(nfX - 5, nfY - 20, nfX + hp/100 * 30 - 5, 
                                nfY - 19, fill = 'turquoise', 
                                outline = 'turquoise')

    def drawNightFury(self, canvas):
        self.drawSelf(canvas)
        self.drawPSbar(canvas)
        self.drawHPbar(canvas)
        if self.slashFramesL:
            self.attackBox.drawLeftSlash(canvas)
        if self.slashFramesR:
            self.attackBox.drawRightSlash(canvas)
        # self.drawAim(canvas)
        # self.drawShoot(canvas)