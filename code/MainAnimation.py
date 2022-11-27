from cmu_112_graphics import *
import time # sleep()
import copy

from ControlSetClass import ControlSet
from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import Enemy, FlyEnemy, WalkEnemy

from GenerateLevel import Level1

settings = Button(10, 10, 60, 20, 'menu', 'aquamarine', 'settings', 10)
refresh = Button(80, 10, 60, 20, 'refresh', 'aquamarine', 'refresh', 10)

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
nightFury1 = NightFury(10, 590 - 50, 20, 50, 'white', 5, 13, 0.7, 20, 10, 
                       100, 100, 100)
print (nightFury1)

# __init__(self, x, y, w, h, color, speed, DMG, knockBack, health):
# flyEnemy1 = FlyEnemy(110, 220, 10, 10, 'yellow', 0.5, 20, 20, 50)
walkEnemy1 = WalkEnemy(50, 480, 20, 20, 'yellow', 0.5, 20, 20, 50)
flyEnemy2 = FlyEnemy(150, 500, 10, 10, 'yellow', 0.5, 20, 20, 50)
flyEnemy3 = FlyEnemy(770, 200, 10, 10, 'yellow', 0.5, 20, 20, 50)
# flyEnemy3 = FlyEnemy(170, 500, 10, 10, 'yellow', 0.5, 20, 50)
flyEnemy4 = FlyEnemy(550, 420, 10, 10, 'yellow', 0.5, 20, 20, 50)
flyEnemy5 = FlyEnemy(380, 100, 10, 10, 'yellow', 0.5, 20, 20, 50)
flyEnemy6 = FlyEnemy(900, 450, 10, 10, 'yellow', 0.5, 20, 20, 50)
flyEnemy7 = FlyEnemy(600, 250, 10, 10, 'yellow', 0.5, 20, 20, 50)
enemies = {walkEnemy1, flyEnemy2, flyEnemy3, flyEnemy4, flyEnemy5, flyEnemy6,
           flyEnemy7}

controlSettings = ControlSet('Left', 'Right', 'x', 'z')

# 3 * 4
level1 = Level1(3, 5)

def appStarted(app):
    # timerDelay
    app.timerDelay = 10
    # nightFury
    app.nightFury = nightFury1
    app.nfGoLeft = False
    app.nfGoRight = False
    # terrain
    # app.terrain = terrain
    level1.createTerrain(app)
    app.level1 = level1
    app.terrain = level1.terrain
    # enemies
    app.enemies = enemies
    # buttons
    app.settings = settings
    app.refresh = refresh
    # menu
    app.settings = controlSettings
    app.inputKey = None
    menu = Button(10, 10, 60, 20, 
                        'menu', 'aquamarine', 'menu', 10)
    app.menu = menu
    app.mouseX, app.mouseY = (-1, -1)
    leftB = Button(app.width/2 - 300, app.height/10 * 3, 200, 40, 
                        'left', 'aquamarine', 'set left', 20)
    rightB = Button(app.width/2 - 300, app.height/10 * 4, 200, 40, 
                        'right', 'aquamarine', 'set right', 20)
    jumpB = Button(app.width/2 - 300, app.height/10 * 5, 200, 40, 
                        'jump', 'aquamarine', 'set jump', 20)
    dashB = Button(app.width/2 - 300, app.height/10 * 6, 200, 40, 
                        'dash', 'aquamarine', 'set dash', 20)
    app.menuButtons = {leftB, rightB, jumpB, dashB}
    app.menuOn = False

def enemiesTimerFired(app):
    temp = copy.copy(app.enemies)
    for enemy in temp:
        # backupPosition = enemy.getLocation()
        if enemy.isDead == True:
            app.enemies.remove(enemy)
        if type(enemy) == FlyEnemy:
            enemy.flyIdle(app)
        if type(enemy) == WalkEnemy:
            enemy.walkIdle(app)

def buttonTimerFired(app):
    app.refresh.checkMouseOn(app.mouseX, app.mouseY)
    if app.menuOn == False:
        app.menu.checkMouseOn(app.mouseX, app.mouseY)
    else:
        for button in app.menuButtons:
            button.checkMouseOn(app.mouseX, app.mouseY)

def timerFired(app):
    app.nightFury.nightFuryTimerFired(app)
    enemiesTimerFired(app)
    buttonTimerFired(app)
    app.level1.passLevel(app.nightFury, app.enemies)

# helper functions for controlzz
def openMenu(app):
    app.menuOn = True

def mouseMoved(app, event):
    app.mouseX, app.mouseY = (event.x, event.y)

def mousePressed(app, event):
    if app.menuOn == False:
        app.menu.mouseClicked(event.x, event.y, openMenu, app)
    else:
        for button in app.menuButtons:
            button.mouseClicked(event.x, event.y, 
                                app.settings.resetKey, (app.inputKey, button))
    app.refresh.mouseClicked(event.x, event.y, app.level1.refresh, app)
    app.terrain = level1.terrain

def keyPressed(app, event):
    # let the players set the keys
    app.inputKey = event.key
    if app.inputKey == 'q':
        app.menuOn = False
    # move
    # if event.key == 'Left':
    if event.key == app.settings.left:
        app.nfGoLeft = True
    # elif event.key == 'Right':
    elif event.key == app.settings.right:
        app.nfGoRight = True
    
    # jump
    # if event.key == 'x':
    if event.key == app.settings.jump:
        app.nightFury.jump()#app.terrain
    # dash
    # if event.key == 'z':
    if event.key == app.settings.dash:
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
    if event.key == app.settings.left:
        app.nfGoLeft = False

    elif event.key == app.settings.right:
        app.nfGoRight = False

# helper functions for redraw All
def redrawAll(app,canvas):
    # draw background
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'black', outline = None)
    Block.drawBlockSet(app.terrain, canvas)
    Enemy.drawEnemySet(app.enemies, canvas)
    app.nightFury.drawNightFury(canvas)
    app.refresh.drawButton(canvas)
    app.menu.drawButton(canvas)
    if app.level1.win == True:
        app.level1.drawPassLevel(app, canvas)
    if app.menuOn == True:
        app.settings.drawMenu(app, canvas)

runApp(width = 1000, height = 600)