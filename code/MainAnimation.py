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
nightFury1 = NightFury(0, 590 - 60, 30, 60, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)
print (nightFury1)

# __init__(self, x, y, w, h, color, speed, DMG, health)
flyEnemy1 = FlyEnemy(110, 110, 10, 10, 'red', 0.5, 20, 50)

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    # terrain
    app.terrain = terrain1
    # enemies
    app.flyEnemy = flyEnemy1

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
    app.nightFury.isKilled()
    app.nightFury.regainPS()
    app.nightFury.falling(app.terrain)
    app.nightFury.doFalling()
    # test keypressed
    app.nightFury.doJump()
    app.nightFury.doLeftDash()# app.terrain
    app.nightFury.doRightDash()# app.terrain
    app.nightFury.doSlash()
    # test legal, avoid error
    if app.terrain.isLegalLocation(app.nightFury) == True \
        and withinCanvasRange(app, app.nightFury):
        pass
    else:
        # print('here')
        app.nightFury.resetDefaultMove()
        app.nightFury.resetLocation(backupPosition)

def enemiesTimerFired(app):
    backupPosition = app.flyEnemy.getLocation()
    app.flyEnemy.flyIdle(app.terrain)
    if app.terrain.isLegalLocation(app.flyEnemy) == True \
        and withinReasonableRange(app, app.flyEnemy):
        pass
    else:
        # print('here')
        app.flyEnemy.resetDefaultMove()
        app.flyEnemy.resetLocation(backupPosition)

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
    lenPS = app.nightFury.getPS()
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    canvas.create_rectangle(nfX, nfY - 10, nfX + lenPS/100 * nfW, 
                            nfY - 7, fill = 'orange')

def drawLeftSlash(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    nfX += nfW/2
    canvas.create_polygon(nfX, nfY - 20, 
                            nfX - 60, nfY - 15, 
                            nfX - 100, nfY, 
                            nfX - 120, nfY + 15, 
                            nfX - 120, nfY + nfH - 15, 
                            nfX - 100, nfY + nfH, 
                            nfX - 60, nfY + nfH + 15, 
                            nfX, nfH + nfY + 20, 
                            fill = None, outline = 'blue')

def drawRightSlash(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    nfX += nfW/2
    canvas.create_polygon(nfX, nfY - 20, 
                            nfX + 60, nfY - 15, 
                            nfX + 100, nfY, 
                            nfX + 120, nfY + 15, 
                            nfX + 120, nfY + nfH - 15, 
                            nfX + 100, nfY + nfH, 
                            nfX + 60, nfY + nfH + 15, 
                            nfX, nfH + nfY + 20, 
                            fill = None, outline = 'blue')
    
def drawFlyEnemy(app, canvas):
    fX, fY = app.flyEnemy.getLocation()
    fW, fH = app.flyEnemy.getSize()
    fColor = app.flyEnemy.getColor()
    # this rectangle is collision box
    canvas.create_rectangle(fX, fY, fX + fW, fY + fH, 
                            fill = None, outline = fColor)

def drawPlayer(app, canvas):
    drawNightFury(app, canvas)
    drawPSbar(app, canvas)
    if app.nightFury.getSlashAttack():
        if app.nightFury.getDirection() == 'Left':
            drawLeftSlash(app, canvas)
        elif app.nightFury.getDirection() == 'Right':
            drawRightSlash(app, canvas)

def drawEnemies(app, canvas):
    drawFlyEnemy(app, canvas)

def redrawAll(app,canvas):
    drawBlocks(app, canvas)
    drawPlayer(app, canvas)
    drawEnemies(app, canvas)

runApp(width = 1000, height = 600)