from cmu_112_graphics import *
import time # sleep()
import copy
import math
import pygame

from MenuClass import Menu
from DisplayClass import Display
from ButtonClass import Button
from BlockClass import Block, MovBlock
from NightFuryClass import NightFury
from EnemyClass import Enemy, FlyEnemy, WalkEnemy
from SpritesClass import NightFurySprites, EnemySprites
from GenerateLevel import Level
from FoodClass import Food
from SoundClass import Sound, BackGroundSound

# Sound effects from HOLLOW KNIGHT (team cherry)
# https://www.dropbox.com/sh/faqjj2ekftj1nb4/AADu5kD3mmbAJ-G-J84AmzBra?dl=0
# background music: Philter - Dance Of The Fireflies
# player sprites are hand-drawn by myself (reference is HOLLOW KNIGHT)

pygame.mixer.init()
slashSound = Sound("sword_1.wav")
dashSound = Sound("hero_dash.wav")
bgSound = BackGroundSound("Philter - Dance Of The Fireflies.mp3")

def normal(app):
    level = Level(7, 3, 2, 5)
    level.generateLevel(app)
    startX, startY = level.enter.getLocation()
    nightFury1 = NightFury(startX, startY, 20, 50, 'white', 5, 13, 0.7, 20, 10, 
                        100, 100, 100)
    return level, nightFury1

def appStarted(app):
    # initialize
    menu = Menu('Left', 'Right', 'x', 'z', 'c', 'Space')
    level, nightFury1 = normal(app)
    menuButton = Button(app.width - 70, 10, 60, 20, 
                        'menuButton', 'aquamarine', 'menu', 10)
    refreshButton = Button(app.width - 140, 10, 60, 20, 
                        'refreshButton', 'aquamarine', 'refresh', 10)
    # level
    app.level = level
    app.terrain = level.terrain
    app.enemies = level.enemies
    # nightFury (player)
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
    # WARNING: if implement bg, the animation will be extremely slow
    # background 
    # bg = 'Pixel Cities.gif'
    # app.background = app.loadImage(bg)
    # app.background = app.scaleImage(app.background, 1.5)
    # sprites
    nfSprites = NightFurySprites()
    enemySprites = EnemySprites()
    app.nfSprites = nfSprites
    app.nfSprites.initializeAll(app)
    app.enemySprites = enemySprites
    app.enemySprites.initializeIdle(app)
    # sound
    app.slashSound = slashSound
    app.dashSound = dashSound
    app.bgMusic = bgSound
    # app.runSound = Sound("hero_run.wav")
    # app.jumpSound = Sound("hero_jump.wav")

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
    # level timerFired
    app.level.winGame(app.nightFury)
    if app.level.win == True:
        return
    app.level.passLevel(app.nightFury)
    if app.level.levelPass == True:
        app.level.refreshLevel(app)
        app.terrain = app.level.terrain
        app.enemies = app.level.enemies
        app.nightFury.resetLocation(app.level.enter.getLocation())
        app.level.levelPass = False
    # nightFury timerFired
    app.nightFury.nightFuryTimerFired(app)
    # enemies timerFired
    app.enemies = app.level.enemies
    Enemy.enemiesTimerFired(app)
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
                                app.menu.doFunction,(app.inputKey, button, app))
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
    if event.key == 'p':
        if app.bgMusic.isPlaying(): app.bgMusic.stop()
        else: app.bgMusic.start(loops=-1)
    if (app.nightFury.isDead == True or app.level.win == True)\
                                                        and event.key == 'r':
        app.level.reStart(app)
        app.terrain = app.level.terrain
        app.nightFury.respawn()
    app.inputKey = event.key
    if app.inputKey == 'q':
        app.menu.menuOn = False
    # move
    if event.key == app.menu.left:
        # print('left', app.nightFury.nfGoLeft)
        # if app.nightFury.nfGoLeft == False:
        #     app.runSound.start(loops=-1)
        app.nightFury.nfGoLeft = True
    elif event.key == app.menu.right:
        # print('right', app.nightFury.nfGoRight)
        # if app.nightFury.nfGoRight == False:
        #     app.runSound.start(loops=-1)
        app.nightFury.nfGoRight = True
    # jump
    if event.key == app.menu.jump:
        app.nightFury.jump()
    # dash
    if event.key == app.menu.dash:
        if app.nightFury.PS >= 30:
            app.dashSound.play()
        if app.nightFury.direction == 'Left':
            app.nightFury.dashL()
        elif app.nightFury.direction == 'Right':
            app.nightFury.dashR()
    # attack
    if event.key == app.menu.slash:
        if app.nightFury.slashFramesL == [] and app.nightFury.slashFramesR ==[]:
            app.slashSound.play()
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
        # print('left release')
        # if app.runSound.isPlaying(): app.runSound.stop()
        app.nightFury.nfGoLeft = False
    elif event.key == app.menu.right:
        # print('right release')
        # if app.runSound.isPlaying(): app.runSound.stop()
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
    # canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.background))
    app.level.drawDoors(canvas)
    Block.drawBlockSet(app.terrain, canvas)
    Enemy.drawEnemySet(app.enemies, canvas)
    Food.drawFoodSet(app.level.food, canvas)
    Display.display(app, canvas)
    app.nightFury.drawAim(canvas)
    app.nightFury.drawShoot(canvas)
    app.refreshButton.drawButton(canvas)
    app.menuButton.drawButton(canvas)
    app.nfSprites.drawSprites(app, app.nightFury, canvas)
    for enemy in app.enemies:
        app.enemySprites.drawIdle(enemy, canvas)
    # app.nightFury.drawNightFury(canvas)  # player collision box
    if app.level.win == True:
        app.level.drawWin(app, canvas)
        # time.sleep(1)
    if app.menu.menuOn == True:
        app.menu.drawMenu(app, canvas)
    # draw sprites

runApp(width = 1000, height = 500)