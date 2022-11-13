from cmu_112_graphics import *
import time # sleep()

from NightFuryClass import NightFury
from TerrainClass import Terrain

# __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)
nightFury1 = NightFury(0, 590 - 60, 30, 60, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)
# __init__(self)
terrain1 = Terrain('grey')
terrain1.addBlock(0, 500, 100, 10)

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    # terrain
    app.terrain = terrain1
    # temporary test values

    # tempx, app.groundH = app.terrain.getBaseLocation()
    # print(app.groundH)

# helper functions for timerFired
# def isLegalLocation(app):
#     blocks = app.terrain.getBlocks()
#     blocksLocations = app.terrain.getBlocksLocation()
#     nfx, nfy = app.nightFury.getLocation()
#     nfw, nfh = app.nightFury.getSize()
#     for loc in blocksLocations:
#         tx, ty = loc
#         tw, th = blocks[loc]
#         if nfx + nfw > tx and nfy + nfh > ty and nfx < tx + tw and nfy < ty+th:
#             return False
#     return True

def timerFired(app):
    backupPosition = app.nightFury.getLocation()
    # test default
    app.nightFury.isKilled()
    app.nightFury.regainPS()
    # app.nightFury.falling(app.terrain)
    # app.nightFury.doFalling()
    # test keypressed
    app.nightFury.doJump()
    app.nightFury.doDashLeft()
    app.nightFury.doDashRight()
    # print(app.terrain.isLegalLocation(app.nightFury))
    if app.terrain.isLegalLocation(app.nightFury) == True:
        pass
    else:
        app.nightFury.resetLocation(backupPosition)

# helper functions for keyPressed
def keyPressed(app, event):
    # WARNING: let the player set the keys.
    # move
    if event.key == 'Left':
        app.nightFury.resetDirection('Left')
        app.nightFury.goLeft(app.terrain)
    elif event.key == 'Right':
        app.nightFury.resetDirection('Right')
        app.nightFury.goRight(app.terrain)
    # jump
    if event.key == 'x':
        app.nightFury.jump(app.terrain)
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
# def drawBaseTerrain(app, canvas):
#     tX, tY = app.terrain.getBaseLocation()
#     tH, tW = app.terrain.getBase()[tX, tY]
#     tColor = app.terrain.getColor()
#     # this rectangle is collision box
#     canvas.create_rectangle(tX, tY, tX + tW, tY + tH, 
#                             fill = None, outline = tColor)

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
                            nfY - 7, fill = 'red')

def redrawAll(app,canvas):
    # drawBaseTerrain(app, canvas)
    drawBlocks(app, canvas)
    drawNightFury(app, canvas)
    drawPSbar(app, canvas)

runApp(width = 600, height = 600)
