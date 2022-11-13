from cmu_112_graphics import *
import time # sleep()

from NightFuryClass import NightFury
from TerrainClass import Terrain

# nightFury1 = NightFury(0, 590 - 60, 30, 60, 'black', 16, 12, 0.6, 20, 10, 
#                        100, 100, 100)
nightFury1 = NightFury(100, 100, 30, 60, 'black', 16, 12, 0.6, 20, 10, 
                       100, 100, 100)

def appStarted(app):
    app.nightFury = nightFury1

# Helper functions for timerFired.
def timerFired(app):
    pass

# helper functions for keyPressed
def keyPressed(app, event):
    pass

# helper functions for redraw All
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
                            fill = None, outline = 'black')

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
                            fill = None, outline = 'black')

# def testDraw(app, canvas):
#     canvas.create_polygon(200, 200 - 20, 200 + 50, 200, 
#                         200 + 50, 200 + 30, 200, 200 + 30 + 20, 
#                         fill = None, outline = 'black')

def redrawAll(app,canvas):
    drawLeftSlash(app, canvas)
    drawRightSlash(app, canvas)

runApp(width = 600, height = 600)
