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

# ground = Block(0, 590, 1000, 10, 'grey')
# block1 = Block(0, 500, 100, 10, 'grey')
# block2 = Block(150, 400, 100, 10, 'grey')
# block3 = Block(350, 300, 100, 50, 'grey')
# block4 = Block(300, 200, 100, 10, 'grey')
# block5 = Block(500, 100, 100, 20, 'grey')
# block6 = Block(650, 210, 15, 70, 'grey')
# block7 = Block(700, 320, 70, 120, 'grey')
# block8 = Block(700, 400, 120, 50, 'grey')
# terrain = {ground, block1, block2, block3, block4, block5, block6,block7,block8}




# __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF, 
# health, magic, physicalStrength)


# # __init__(self, x, y, w, h, color, speed, DMG, knockBack, health):
# # flyEnemy1 = FlyEnemy(110, 220, 10, 10, 'yellow', 0.5, 20, 20, 50)
# walkEnemy1 = WalkEnemy(50, 480, 20, 20, 'yellow', 0.5, 20, 20, 50)
# flyEnemy2 = FlyEnemy(150, 500, 10, 10, 'yellow', 0.5, 20, 20, 50)
# flyEnemy3 = FlyEnemy(770, 200, 10, 10, 'yellow', 0.5, 20, 20, 50)
# # flyEnemy3 = FlyEnemy(170, 500, 10, 10, 'yellow', 0.5, 20, 50)
# flyEnemy4 = FlyEnemy(550, 420, 10, 10, 'yellow', 0.5, 20, 20, 50)
# flyEnemy5 = FlyEnemy(380, 100, 10, 10, 'yellow', 0.5, 20, 20, 50)
# flyEnemy6 = FlyEnemy(900, 450, 10, 10, 'yellow', 0.5, 20, 20, 50)
# flyEnemy7 = FlyEnemy(600, 250, 10, 10, 'yellow', 0.5, 20, 20, 50)
# enemies = {walkEnemy1, flyEnemy2, flyEnemy3, flyEnemy4, flyEnemy5, flyEnemy6,
#            flyEnemy7}

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
    # player shoot methods
    app.nightFury.aiming = True

def mouseReleased(app, event):
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
    app.refreshButton.drawButton(canvas)
    app.menuButton.drawButton(canvas)
    if app.level.win == True:
        app.level.drawPassLevel(app, canvas)
        return
    if app.menu.menuOn == True:
        app.menu.drawMenu(app, canvas)
    # draw sprites

runApp(width = 1000, height = 500)