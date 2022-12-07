import random
import copy
import math
from GameObjectClass import GameObject
from AttackBoxClass import AttackBox

class Enemy(GameObject):
    def __init__(self, x, y, w, h, color, speed, ATK, knockBack, health):
        super().__init__(x, y, w, h, color)
        # properties
        self.speed = speed
        self.ATK = ATK
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
                ATK = {self.ATK}\n\
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
        backup = self.x, self.y
        if self.isDead == False:
            # location
            d = player.direction
            if d == 'Left':
                self.x -= self.knockBack
                # print(app.terrain)
                test1 = self.isSetCollide(app.terrain)
                if test1:
                    self.x = test1.x + test1.w
                if self.isActive == False:
                    test2 = self.withinReasonableRange(app)
                    if test2 == False:
                        self.x, self.y = backup
            elif d == 'Right':
                self.x += self.knockBack
                test1 = self.isSetCollide(app.terrain)
                if test1:
                    self.x = test1.x - self.w
                if self.isActive == False:
                    test2 = self.withinReasonableRange(app)
                    if test2 == False:
                        self.x, self.y = backup
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
            enemy.generalAI(app.nightFury)
            if enemy.isDead == True:
                app.enemies.remove(enemy)
            if type(enemy) == FlyEnemy:
                enemy.flyTimerFired(app)
            if type(enemy) == WalkEnemy:
                enemy.walkTimerFired(app)
            if type(enemy) == Boss:
                enemy.bossTimerFired(app)
            if type(enemy) == Summoned:
                enemy.isActive = True
                enemy.flyTimerFired(app)
    
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
            if type(enemy) == Boss:
                enemy.drawShoot(canvas) 
            enemy.drawEnemy(canvas)

class FlyEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, ATK, knockBack, health):
        super().__init__(x, y, w, h, color, speed, ATK, knockBack, health)
        self.idlePath = []
        self.activePath = []

    def resetDefaultMove(self):
        self.idlePath = []
        self.activePath = []
    
    def createIdlePath(self):
        dx = random.choice([self.speed, -self.speed])
        dy = random.choice([self.speed, -self.speed])
        for i in range(30):
            self.idlePath.append((dx, dy))

    def flyIdle(self, app):
        # if self.isActive:
        #     return
        backupPosition = self.x, self.y
        if self.idlePath == []:
            self.createIdlePath()
        dx, dy = self.idlePath.pop(0)
        self.x += dx
        self.y += dy
        for block in app.terrain:
            if self.isObjectCollide(block) == False \
                and self.withinReasonableRange(app):
                pass
            else:
                self.idlePath = []
                self.resetLocation(backupPosition)
                break
    
    def createActivePathHelper(self, px, py):
        dx = random.choice([self.speed * 3, -self.speed * 3])
        dy = random.choice([self.speed * 3, -self.speed * 3])
        old = GameObject.testFindDistance(px, py, self.x, self.y)
        now = GameObject.testFindDistance(px, py, self.x + dx, self.y + dy)
        if now < old:
            return dx, dy
        else:
            return self.createActivePathHelper(px, py)

    def createActivePath(self, app):
        px, py = app.nightFury.getLocation()
        dx, dy = self.createActivePathHelper(px, py)
        for i in range(30):
            self.activePath.append((dx, dy))

    def flyActive(self, app):
        # if self.isActive == False:
        #     return
        backupPosition = self.x, self.y
        if self.activePath == []:
            self.createActivePath(app)
        dx, dy = self.activePath.pop(0)
        self.x += dx
        self.y += dy
        for block in app.terrain:
            if self.isObjectCollide(block) == False:
                pass
            else:
                self.activePath = []
                self.resetLocation(backupPosition)
                break

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

# this class has error, can't be used
class WalkEnemy(Enemy):
    def __init__(self, x, y, w, h, color, speed, ATK, knockBack, health):
        super().__init__(x, y, w, h, color, speed, ATK, knockBack, health)
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

class Summoned(FlyEnemy):
    def __init__(self, x, y, w, h, color, speed, ATK, knockBack, health):
        super().__init__(x, y, w, h, color, speed, ATK, knockBack, health)
        self.isActive = True

class Boss(FlyEnemy):
    def __init__(self, x, y, w, h, color, speed, ATK, knockBack, health, 
                    bulletNum):
        super().__init__(x, y, w, h, color, speed, ATK, knockBack, health)
        self.bulletNum = bulletNum
        # self.shooting = False
        self.bulletsP = []
        self.bullets = set()
        self.bulletP = []
        self.bullet = None
        self.isActive = True
        self.attackBox = AttackBox(self.x, self.y, self.w, self.h, 'aquamarine')
        self.interval = list(range(0, 30))
        self.count = 0
        self.summonNum = 3
        self.enemies = set()

    def resetinterval(self):
        self.interval = list(range(0, 30))

    def createBullet(self, app):
        # if self.shooting == False:
        #     return
        for n in range(self.bulletNum):
            (cx, cy, r) = (self.x + self.w/2 - 10, self.y + self.h/2 - 10, 1000)
            angle = math.pi/2 - (2 * math.pi) * (n/self.bulletNum )
            nx = cx + r * math.cos(angle)
            ny = cy - r * math.sin(angle)
            # self.bullets.append((nX, nY))
            dx = nx - cx
            dy = ny - cy
            if dx == 0 or dy == 0:
                return
            a = dy/dx # gradient
            # b = ny - a*nx # intersection
            d = 5 # the interval between sprites
            dsx = (d**2/(1 + a**2))**0.5
            dsy = a * dsx
            while True:
                if dx < 0:
                    cx -= dsx
                    cy -= dsy
                else:
                    cx += dsx
                    cy += dsy
                self.bulletP.append((cx, cy))
                if app.nightFury.testCollide(cx, cy, 10, 10) or \
                    GameObject.pointWithinCanvasRange(cx, cy, app) == False:
                    break
            self.bulletsP.append(self.bulletP)
            self.bulletP = []
        # print(self.bulletsP, 'here!!!')

    def shoot(self, app):
        # print(self.bullets)
        self.bullets = set()
        if self.bulletsP:
            for bulletP in self.bulletsP:
                if bulletP:
                    x, y = bulletP.pop(0)
                    self.bullet = GameObject(x, y, 20, 20, 'aquamarine')
                    self.bullets.add(self.bullet)
                    if app.nightFury.isObjectCollide(self.bullet) and \
                                                    app.nightFury.immune == []:
                        app.nightFury.HP -= self.ATK
                        app.nightFury.resetImmune()
                        if app.nightFury.HP < 0:
                            app.nightFury.isDead = True
                            app.nightFury.HP = 0
                        return

    def drawShoot(self, canvas):
        if self.bullets:
        #and self.shooting == True:
            for bullet in self.bullets:
                bullet.drawGameObject(canvas)

    def skill1TimerFired(self, app):
        self.flyActive(app)
        if self.interval == []:
            self.resetinterval()
            self.count += 1
        else:
            self.interval.pop()

    def skill2TimerFired(self, app):
        self.flyIdle(app)
        if self.interval == []:
            self.resetinterval()
            self.count += 1
        else:
            self.interval.pop()

    def skill3TimerFired(self, app):
        # self.isActive = True
        # self.shooting = True
        self.flyActive(app)
        if self.interval == []:
            self.createBullet(app)
            self.resetinterval()
            self.count += 1
        else:
            self.interval.pop()

    def summonEnemies(self, app):
        color = 'white' # WARNING: hard code color
        ew, eh = 10, 10 # width, height = 10, 10
        ex, ey = self.x + self.w/2 - 5, self.y + self.h/2 - 5
        enemy = Summoned(ex, ey, ew, eh, color, 1, 20, 20, 30)
        app.enemies.add(enemy)

    def skill4TimerFired(self, app):
        if self.interval == []:
            self.summonEnemies(app)
            self.resetinterval()
            self.count += 1
        else:
            self.interval.pop()

    def bossTimerFired(self, app):
        if self.count <= 10:
            self.skill1TimerFired(app)
        elif self.count <= 15:
            # self.isActive = True
            self.skill3TimerFired(app)
        elif self.count <= 25:
            self.skill2TimerFired(app)
        elif self.count <= 30:
            self.skill3TimerFired(app)
        elif self.count <= 40:
            self.skill2TimerFired(app)
        elif self.count <= 43:
            self.skill4TimerFired(app)
        else:
            self.count = 0
        self.shoot(app)