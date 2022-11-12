from cmu_112_graphics import *
import time # sleep()

from NightFuryClass import NightFury
from TerrainClass import Terrain

# __init__(self, x, y, h, w, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)
nightFury1 = NightFury(0, 600 - 30, 30, 70, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    app.nightFury = nightFury1
    # app.jumpYs = []
    # app.dashRXs = []
    # app.dashLXs = []

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
    app.nightFury.regainPS()

    if app.nightFury.jumpYs:
        doJump(app)
    if app.nightFury.dashLXs:
        doDashLeft(app)
    elif app.nightFury.dashRXs:
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
            app.nightFury.jump(600)
    # dash
    if event.key == 'z':
        # print(app.nightFury.getDirection())
        if app.nightFury.getDirection() == 'Left':
            app.nightFury.dashL()
        elif app.nightFury.getDirection() == 'Right':
            app.nightFury.dashR()
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

def drawPSbar(app, canvas):
    lenPS = app.nightFury.getPS()
    nfX, nfY = app.nightFury.getLocation()
    nfH, nfW = app.nightFury.getSize()
    canvas.create_rectangle(nfX, nfY - 10, nfX + lenPS/100 * nfW, 
                            nfY - 7, fill = 'red')

def redrawAll(app,canvas):
    drawNightFury(app, canvas)
    drawPSbar(app, canvas)

runApp(width = 600, height = 600)
