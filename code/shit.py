from cmu_112_graphics import *

from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import Enemy, FlyEnemy, WalkEnemy

from GenerateLevel import Level

level1 = Level(5, 5, 2)

def appStarted(app):
    app.timerDelay = 10
    app.level1 = level1
    app.level1.generateBossLevel(app)
    startX, startY = app.level1.enter.getLocation()
    nightFury1 = NightFury(startX, startY, 20, 50, 'white', 5, 13, 0.7, 20, 10, 
                    100, 100, 100)
    app.nightFury = nightFury1
    pass

# Helper functions for timerFired.
def timerFired(app):
    app.enemies = app.level1.enemies
    app.terrain = app.level1.terrain
    Enemy.enemiesTimerFired(app)

# helper functions for keyPressed
def keyPressed(app, event):
    pass

# helper functions for redraw All
def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'black', outline = None)
    Block.drawBlockSet(app.level1.terrain, canvas)
    Enemy.drawEnemySet(app.level1.enemies, canvas)
    app.level1.drawEnter(canvas)
    app.nightFury.drawNightFury(canvas)  # player collision box
    pass

runApp(width = 1000, height = 500)