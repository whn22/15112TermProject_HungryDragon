from GameObjectClass import GameObject
from NightFuryClass import NightFury
from EnemyClass import Enemy
from AttackBoxClass import AttackBox

class Boss(NightFury, Enemy):
    def __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, health):
        GameObject.__init__(self, x, y, w, h, color)
        # properties
        self.speed = speed
        self.jumpHeight = jumpHeight
        self.gravity = gravity
        self.ATK = ATK
        self.maxHP = health
        # changable data
        self.HP = health
        # default data
        self.isDead = False
        self.direction = 'Right'
        self.jumpYs = []
        self.lenJ = 0
        self.fallYs = []
        self.lenF = 0
        self.dashLXs = []
        self.dashRXs = []
        # attack collision box
        self.bossGoLeft = False
        self.bossGoRight = False
        self.slashFramesL = [] # how long the attack will last: 15
        self.slashFramesR = [] 
        self.slashFrame = -1
        self.shootFrames = []
        self.aiming = False
        self.shooting = False
        self.shot = None
        self.refS = (-1, -1) # this is aiming reference line Start and End point
        self.refE = (-1, -1)
        self.attackBox = AttackBox(self.x, self.y, self.w, self.h, 'red')

    def decideDash(self, player):
        pass

    def dashL(self):
        if self.dashLXs:
            return
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
        x = self.x
        for i in range(6):
            x += self.speed * 5
            self.dashRXs.append(x)
        for i in range(6):
            x += self.speed * 2
            self.dashRXs.append(x)
        # print (dashXs, 'dashR')

    # def doLeftDash(self, terrain): # apply dash coordinates, test legal
    #     if self.dashLXs:
    #         dashLX = self.dashLXs.pop(0)
    #         self.x = dashLX
    #         for block in terrain:
    #             test = self.isObjectCollide(block)
    #             if test == True:
    #                 self.dashLXs = []
    #                 tx, ty = block.getLocation()
    #                 tw, th = block.getSize()
    #                 self.x = tx + tw

    # def doRightDash(self, terrain):
    #     if self.dashRXs:
    #         dashRX = self.dashRXs.pop(0)
    #         self.x = dashRX
    #         for block in terrain:
    #             test = self.isObjectCollide(block)
    #             if test == True:
    #                 self.dashRXs = []
    #                 tx, ty = block.getLocation()
    #                 self.x = tx - self.w

    # timerFired app
    def bossHorizontal(self, app):
        backupX = self.x
        # keypressed
        if self.bossGoLeft == True:
            self.direction = 'Left'
            self.goLeft(app.terrain)
            if not self.withinCanvasRange(app):
                self.goRight(app.terrain)
        elif self.bossGoRight == True:
            self.direction = 'Right'
            self.goRight(app.terrain)
            if not self.withinCanvasRange(app):
                self.goLeft(app.terrain)
        if self.decideDash(app.nightFury) == True:
            if self.direction == 'Left':
                self.doLeftDash(app.terrain)
            if self.direction == 'Right':
                self.doRightDash(app.terrain)
        # check legal
        for block in app.terrain:
            # if type(block) == MovBlock and self.hold == True and block.hold == True:
            #     return
            if block.isObjectCollide(self) == False \
                and self.withinCanvasRange(app):
                pass
            else:
                # print('here')
                self.resetDefaultMoveX()
                self.x = backupX
                break

    def bossVertical(self, app):
        backupY = self.y
        self.falling(app.terrain)
        self.doFalling()
        # keypressed
        self.doJump(app.terrain) #()
        # check legal
        for block in app.terrain:
            # if type(block) == MovBlock and self.hold == True and block.hold == True:
            #     return
            if block.isObjectCollide(self) == False \
                and self.withinCanvasRange(app):
                pass
            else:
                # print('here')
                self.resetDefaultMoveY()
                self.y = backupY
                break

    def bossAI(self, app):
        # move
        # slash
        # shoot
        pass

    def bossTimerFired(self, app):
        self.bossHorizontal(app)
        self.bossVertical(app)
        # test default
        self.refreshSlashLocation()
        # self.loseHealth(app.enemies)
        self.isKilled()
        self.eat(app)
        # triggered
        self.doLeftSlash(app)
        self.doRightSlash(app)
        self.getShot(app.enemies, app)

# __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, health)
b = Boss(100, 100, 50, 50, 'red', 3, 13, 0.7, 20, 500)
print(b.bossGoLeft)