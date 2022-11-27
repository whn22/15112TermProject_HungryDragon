import random
from ControlSetClass import ControlSet
from ButtonClass import Button
from BlockClass import Block
from NightFuryClass import NightFury
from EnemyClass import FlyEnemy, WalkEnemy
from NightFuryClass import NightFury

class Level1():
    def __init__(self, terrainNum, enemyNum, player):
        # set number
        self.backupNum = terrainNum * 4, enemyNum
        self.terrainNum = terrainNum * 4
        self.enemyNum = enemyNum
        # default settings
        self.base = set()
        self.terrain = set()
        self.door = (0, 590 - player.h) # changable
        self.startEndLoc = [0, 590 - player.h]
        self.enemies = set()
    
    def initNum(self):
        self.terrainNum, self.enemyNum = self.backupNum

    def findMinDistance(self, block):
        terrain = list(self.terrain)
        minDX = 0
        minDY = 0
        pass

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

    def GenerateDoor(): # generate two doors, one for enter, one for exit
        pass

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
        for i in range(self.terrainNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(0, app.width/2 - tw)
            ty = random.randint(100, app.height/2 - th)
            block = Block(tx, ty, tw, th, color)
            self.terrain.add(block)
        for i in range(self.terrainNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(app.width/2 - tw, app.width)
            ty = random.randint(100, app.height/2 - th)
            block = Block(tx, ty, tw, th, color)
            self.terrain.add(block)
        for i in range(self.terrainNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(0, app.width/2 - tw)
            ty = random.randint(app.height/2 - th, app.height - th)
            block = Block(tx, ty, tw, th, color)
            self.terrain.add(block)
        for i in range(self.terrainNum//4):
            tw = random.randint(20, 200)
            th = random.randint(10, 100)
            tx = random.randint(app.width/2 - tw, app.width)
            ty = random.randint(app.height/2 - th, app.height - th)
            block = Block(tx, ty, tw, th, color)
            self.terrain.add(block)
    
    def createTerrain(self, app):
        self.createBlocks(app)
        if self.terrain != set() and self.testVaildPath():
            self.terrain = self.terrain + self.base
        else:
            self.initNum()
            self.terrain = set()
            self.createTerrain(app)

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
    #     if self.terrainNum == 0:
    #         self.initNum()
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
