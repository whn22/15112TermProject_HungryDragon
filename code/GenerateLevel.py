import random
from ControlSetClass import ControlSet
from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import FlyEnemy, WalkEnemy
from NightFuryClass import NightFury

class Level1():
    def __init__(self, blockNum, enemyNum):
        # set number
        self.backupNum = blockNum * 4, enemyNum
        self.blockNum = blockNum * 4
        self.enemyNum = enemyNum
        # default settings
        self.base = set()
        self.blocks = set()
        self.terrain = set()
        self.enter = None # changable
        self.exit = None
        self.enemies = set()
        self.win = False
    
    def refresh(self, app):
        self.initAll()
        self.createTerrain(app)

    def initAll(self):
        self.blockNum, self.enemyNum = self.backupNum
        self.blocks = set()
        self.terrain = set()
        # self.enemies = set()

    # def findMinDistance(self, block):
    #     terrain = list(self.terrain)
    #     minDX = 0
    #     minDY = 0
    #     pass

    def passLevel(self, player, enemies):
        if enemies == set() and player.isObjectCollide(self.exit):
            self.win = True

    # this function is wrong, do not use it
    def testVaildPath(self):
        terrain = list(self.terrain)
        maxDX = 0
        maxDY = 0
        for i in range(len(terrain) - 1):
            for j in range(i + 1, len(terrain)):
                dy = abs(terrain[i].y - terrain[j].y)
                if dy > maxDY:
                    maxDY = dy
                dx = abs(terrain[i].x - terrain[j].x)
                if dx > maxDX:
                    maxDX = dx
        print(maxDY, maxDX)
        if maxDY > 120 or maxDX > 200:
            return False
        else:
            return True

    # def GenerateDoor(self): # generate two doors, one for enter, one for exit

    #     pass

    # def terrainAddBlock(self, app):
    #     color = 'grey' # WARNING: hard code color
    #     ground = Block(0, 590, 1000, 10, color)
    #     self.terrain.add(ground)
    #     tw = random.randint(20, 200)
    #     th = random.randint(10, 100)
    #     tx = random.randint(0, app.width - tw)
    #     ty = random.randint(100, app.height - th)
    #     block = Block(tx, ty, tw, th, color)
    #     self.terrain.add(block)

    def createEnter(self, app):
        if self.enter == None:
            self.enter = Block(20, app.height - 10, 30, 10, 'aquamarine')
        else:
            # eg.end on celling, regenerate on botton.
            # same location (width = width, height flipped, vice versa)
            if self.exit == None:
                self.createExit(app)
            self.enter = Block(self.exit.x, app.height - 10, 30, 10, 'aquamarine')
    
    def createExit(self, app):
        if self.enter == None:
            self.createEnter(app)
        self.exit = Block(random.randint(20, app.width - 20 - 30), 0, 30, 10, 'aquamarine')
        platform = Block(self.exit.x - 10, 100, 50, 20, 'grey')
        self.blocks.add(platform)

    # def createExit(self, app):
    #     exitx, exity = -1, -1
    #     # exitw, exith = 30, 10 or 10, 30
    #     if self.enter == None:
    #         self.enter = Block(10, app.height - 10, 30, 10, 'aquamarine')
    #     enterx, entery = self.enter.getLocation()
    #     if enterx == 0:
    #         exitx = random.choice(app.width - 10, random.randint(10, app.width - 10 - 30))
    #         if exitx == app.width - 10:
    #             # 30 is the width of the door
    #             exity = random.randint(10, app.height - 10 - 30)
    #         else:
    #             if entery < app.height/2:
    #                 exity = app.height - 10
    #             else:
    #                 exity = 0
    #     if entery == app.height - 10:
    #         exity = random.choice(0, random.randint(10, app.height - 10 - 30))
    #         if exity == 0:
    #             exitx = random.randint(10, app.width - 10 - 30)
    #         else:
    #             if enterx < app.width/2:
    #                 exitx = app.width - 10
    #             else:
    #                 exitx = 0
    #     self.exit = Block(exitx, exity, 30, 10, 'aquamarine')

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
        # using recursion
        # random generate n blocks (within canvas range), 
        # if they can from a path to the success end, then legal
        # if not, generate again.
        color = 'grey' # WARNING: hard code color
        for i in range(self.blockNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(20, app.width/2 - tw)
            ty = random.randint(100, app.height/2 - th)
            block = Block(tx, ty, tw, th, color)
            self.blocks.add(block)
        for i in range(self.blockNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(app.width/2 - tw, app.width)
            ty = random.randint(100, app.height/2 - th)
            block = Block(tx, ty, tw, th, color)
            self.blocks.add(block)
        for i in range(self.blockNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(20, app.width/2 - tw)
            ty = random.randint(app.height/2 - th, app.height - th)
            block = Block(tx, ty, tw, th, color)
            self.blocks.add(block)
        for i in range(self.blockNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(app.width/2 - tw, app.width)
            ty = random.randint(app.height/2 - th, app.height - th)
            block = Block(tx, ty, tw, th, color)
            self.blocks.add(block)

    def createTerrain(self, app):
        self.createBase(app)
        self.createBlocks(app)
        self.createEnter(app)
        self.createExit(app)
        self.terrain = self.blocks.union(self.base)
        self.terrain.add(self.enter)
        self.terrain.add(self.exit)

    def drawPassLevel(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2,
                text = 'Level passed',
                font = 'Arial 20', fill = 'white')

    # def createTerrain(self, app):
    #     self.createBlocks(app)
    #     if self.blocks != set() and self.testVaildPath():
    #         self.terrain = self.blocks + self.base
    #         self.terrain.add(self.enter)
    #         self.terrain.add(self.exit)
    #     else:
    #         self.initAll()
    #         self.terrain = set()
    #         self.createTerrain(app)

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
    #         flyEnemy7}

    
    # def createTerrain(self, app):
    #     # using recursion
    #     # random generate n blocks (within canvas range), 
    #     # if they can from a path to the success end, then legal
    #     # if not, generate again.
        
    #     color = 'grey' # WARNING: hard code color
    #     ground = Block(0, 590, 1000, 10, color)
    #     self.terrain.add(ground)
    #     if self.blockNum == 0:
    #         self.initAll()
    #         return
    #     else:
    #         tw = random.randint(20, 200)
    #         th = random.randint(10, 100)
    #         tx = random.randint(0, app.width/2 - tw)
    #         ty = random.randint(100, app.height/2 - th)
    #         block = Block(tx, ty, tw, th, color)
    #         if ty - 
    #         self.terrain.add(block)

    # controlSettings = ControlSet('Left', 'Right', 'x', 'z')
    # settings = Button(10, 10, 60, 20, 'menu', 'aquamarine', 'settings', 10)
