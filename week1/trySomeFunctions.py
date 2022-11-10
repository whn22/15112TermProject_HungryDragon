from cmu_112_graphics import *
import time # sleep()

class NightFury:
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
        self.eaten = None
        self.HP = health
        self.MP = magic
        self.PP = physicalStrength
    
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
    
    # state methods
    def isKilled(self):
        if self.HP <= 0:
            self.isDead = True

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

# __init__(self, x, y, h, w, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)
nightFury1 = NightFury(0, 600 - 30, 30, 70, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # # nightFury image
    # app.nfX, app.nfY = nightFury.getLocation()
    # app.nfH, app.nfW = nightFury.getSize()
    # app.nfColor = nightFury.getColor()
    # # night Fury properties
    # app.nfSpeed = nightFury.getSpeed()
    # # night Fury status
    # app.nfIsDead = nightFury.getIsDead()
    app.nightFury = nightFury1
    app.jumpYs = []
    app.dashRXs = []
    app.dashLXs = []

# helper functions for timerFired
def doJump(app):
    jumpY = app.jumpYs.pop(0)
    app.nightFury.resetY(jumpY)

def doDashLeft(app):
    dashLX = app.dashLXs.pop(0)
    app.nightFury.resetX(dashLX)

def doDashRight(app):
    dashRX = app.dashRXs.pop(0)
    app.nightFury.resetX(dashRX)

def timerFired(app):
    app.nightFury.isKilled()

    if app.jumpYs:
        doJump(app)
    if app.dashLXs:
        doDashLeft(app)
    elif app.dashRXs:
        doDashRight(app)

# helper functions for keyPressed
def keyPressed(app, event):
    # WARNING: let the player set the keys.
    # move
    if event.key == 'Left':
        app.nightFury.goLeft()
        app.nightFury.resetDirection('Left')
    elif event.key == 'Right':
        app.nightFury.goRight()
        app.nightFury.resetDirection('Right')
    # jump
    if event.key == 'x':
        if app.jumpYs == []:
            app.jumpYs = app.nightFury.jump(600)
    # dash
    if event.key == 'z':
        # print(app.nightFury.getDirection())
        if app.nightFury.getDirection() == 'Left':
            app.dashLXs = app.nightFury.dashL()
        elif app.nightFury.getDirection() == 'Right':
            app.dashRXs = app.nightFury.dashR()
    # attack
    if event.key == 'c':
        if app.nightFury.getDirection() == 'Left':
            app.nightFury.leftSlash()
        elif app.nightFury.getDirection() == 'Right':
            app.nightFury.rightSlash()

# helper functions for redraw All
def drawNightFury(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfH, nfW = app.nightFury.getSize()
    nfColor = app.nightFury.getColor()
    # this rectangle is collision box
    canvas.create_rectangle(nfX, nfY, nfX + nfW, nfY + nfH, fill = nfColor)

def redrawAll(app,canvas):
    drawNightFury(app, canvas)

runApp(width = 600, height = 600)
