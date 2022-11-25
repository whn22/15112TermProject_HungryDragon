from cmu_112_graphics import *
import time # sleep()
import copy

from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import FlyEnemy

settings = Button(10, 10, 60, 20, 'menu', 'aquamarine', 'settings', 10)

ground = Block(0, 590, 1000, 10, 'grey')
block1 = Block(0, 500, 100, 10, 'grey')
block2 = Block(150, 400, 100, 10, 'grey')
block3 = Block(350, 300, 100, 50, 'grey')
block4 = Block(300, 200, 100, 10, 'grey')
block5 = Block(500, 100, 100, 20, 'grey')
block6 = Block(650, 210, 15, 70, 'grey')
block7 = Block(700, 320, 70, 120, 'grey')
block8 = Block(700, 400, 120, 50, 'grey')
terrain = {ground, block1, block2, block3, block4, block5, block6,block7,block8}

# __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)
nightFury1 = NightFury(0, 590 - 50, 20, 50, 'blueviolet', 5, 13, 0.7, 20, 10, 
                       100, 100, 100)
print (nightFury1)

# __init__(self, x, y, w, h, color, speed, DMG, health)
flyEnemy1 = FlyEnemy(110, 220, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy2 = FlyEnemy(150, 500, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy3 = FlyEnemy(770, 200, 10, 10, 'yellow', 0.5, 20, 50)
# flyEnemy3 = FlyEnemy(170, 500, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy4 = FlyEnemy(550, 420, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy5 = FlyEnemy(380, 100, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy6 = FlyEnemy(900, 450, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy7 = FlyEnemy(600, 250, 10, 10, 'yellow', 0.5, 20, 50)
enemies = {flyEnemy1, flyEnemy2, flyEnemy3, flyEnemy4, flyEnemy5, flyEnemy6,
           flyEnemy7}

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    app.nfGoLeft = False
    app.nfGoRight = False
    # terrain
    app.terrain = terrain
    # enemies
    app.enemies = enemies
    # buttons
    app.settings = settings

# Helper functions for timerFired.
def withinCanvasRange(app, object):
    oX, oY = object.getLocation()
    oW, oH = object.getSize()
    if oX < 0 or oY < 0 or oX + oW > app.width or oY + oH > app.height:
        return False
    return True

def withinReasonableRange(app, object):
    oX, oY = object.getLocation()
    oW, oH = object.getSize()
    if oX < 50 or oY < 50 or oX + oW > app.width - 50 or \
        oY + oH > app.height - 50:
        return False
    return True

def nightFuryHorizontal(app):
    backupX = app.nightFury.x
    # keypressed
    if app.nfGoLeft == True:
        app.nightFury.direction = 'Left'
        app.nightFury.goLeft(app.terrain)
        if not withinCanvasRange(app, app.nightFury):
            app.nightFury.goRight(app.terrain)
    elif app.nfGoRight == True:
        app.nightFury.direction = 'Right'
        app.nightFury.goRight(app.terrain)
        if not withinCanvasRange(app, app.nightFury):
            app.nightFury.goLeft(app.terrain)
    app.nightFury.doLeftDash(app.terrain)
    app.nightFury.doRightDash(app.terrain)
    # check legal
    for block in app.terrain:
        if block.isObjectCollide(app.nightFury) == False \
            and withinCanvasRange(app, app.nightFury):
            pass
        else:
            # print('here')
            app.nightFury.resetDefaultMoveX()
            app.nightFury.x = backupX
            break

def nightFuryVertical(app):
    backupY = app.nightFury.y
    app.nightFury.falling(app.terrain)
    app.nightFury.doFalling()
    # keypressed
    app.nightFury.doJump(app.terrain) #()
    # check legal
    for block in app.terrain:
        if block.isObjectCollide(app.nightFury) == False \
            and withinCanvasRange(app, app.nightFury):
            pass
        else:
            # print('here')
            app.nightFury.resetDefaultMoveY()
            app.nightFury.y = backupY
            break

def nightFuryTimerFired(app):
    nightFuryHorizontal(app)
    nightFuryVertical(app)
    # test default
    app.nightFury.respawn()
    app.nightFury.refreshSlashLocation()
    app.nightFury.isKilled()
    app.nightFury.regainPS()
    app.nightFury.loseHealth(enemies)
    app.nightFury.unImmune()
    # keypressed
    app.nightFury.doLeftSlash(enemies)
    app.nightFury.doRightSlash(enemies)

def enemiesTimerFired(app):
    temp = copy.copy(app.enemies)
    for enemy in temp:
        backupPosition = enemy.getLocation()
        if enemy.isDead == True:
            app.enemies.remove(enemy)
        if type(enemy) == FlyEnemy:
            enemy.flyIdle(app.terrain)
        for block in app.terrain:
            if block.isObjectCollide(enemy) == False \
                and withinReasonableRange(app, enemy):
                pass
            else:
                # print('here')
                enemy.resetDefaultMove()
                enemy.resetLocation(backupPosition)
                break

def timerFired(app):
    nightFuryTimerFired(app)
    enemiesTimerFired(app)

# helper functions for control
def keyPressed(app, event):
    # WARNING: let the player set the keys.
    # move
    if event.key == 'Left':
        app.nfGoLeft = True
    elif event.key == 'Right':
        app.nfGoRight = True
    
    # jump
    if event.key == 'x':
        app.nightFury.jump()#app.terrain
    # dash
    if event.key == 'z':
    # if event.key == 'l':
        if app.nightFury.direction == 'Left':
            app.nightFury.dashL()
        elif app.nightFury.direction == 'Right':
            app.nightFury.dashR()
    # attack
    if event.key == 'c':
    # if event.key == 'j':
        app.nightFury.slash()

def keyReleased(app, event):
    # WARNING: let the player set the keys.
    # move
    if event.key == 'Left':
        app.nfGoLeft = False

    elif event.key == 'Right':
        app.nfGoRight = False

# helper functions for redraw All
def drawEnemies(app, canvas):
    for enemy in app.enemies:
        enemy.drawEnemy(canvas)

def drawBlocks(app, canvas):
    for block in app.terrain:
        block.drawBlock(canvas)

def redrawAll(app,canvas):
    # draw background
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'black', outline = None)
    drawBlocks(app, canvas)
    app.settings.drawButton(canvas)
    drawEnemies(app, canvas)
    app.nightFury.drawNightFury(canvas)

runApp(width = 1000, height = 600)