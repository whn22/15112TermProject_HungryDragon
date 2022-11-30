from cmu_112_graphics import *
import time # sleep()
import copy

from MenuClass import Menu
from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import Enemy, FlyEnemy, WalkEnemy
from SpritesClass import NightFurySprites

from GenerateLevel import Level

level = Level(10, 5)

def appStarted(app):
    # initialize all data
    menu = Menu('Left', 'Right', 'x', 'z')
    level.createTerrain(app)
    level.createEnemies(app)
    nfheight = 50
    startX, startY = level.enter.x, level.enter.y - nfheight
    nfSprites = NightFurySprites()
    nightFury1 = NightFury(startX, startY, 20, 50, 'white', 5, 13, 0.7, 20, 10, 
                        100, 100, 100)
    print (nightFury1)
    menuButton = Button(10, 10, 60, 20, 'menuButton', 'aquamarine', 'menu', 10)
    refreshButton = Button(80, 10, 60, 20, 'refreshButton', 'aquamarine', 'refresh', 10)
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    app.nfGoLeft = False
    app.nfGoRight = False
    # terrain
    # app.terrain = terrain
    app.level = level
    app.terrain = level.terrain
    # enemies
    app.enemies = level.enemies
    # buttons
    # app.menu = settings
    app.menuButton = menuButton
    app.refreshButton = refreshButton
    # app.menuButton = Button(10, 10, 60, 20, 
    #                     'menu', 'aquamarine', 'menu', 10)
    # menu
    app.menu = menu
    app.inputKey = None

    app.mouseX, app.mouseY = (-1, -1)
    app.menu.createMenu(app)

    #sprites
    app.nfSprites = nfSprites
    app.nfSprites.initializeAll(app)

# helper functions for timerFired
def buttonTimerFired(app):
    app.refreshButton.checkMouseOn(app.mouseX, app.mouseY)
    if app.menu.menuOn == False:
        app.menuButton.checkMouseOn(app.mouseX, app.mouseY)
    else:
        for button in app.menu.menuButtons:
            button.checkMouseOn(app.mouseX, app.mouseY)

def timerFired(app):
    app.nightFury.nightFuryTimerFired(app)
    Enemy.enemiesTimerFired(app)
    buttonTimerFired(app)
    app.level.passLevel(app.nightFury, app.enemies)
    # sprites timerFired
    app.nfSprites.nfSpritesTimer()

# helper functions for control
def mouseMoved(app, event):
    app.mouseX, app.mouseY = (event.x, event.y)

def mousePressed(app, event):
    # menu methods
    if app.menu.menuOn == False:
        app.menuButton.mouseClicked(event.x, event.y, app.menu.openMenu, app)
    else:
        for button in app.menu.menuButtons:
            button.mouseClicked(event.x, event.y, 
                                app.menu.resetKey, (app.inputKey, button))
    app.refreshButton.mouseClicked(event.x, event.y, 
                                app.level.refreshLevel, app)
    app.terrain = level.terrain

def mouseDragged(app, event):
    # player shoot methods
    app.nightFury.aiming = True # this maybe redundant
    app.nightFury.aim(event.x, event.y)

def mouseReleased(app, event):
    if app.nightFury.aiming == True: # this maybe redundant
        app.nightFury.shooting = True
        app.nightFury.shoot(event.x, event.y, app.enemies, app.terrain, app)
        app.nightFury.aiming = False

def keyPressed(app, event):
    # let the players set the keys
    app.inputKey = event.key
    if app.inputKey == 'q':
        app.menu.menuOn = False
    # move
    if event.key == app.menu.left:
        app.nfGoLeft = True
    elif event.key == app.menu.right:
        app.nfGoRight = True
    # jump
    if event.key == app.menu.jump:
        app.nightFury.jump()
    # dash
    if event.key == app.menu.dash:
        if app.nightFury.direction == 'Left':
            app.nightFury.dashL()
        elif app.nightFury.direction == 'Right':
            app.nightFury.dashR()
    # attack
    if event.key == 'c':
        app.nightFury.slash()

def keyReleased(app, event):
    # move
    if event.key == app.menu.left:
        app.nfGoLeft = False

    elif event.key == app.menu.right:
        app.nfGoRight = False

# helper functions for redraw All
def redrawAll(app,canvas):
    # draw background
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'black', outline = None)
    app.level.drawDoors(canvas)
    Block.drawBlockSet(app.terrain, canvas)
    Enemy.drawEnemySet(app.enemies, canvas)
    app.nfSprites.drawSprites(app, app.nightFury, canvas)
    # app.nightFury.drawNightFury(canvas)    # player collision box
    app.nightFury.drawAim(canvas)
    app.nightFury.drawShoot(canvas)
    app.refreshButton.drawButton(canvas)
    app.menuButton.drawButton(canvas)
    if app.level.win == True:
        app.level.drawPassLevel(app, canvas)
        return
    if app.menu.menuOn == True:
        app.menu.drawMenu(app, canvas)
    # draw sprites

runApp(width = 1000, height = 500)