from cmu_112_graphics import *
import time # sleep()
import copy
import math

from MenuClass import Menu
from DisplayClass import Display
from ButtonClass import Button
from BlockClass import Block, MovBlock
from NightFuryClass import NightFury
from EnemyClass import Enemy, FlyEnemy, WalkEnemy
from SpritesClass import NightFurySprites
from GenerateLevel import Level
from FoodClass import Food

def appStarted(app):
    # initialize
    level = Level(7, 3, 1)
    menu = Menu('Left', 'Right', 'x', 'z', 'c', 'Space')
    level.generateLevel(app)
    menuButton = Button(app.width - 70, 10, 60, 20, 
                        'menuButton', 'aquamarine', 'menu', 10)
    refreshButton = Button(app.width - 140, 10, 60, 20, 
                        'refreshButton', 'aquamarine', 'refresh', 10)
    # level
    app.level = level
    app.terrain = level.terrain
    app.enemies = level.enemies
    startX, startY = app.level.enter.getLocation()
    # nightFury
    nfSprites = NightFurySprites()
    # def __init__(self, x, y, w, h, color, speed, jumpHeight, gravity, ATK, DEF,
    #           health, magic, physicalStrength):
    nightFury1 = NightFury(startX, startY, 20, 50, 'white', 5, 13, 0.7, 20, 10, 
                        100, 100, 100)
    # print (nightFury1)
    app.nightFury = nightFury1
    # timerDelay
    app.timerDelay = 10
    # buttons
    app.menuButton = menuButton
    app.refreshButton = refreshButton
    # menu
    app.menu = menu
    app.inputKey = None
    app.mouseX, app.mouseY = (-1, -1)
    app.menu.createMenu(app)
    #sprites
    app.nfSprites = nfSprites
    app.nfSprites.initializeAll(app)

# helper functions for timerFired
def timerFired(app):
    # level timerFired
    if app.menu.menuOn == True:
        for button in app.menu.menuButtons:
            button.checkMouseOn(app.mouseX, app.mouseY)
        return
    # button timerFired
    app.menuButton.checkMouseOn(app.mouseX, app.mouseY)
    app.refreshButton.checkMouseOn(app.mouseX, app.mouseY)
    if app.level.levelPass == True:
        app.level.generateLevel(app)
        app.terrain = app.level.terrain
        app.enemies = app.level.enemies
        app.nightFury.resetLocation(app.level.enter.getLocation())
        app.level.levelPass = False
    app.level.passLevel(app.nightFury, app.enemies)
    # nightFury timerFired
    app.nightFury.nightFuryTimerFired(app)
    # enemies timerFired
    app.enemies = app.level.enemies
    Enemy.enemiesTimerFired(app)
    # sprites timerFired
    app.nfSprites.nfSpritesTimer()
    # hold
    # for block in app.terrain:
    #     if type(block) == MovBlock:
    #         # print(app.nightFury.hold, block.hold)
    #         if app.nightFury.hold == True and block.hold == True:
    #         # and block.isObjectTouch(app.nightFury):
    #             block.move(app)

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
    app.terrain = app.level.terrain

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
    if app.nightFury.isDead == True and event.key == 'r':
        app.level.reStart(app)
        app.nightFury.respawn()
    app.inputKey = event.key
    if app.inputKey == 'q':
        app.menu.menuOn = False
    # move
    if event.key == app.menu.left:
        app.nightFury.nfGoLeft = True
    elif event.key == app.menu.right:
        app.nightFury.nfGoRight = True
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
    if event.key == app.menu.slash:
        app.nightFury.slash()
    
    # move blocks
    if event.key == app.menu.hold:
        for block in app.terrain:
            if type(block) == MovBlock and block.isObjectTouch(app.nightFury):
                if app.nightFury.hold == False:
                    block.hold = True
                    block.findDiff(app)
                app.nightFury.hold = True
                # block.move(app)

def keyReleased(app, event):
    # move
    if event.key == app.menu.left:
        app.nightFury.nfGoLeft = False
    elif event.key == app.menu.right:
        app.nightFury.nfGoRight = False

    if event.key == app.menu.hold:
        app.nightFury.hold = False
        for block in app.terrain:
            if type(block) == MovBlock:
                block.hold = False

# helper functions for redraw All
def redrawAll(app,canvas):
    if app.nightFury.isDead == True:
        NightFury.drawDead(canvas, app)
        return
    # draw background
    canvas.create_rectangle(0, 0, app.width, app.height, 
                            fill = 'black', outline = None)
    app.level.drawDoors(canvas)
    Block.drawBlockSet(app.terrain, canvas)
    Enemy.drawEnemySet(app.enemies, canvas)
    Food.drawFoodSet(app.level.food, canvas)
    Display.display(app, canvas)
    app.nfSprites.drawSprites(app, app.nightFury, canvas)
    # app.nightFury.drawNightFury(canvas)  # player collision box
    app.nightFury.drawAim(canvas)
    app.nightFury.drawShoot(canvas)
    app.refreshButton.drawButton(canvas)
    app.menuButton.drawButton(canvas)
    if app.level.win == True:
        app.level.drawWin(app, canvas)
        # time.sleep(1)
        return
    if app.menu.menuOn == True:
        app.menu.drawMenu(app, canvas)
    # draw sprites

runApp(width = 1000, height = 500)