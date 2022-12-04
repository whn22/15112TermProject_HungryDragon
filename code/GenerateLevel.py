import random
import copy
from BlockClass import Block, MovBlock, Platform
from EnemyClass import FlyEnemy, WalkEnemy
from FoodClass import Food

class Level():
    def __init__(self, blockNum, enemyNum, foodNum):
        # set number
        self.backupNum = blockNum, enemyNum, foodNum
        self.blockNum = blockNum
        self.enemyNum = enemyNum
        self.foodNum = foodNum
        # default settings
        self.base = set()
        self.blocks = set()
        self.terrain = set()
        self.enter = None # changable
        self.exit = None
        self.enemies = set()
        self.platforms = set()
        self.food = set()
        # pass level
        self.win = False
        self.levelOrd = 1
    
    # general methods
    # generate level
    def generateLevel(self, app):
        self.initSets()
        self.createTerrain(app)
        self.createEnemies(app)
        self.createFood()

    def refreshLevel(self, app):
        self.initSets()
        self.createTerrain(app)
        self.createEnemies(app)
        self.createFood()
        app.nightFury.resetLocation(self.enter.getLocation())

    def reStart(self, app):
        self.blockNum, self.enemyNum, self.foodNum = self.backupNum
        self.enter = None
        self.exit = None
        self.win = False
        self.levelOrd = 1
        self.refreshLevel(app)

    def initSets(self):
        # self.blockNum, self.enemyNum = self.backupNum
        self.blocks = set()
        self.terrain = set()
        self.platforms = set()
        self.enemies = set()
        self.food = set()

    def passLevel(self, player, enemies):
        # print(len(enemies), player.isObjectCollide(self.exit))
        if enemies == set() and player.isObjectCollide(self.exit):
            self.levelOrd += 1
            self.enemyNum += 1
            self.win = True

    # create terrain
    def createEnter(self, app):
        if self.enter == None:
            self.enter = Block(20, app.height - 60, 30, 60, 'aquamarine')
        else:
            # eg.end on celling, regenerate on botton.
            # same location (width = width, height flipped, vice versa)
            if self.exit == None:
                self.createExit(app)
            self.enter = Block(self.exit.x, app.height - 60, 30, 60, 'aquamarine')
    
    def createExit(self, app):
        if self.enter == None:
            self.createEnter(app)
        self.exit = Block(random.randint(70, app.width - 70 - 30), 0, 30, 15, 'aquamarine')

    def createPlatforms(self, app):
        color = 'white' # WARNING: hard code color
        # lastX = app.width - 100
        for i in range(5):
            tw = random.randint(50, 100)
            th = random.randint(10, 20)
            ty = int(app.height/6) * (i + 1)
            tx = random.randint(150, app.width - 150)
            platform = Platform(tx, ty, tw, th, color)
            self.platforms.add(platform)

    def createBase(self, app):
        platform1 = Platform(self.exit.x - 10, 120, 50, 20, 'white')
        self.blocks.add(platform1)
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
            elif lastY > app.height - 150:
                ty = random.randint(lastY - 200, app.height - 150)
            else:
                ty = random.randint(lastY - 100, lastY + 200)
            lastY = ty
            block = MovBlock(tx, ty, tw, th, color)
            self.blocks.add(block)
        copyB = copy.copy(self.blocks)
        for block in copyB:
            if block.isObjectCollide(self.enter):
                self.blocks.remove(block)
        copyB = copy.copy(self.blocks)
        for block in copyB:
            for platform in self.platforms:
                if block.isObjectCollide(platform):
                    self.blocks.discard(block)

    def createTerrain(self, app):
        self.createEnter(app)
        self.createExit(app)
        self.createPlatforms(app)
        self.createBase(app)
        self.createBlocks(app)
        # self.terrain = self.blocks.union(self.base)
        self.terrain = self.base.union(self.platforms, self.blocks)

    # create enemies
    # this is a test function which only creates fly enemies
    def createEnemies(self, app):
        color = 'white' # WARNING: hard code color
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

    # create food 
    def createFood(self):
        for i in range(self.foodNum):
            food = self.createFoodHelper()
            self.food.add(food)
    
    def createFoodHelper(self):
        color = 'red'
        fx = random.randint(200, 800)
        fy = random.randint(100, 400)
        food = Food(fx, fy, 10, 10, color)
        for block in self.terrain:
            if block.isObjectCollide(food):
                return self.createFoodHelper()
        return food

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
