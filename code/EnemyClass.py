import random
import copy
from GameObjectClass import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, w, h, color, speed, DMG, knockBack, health):
        super().__init__(x, y, w, h, color)
        # properties
        self.speed = speed
        self.DMG = DMG
        self.knockBack = knockBack
        # changable data
        self.maxHP = health
        self.HP = health
        # default data
        self.isDead = False
        self.isActive = False
        self.direction = 'Right'

    def __repr__(self):
        return f'Enemy:\n\
                x = {self.x}\n\
                y = {self.y}\n\
                width = {self.w}\n\
                height = {self.h}\n\
                color = {self.color}\n\
                speed = {self.speed}\n\
                ATK = {self.DMG}\n\
                HP = {self.HP}\n\
                isDead = {self.isDead}\n\
                direction = {self.direction}\n'
    
    # set methods
    def resetDirection(self, str): # Left or Right
        self.direction = str
    
    def changeDirection(self):
        if self.direction == 'Right':
            self.direction = 'Left'
        elif self.direction == 'Left':
            self.direction = 'Right'

    # get methods
    def getDirection(self):
        return self.direction

    def getHP(self):
        return self.HP

    # interact with player:
    def beAttacked(self, player, app):
        if self.isDead == False:
            # location
            d = player.direction
            if d == 'Left':
                self.x -= self.knockBack
                # print(app.terrain)
                test1 = self.isSetCollide(app.terrain)
                if test1:
                    self.x = test1.x + test1.w
                test2 = self.withinReasonableRange(app)
                if test2 == False:
                    self.x = 50
            elif d == 'Right':
                self.x += self.knockBack
                test1 = self.isSetCollide(app.terrain)
                if test1:
                    self.x = test1.x - self.w
                test2 = self.withinReasonableRange(app)
                if test2 == False:
                    self.x = app.width - 50
            # health
            self.HP -= player.ATK
            if self.HP <= 0:
                self.isDead = True
                self.HP = 0
    
    # AI
    def generalAI(self, player):
        if self.findDistance(player) < 150:
            self.isActive = True
        else:
            self.isActive = False

    def enemiesTimerFired(app):
        temp = copy.copy(app.enemies)
        for enemy in temp:
            # backupPosition = enemy.getLocation()
            if enemy.isDead == True:
                app.enemies.remove(enemy)
            if type(enemy) == FlyEnemy:
                enemy.flyTimerFired(app)
            if type(enemy) == WalkEnemy:
                enemy.walkTimerFired(app)
    
    # draw methods:
    def drawEnemy(self, canvas):
        if self.isDead == True:
            return
        x, y = self.getLocation()
        w, h = self.getSize()
        c = self.color
        hp = self.HP
        # this rectangle is collision box
        canvas.create_rectangle(x, y, x + w, y + h, 
                                fill = None, outline = c)
        # draw HP bar above head
        canvas.create_rectangle(x - 5, y - 10, 
                                x + hp/self.maxHP * (w + 5), y - 9, 
                                fill = 'turquoise', outline = 'turquoise')

    def drawEnemySet(enemies, canvas):
        for enemy in enemies:
            enemy.drawEnemy(canvas)

class FlyEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, DMG, knockBack, health):
        super().__init__(x, y, w, h, color, speed, DMG, knockBack, health)
        self.idlePath = []

    def resetDefaultMove(self):
        self.idlePath = []
    
    def createIdlePath(self):
        chooseX = random.choice([self.speed, -self.speed])
        chooseY = random.choice([self.speed, -self.speed])
        for i in range(30):
            self.idlePath.append((chooseX, chooseY))

    def flyIdle(self, app):
        backupPosition = self.x, self.y
        if self.idlePath == []:
            self.createIdlePath()
        dx, dy = self.idlePath.pop(0)
        self.x += dx
        self.y += dy
        for block in app.terrain:
            if self.isObjectCollide(block) == False:
                pass
            else:
                self.idlePath = []
                break
        for block in app.terrain:
            if self.isObjectCollide(block) == False \
                and self.withinReasonableRange(app):
                pass
            else:
                # print('here')
                self.resetDefaultMove()
                self.resetLocation(backupPosition)
                break
    
    def flyActive(self, app):
        pass

    # def flyAI(self, app):
    #     if self.isActive == False:
    #         self.flyIdle(app)
    #     else:
    #         self.flyActive(app)
    
    def flyTimerFired(self, app):
        if self.isActive == False:
            self.flyIdle(app)
        else:
            self.flyActive(app)

class WalkEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, DMG, knockBack, health):
        super().__init__(x, y, w, h, color, speed, DMG, knockBack, health)
        # properties
        self.gravity = 0.7
        self.jumpheight = 13
        # default data
        self.fallYs = []

    def resetDefaultMove(self):
        self.fallYs = []

    def falling(self, terrain): # generate falling coordinates if suspend.
        if self.fallYs:
            return
        u = 1 # initial falling speed
        v = self.jumpheight # Maximum falling speed
        g = self.gravity 
        y = self.y
        while True:
            y += u
            if u < v:
                u += g
            self.fallYs.append(y)
            for block in terrain:
                if block.testCollide(self.x, y, self.w, self.h):
                    self.fallYs.pop()
                    tx, ty = block.getLocation()
                    self.fallYs.append(ty - self.h)
                    return
        # print(self.fallYs)

    def doFalling(self): # if there are falling coordinates, apply them.
        if self.fallYs:
            fallY = self.fallYs.pop(0)
            self.y = fallY
        
    def walkIdle(self, app):
        backupPosition = self.x, self.y
        if self.direction == 'Right':
            self.x += self.speed
        elif self.direction == 'Left':
            self.x -= self.speed
        for block in app.terrain:
            if self.isObjectCollide(block) == False and \
                self.withinCanvasRange(app) and \
                self.testExceedEdge(block) == False:
                pass
            else:
                self.x, self.y = backupPosition
                self.changeDirection()
                break
    
    def walkActive(self, app):
        pass

    # def walkAI(self, app):
    #     if self.isActive == False:
    #         self.walkIdle(app)
    #     else:
    #         self.walkActive(app)

    def walkTimerFired(self, app):
        if self.isActive == False:
            self.walkIdle(app)
        else:
            self.walkActive(app)