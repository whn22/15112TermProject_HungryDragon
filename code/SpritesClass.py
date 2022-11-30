from cmu_112_graphics import *
from NightFuryClass import NightFury

class NightFurySprites():
    def __init__(self):
        # idle
        self.idleLeft = []
        self.idleRight = []
        self.idleCount = 0
        # run
        self.runLeft = []
        self.runRight = []
        self.runCount = 0
        # slash
        self.slashLeft = []
        self.slashRight = []
        self.effectLeft = []
        self.effectRight = []
        # self.slashCount = 0
        # # slashAlt
        # self.slashAlt = []
        # self.slashEffectAlt = []
        # Air
        self.airLeft = []
        self.airRight = []
        # self.airCount = 0
        # fall
        self.fallL = None
        self.fallR = None
        # self.fallCount = 0
        # dash
        self.dashL = []
        self.dashR = []
    
    def initializeIdle(self, app):
        NFidleLeft = '001_nf_Idle.png'
        idleL = app.loadImage(NFidleLeft)
        idleL = app.scaleImage(idleL, 0.6)
        for i in range(9):
            sprite = idleL.crop((36.5*i, 0, 36.5+36.5*i, 170))
            # sprite = idleL.crop((61*i, 0, 60+61*i, 190))
            for j in range(5):
                self.idleLeft.append(sprite)
        idleR = idleL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(9):
            sprite = idleR.crop((36.5*i, 0, 36.5+36.5*i, 170))
            # sprite = idleR.crop((61*i, 0, 60+61*i, 190))
            for j in range(5):
                self.idleRight.append(sprite)

    def initializeRun(self, app):
        NFRunLeft = '002_nf_Run.png'
        runL = app.loadImage(NFRunLeft)
        runL = app.scaleImage(runL, 0.6)
        for i in range(13):
            sprite = runL.crop((52*i, 0, 52+52*i, 170))
            # sprite = idleL.crop((61*i, 0, 60+61*i, 190))
            for j in range(4):
                self.runLeft.append(sprite)
        runR = runL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(13):
            sprite = runR.crop((52*i, 0, 52+52*i, 170))
            # sprite = idleR.crop((61*i, 0, 60+61*i, 190))
            for j in range(4):
                self.runRight.append(sprite)

    def initializeSlash(self, app):
        NFSlashLeft = '003_nf_Slash.png'
        slashL = app.loadImage(NFSlashLeft)
        slashL = app.scaleImage(slashL, 0.6)
        for i in range(15):
            sprite = slashL.crop((65*i, 0, 65+65*i, 170))
            self.slashLeft.append(sprite)
        slashR = slashL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(15):
            sprite = slashR.crop((65*i, 0, 65+65*i, 170))
            self.slashRight.append(sprite)
        NFeffectLeft = '004_nf_SlashEffect.png'
        effectL = app.loadImage(NFeffectLeft)
        for i in range(4):
            sprite = effectL.crop((157*i, 0, 157+157*i, 170))
            self.effectLeft.append(sprite)
        effectR = effectL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(4):
            sprite = effectR.crop((157*i, 0, 157+157*i, 170))
            self.effectRight.append(sprite)
    
    def initializeAirBorne(self, app):
        NFAir = '005_nf_AirBorne.png'
        airL = app.loadImage(NFAir)
        airL = app.scaleImage(airL, 0.6)
        for i in range(12):
            sprite = airL.crop((62*i, 0, 62+62*i, 170))
            for j in range(4):
                self.airLeft.append(sprite)
        airR = airL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(12):
            sprite = airR.crop((62*i, 0, 62+62*i, 170))
            for j in range(4):
                self.airRight.append(sprite)

    def initializeFall(self, app):
        NFfall = '006_nf_Fall.png'
        self.fallL = app.loadImage(NFfall)
        self.fallL = app.scaleImage(self.fallL, 0.6)
        self.fallR = self.fallL.transpose(Image.FLIP_LEFT_RIGHT)
    
    def initializeDash(self, app):
        NFdashLeft = '007_nf_Dash.png'
        dashL = app.loadImage(NFdashLeft)
        dashL = app.scaleImage(dashL, 0.6)
        for i in range(9):
            sprite = dashL.crop((115*i, 0, 115+115*i, 170))
            for j in range(2):
                self.dashL.append(sprite)
        dashR = dashL.transpose(Image.FLIP_LEFT_RIGHT)
        for i in range(9):
            sprite = dashR.crop((115*i, 0, 115+115*i, 170))
            for j in range(2):
                self.dashR.append(sprite)

    def initializeAll(self, app):
        self.initializeIdle(app)
        self.initializeRun(app)
        self.initializeSlash(app)
        self.initializeAirBorne(app)
        self.initializeFall(app)
        self.initializeDash(app)

    def nfSpritesTimer(self):
        self.idleCount = (1 + self.idleCount) % len(self.idleLeft)
        self.runCount = (1 + self.runCount) % len(self.runLeft)
    
    def drawIdle(self, player, canvas):
        if player.direction == 'Left':
            sprite = self.idleLeft[self.idleCount]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
        elif player.direction == 'Right':
            sprite = self.idleRight[self.idleCount]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))

    def drawRun(self, player, app, canvas):
        if app.nfGoLeft == True:
            sprite = self.runLeft[self.runCount]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            return True
        elif app.nfGoRight == True:
            sprite = self.runRight[self.runCount]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            return True

    def drawSlash(self, player, canvas):
        if player.slashFramesL:
            # print('left', player.frame)
            sprite = self.slashLeft[player.slashFrame - 1]
            canvas.create_image(player.x, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            if player.slashFrame > 2 and player.slashFrame < 7:
                effect = self.effectLeft[player.slashFrame - 3]
                canvas.create_image(player.x - player.w * 2.4, player.y + player.h, 
                                image=ImageTk.PhotoImage(effect))
            return True
        elif player.slashFramesR:
            # print('right', player.frame)
            sprite = self.slashRight[len(self.effectRight) - (player.slashFrame - 1) - 1]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            if player.slashFrame > 2 and player.slashFrame < 7:
                effect = self.effectRight[len(self.effectRight) - (player.slashFrame - 3) - 1]
                canvas.create_image(player.x + player.w * 3, player.y + player.h, 
                                image=ImageTk.PhotoImage(effect))
            return True

    def drawAir(self, player, canvas):
        if player.jumpYs and player.direction == 'Left':
            sprite = self.airLeft[player.lenJ - len(player.jumpYs)]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h, 
                                image=ImageTk.PhotoImage(sprite))
            return True
        elif player.jumpYs and player.direction == 'Right':
            sprite = self.airRight[player.lenJ - len(player.jumpYs)]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h, 
                                image=ImageTk.PhotoImage(sprite))
            return True
    
    def drawFall(self, player, canvas):
        if player.fallYs and player.direction == 'Left':
            canvas.create_image(player.x + player.w * 0.6, player.y, 
                        image=ImageTk.PhotoImage(self.fallL))
            return True
        elif player.fallYs and player.direction == 'Right':
            canvas.create_image(player.x + player.w * 0.6, player.y, 
                        image=ImageTk.PhotoImage(self.fallR))
            return True
    
    def drawDash(self, player, canvas):
        if player.dashLXs:
            sprite = self.dashL[len(self.dashL) - len(player.dashLXs)]
            canvas.create_image(player.x + player.w * 0.6, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            return True
        if player.dashRXs:
            sprite = self.dashR[len(self.dashR) - len(player.dashRXs)]
            canvas.create_image(player.x, player.y + player.h * 1.2, 
                                image=ImageTk.PhotoImage(sprite))
            return True

    def drawSprites(self, app, player, canvas):
        if self.drawSlash(player, canvas):
            return
        elif self.drawDash(player, canvas):
            return
        elif self.drawAir(player, canvas):
            return
        elif self.drawFall(player, canvas):
            return
        elif self.drawRun(player, app, canvas):
            return
        else:
            self.drawIdle(player, canvas)

class EnemySprites():
    def __init__(app):
        app.idle = []

class TerrainSprites():
    def __init__(app):
        app.block = []

