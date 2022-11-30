import random
from MenuClass import Menu
from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import FlyEnemy, WalkEnemy
from NightFuryClass import NightFury

class Level():
    def __init__(self, blockNum, enemyNum):
        # set number
        self.backupNum = blockNum, enemyNum
        self.blockNum = blockNum
        self.enemyNum = enemyNum
        # default terrain settings
        self.base = set()
        self.blocks = set()
        self.terrain = set()
        self.enter = None # changable
        self.exit = None
        self.enemies = set()
        # pass level
        self.win = False
    
    # general methods
    def refreshLevel(self, app):
        self.initAll()
        self.createTerrain(app)

    def initAll(self):
        self.blockNum, self.enemyNum = self.backupNum
        self.blocks = set()
        self.terrain = set()
        # self.enemies = set()

    def passLevel(self, player, enemies):
        # print(len(enemies), player.isObjectCollide(self.exit))
        if enemies == set() and player.isObjectCollide(self.exit):
            self.win = True

    # create terrain
    def createEnter(self, app):
        if self.enter == None:
            self.enter = Block(20, app.height - 15, 30, 15, 'aquamarine')
        else:
            # eg.end on celling, regenerate on botton.
            # same location (width = width, height flipped, vice versa)
            if self.exit == None:
                self.createExit(app)
            self.enter = Block(self.exit.x, app.height - 10, 30, 10, 'aquamarine')
    
    def createExit(self, app):
        if self.enter == None:
            self.createEnter(app)
        self.exit = Block(random.randint(20, app.width - 20 - 30), 0, 30, 15, 'aquamarine')
        platform = Block(self.exit.x - 10, 100, 50, 20, 'grey')
        self.blocks.add(platform)

    def createBase(self, app):
        color = 'grey' # WARNING: hard code color
        ground = Block(0, app.height - 10, app.width, 10, color)
        leftWall = Block(0, 0, 10, app.height, color)
        rightWall = Block(app.width - 10, 0, 10, app.height, color)
        celling = Block(0, 0, app.width, 10, color)
        self.base.add(ground)
        self.base.add(leftWall)
        self.base.add(rightWall)
        self.base.add(celling)

    def createBlocks(self, app):
        color = 'grey' # WARNING: hard code color
        lastY = app.height - 100
        for i in range(self.blockNum):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = int(app.width/self.blockNum) * i
            if lastY < 100:
                ty = random.randint(100, app.height - 200)
            elif lastY + 100 > app.height:
                ty = random.randint(lastY - 250, app.height - 100)
            else:
                ty = random.randint(lastY - 100, lastY + 250)
            lastY = ty
            block = Block(tx, ty, tw, th, color)
            self.blocks.add(block)

    def createTerrain(self, app):
        self.createBase(app)
        self.createBlocks(app)
        self.createEnter(app)
        self.createExit(app)
        self.terrain = self.blocks.union(self.base)

    # create enemies
    # this is a test function which only creates fly enemies
    def createEnemies(self, app):
        color = 'aquamarine' # WARNING: hard code color
        for i in range(self.enemyNum + 1):
            if i == 0:
                continue
            ew, eh = 10, 10 # width, height = 10, 10
            ex = int(app.width/(self.enemyNum + 1)) * i
            ey = random.randint(100, app.height - 100)
            # __init__(self, x, y, w, h, color, speed, DMG, knockBack, health)
            enemy = FlyEnemy(ex, ey, ew, eh, color, 0.5, 20, 20, 50)
            for block in self.terrain:
                while enemy.isObjectCollide(block):
                    ey = random.randint(100, app.height - 100)
                    enemy = FlyEnemy(ex, ey, ew, eh, color, 0.5, 20, 20, 50)
            self.enemies.add(enemy)

    # draw function
    def drawPassLevel(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2,
                text = 'Level passed',
                font = 'Arial 20', fill = 'white')
    
    def drawDoors(self, canvas):
        x1 = self.enter.x
        y1 = self.enter.y
        w1 = self.enter.w
        h1 = self.enter.h
        canvas.create_rectangle(x1, y1, x1 + w1, y1 + h1, 
                                fill = None, outline = self.enter.color)
        x2 = self.exit.x
        y2 = self.exit.y
        w2 = self.exit.w
        h2 = self.exit.h
        canvas.create_rectangle(x2, y2, x2 + w2, y2 + h2, 
                                fill = None, outline = self.exit.color)
