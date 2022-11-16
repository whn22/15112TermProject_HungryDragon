from cmu_112_graphics import *
import time # sleep()

from TerrainClass import Terrain
from NightFuryClass import NightFury
from EnemyClass import FlyEnemy

# __init__(self)
terrain1 = Terrain('grey')
# create a temporary map
terrain1.addBlock(0, 500, 100, 10)
terrain1.addBlock(150, 400, 100, 10)
terrain1.addBlock(350, 300, 100, 50)
terrain1.addBlock(300, 200, 100, 10)
terrain1.addBlock(500, 100, 100, 20)
terrain1.addBlock(650, 210, 15, 70)
terrain1.addBlock(700, 320, 70, 120)
terrain1.addBlock(700, 400, 120, 50)

# __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)
nightFury1 = NightFury(0, 590 - 50, 20, 50, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)
print (nightFury1)

# __init__(self, x, y, w, h, color, speed, DMG, health)
flyEnemy1 = FlyEnemy(110, 110, 10, 10, 'red', 0.5, 20, 50)
flyEnemy2 = FlyEnemy(150, 500, 10, 10, 'red', 0.5, 20, 50)
flyEnemy3 = FlyEnemy(770, 200, 10, 10, 'red', 0.5, 20, 50)
flyEnemy4 = FlyEnemy(550, 420, 10, 10, 'red', 0.5, 20, 50)
flyEnemy5 = FlyEnemy(380, 100, 10, 10, 'red', 0.5, 20, 50)
enemies = [flyEnemy1, flyEnemy2, flyEnemy3, flyEnemy4, flyEnemy5]

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    # terrain
    app.terrain = terrain1
    # enemies
    app.enemies = enemies

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

def nightFuryTimerFired(app):
    backupPosition = app.nightFury.getLocation()
    # test default
    app.nightFury.refreshSlashLocation()
    app.nightFury.isKilled()
    app.nightFury.regainPS()
    app.nightFury.falling(app.terrain)
    app.nightFury.doFalling()
    # test keypressed
    app.nightFury.doJump()
    app.nightFury.doLeftDash()# app.terrain
    app.nightFury.doRightDash()# app.terrain
    app.nightFury.doLeftSlash(enemies)
    app.nightFury.doRightSlash(enemies)
    # test legal, avoid error
    if app.terrain.isLegalLocation(app.nightFury) == True \
        and withinCanvasRange(app, app.nightFury):
        pass
    else:
        # print('here')
        app.nightFury.resetDefaultMove()
        app.nightFury.resetLocation(backupPosition)

def enemiesTimerFired(app):
    for enemy in app.enemies:
        backupPosition = enemy.getLocation()
        if enemy.getIsDead() == True:
            app.enemies.remove(enemy)
        if type(enemy) == FlyEnemy:
            enemy.flyIdle(app.terrain)
        if app.terrain.isLegalLocation(enemy) == True \
            and withinReasonableRange(app, enemy):
            pass
        else:
            # print('here')
            enemy.resetDefaultMove()
            enemy.resetLocation(backupPosition)

def timerFired(app):
    nightFuryTimerFired(app)
    enemiesTimerFired(app)

# helper functions for keyPressed
def keyPressed(app, event):
    # WARNING: let the player set the keys.
    # move
    if event.key == 'Left':
        app.nightFury.resetDirection('Left')
        app.nightFury.goLeft(app.terrain)
        if not withinCanvasRange(app, app.nightFury):
            app.nightFury.goRight(app.terrain)
    elif event.key == 'Right':
        app.nightFury.resetDirection('Right')
        app.nightFury.goRight(app.terrain)
        if not withinCanvasRange(app, app.nightFury):
            app.nightFury.goLeft(app.terrain)
    # jump
    if event.key == 'x':
        app.nightFury.jump(app.terrain)
    # dash
    if event.key == 'z':
        if app.nightFury.getDirection() == 'Left':
            app.nightFury.dashL()
        elif app.nightFury.getDirection() == 'Right':
            app.nightFury.dashR()
    # attack
    if event.key == 'c':
        app.nightFury.slash()

# helper functions for redraw All
def drawBlocks(app, canvas):
    blocks = app.terrain.getBlocks()
    blocksLocations = app.terrain.getBlocksLocation()
    tColor = app.terrain.getColor()
    for loc in blocksLocations:
        x, y = loc
        w, h = blocks[loc]
        canvas.create_rectangle(x, y, x + w, y + h, 
                            fill = None, outline = tColor)

def drawNightFury(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    nfColor = app.nightFury.getColor()
    # this rectangle is collision box
    canvas.create_rectangle(nfX, nfY, nfX + nfW, nfY + nfH, 
                            fill = None, outline = nfColor)

def drawPSbar(app, canvas):
    ps = app.nightFury.getPS()
    nfX, nfY = app.nightFury.getLocation()
    canvas.create_rectangle(nfX - 5, nfY - 10, nfX + ps/100 * 25, 
                            nfY - 7, fill = 'orange')

def drawLeftSlash(app, canvas):
    leftSlash = app.nightFury.getLeftSlashBox()
    for rect in leftSlash:
        x, y = rect
        w, h = leftSlash[rect]
        canvas.create_rectangle(x, y, x + w, y + h, fill = None, outline = 'blue')

def drawRightSlash(app, canvas):
    rightSlash = app.nightFury.getRightSlashBox()
    for rect in rightSlash:
        x, y = rect
        w, h = rightSlash[rect]
        canvas.create_rectangle(x, y, x + w, y + h, fill = None, outline = 'blue')

def drawEnemies(app, canvas):
    for enemy in app.enemies:
        if enemy.getIsDead() == True:
            continue
        fX, fY = enemy.getLocation()
        fW, fH = enemy.getSize()
        fColor = enemy.getColor()
        hp = enemy.getHP()
        # this rectangle is collision box
        canvas.create_rectangle(fX, fY, fX + fW, fY + fH, 
                                fill = None, outline = fColor)
        canvas.create_rectangle(fX - 5, fY - 10, fX + hp/50 * 20 - 5, fY - 7, 
                                fill = 'red')

def drawPlayer(app, canvas):
    drawNightFury(app, canvas)
    drawPSbar(app, canvas)
    if app.nightFury.getSlashFrames():
        if app.nightFury.getDirection() == 'Left':
            drawLeftSlash(app, canvas)
        elif app.nightFury.getDirection() == 'Right':
            drawRightSlash(app, canvas)

# def drawEnemies(app, canvas):
#     drawFlyEnemy(app, canvas)

def redrawAll(app,canvas):
    drawBlocks(app, canvas)
    drawPlayer(app, canvas)
    drawEnemies(app, canvas)

runApp(width = 1000, height = 600)