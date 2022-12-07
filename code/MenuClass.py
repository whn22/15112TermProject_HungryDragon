from ButtonClass import Button
from GenerateLevel import Level


class Menu():
    def __init__(self, left, right, jump, dash, slash, hold):
        self.left = left
        self.right = right
        self.jump = jump
        self.dash = dash
        self.slash = slash
        self.hold = hold
        self.levelSelect = 'normal'
        self.menuButtons = set()
        self.menuOn = True
    
    def __repr__(self):
        return f'controlSettings:\n\
                left = {self.left}\n\
                right = {self.right}\n\
                jump = {self.jump}\n\
                dash = {self.dash}\n\
                hold = {self.hold}'

    def doFunction(self, p):
        input, button, app = p
        if button.ID == 'left':
            self.left = input
        elif button.ID == 'right':
            self.right = input
        elif button.ID == 'jump':
            self.jump = input
        elif button.ID == 'dash':
            self.dash = input
        elif button.ID == 'slash':
            self.slash = input
        elif button.ID == 'hold':
            self.hold = input
        elif button.ID == 'easy':
            level, nightFury = Level.easy(app)
            app.level = level
            app.terrain = level.terrain
            app.enemies = level.enemies
            app.nightFury = nightFury
            self.levelSelect = 'easy'
        elif button.ID == 'normal':
            level, nightFury = Level.normal(app)
            app.level = level
            app.terrain = level.terrain
            app.enemies = level.enemies
            app.nightFury = nightFury
            self.levelSelect = 'normal'
        elif button.ID == 'difficult':
            level, nightFury = Level.difficult(app)
            app.level = level
            app.terrain = level.terrain
            app.enemies = level.enemies
            app.nightFury = nightFury
            self.levelSelect = 'difficult'
        # print(self)
    
    def openMenu(self, app):
        self.menuOn = True

    def createMenu(self, app):
        self.createSetKeys(app)
        self.createSelectDifficulty(app)

    def createSetKeys(self, app):
        leftB = Button(app.width/2 - 300, app.height/10 * 2, 200, 40, 
                            'left', 'aquamarine', 'set left', 20)
        rightB = Button(app.width/2 - 300, app.height/10 * 3, 200, 40, 
                            'right', 'aquamarine', 'set right', 20)
        jumpB = Button(app.width/2 - 300, app.height/10 * 4, 200, 40, 
                            'jump', 'aquamarine', 'set jump', 20)
        dashB = Button(app.width/2 - 300, app.height/10 * 5, 200, 40, 
                            'dash', 'aquamarine', 'set dash', 20)
        slashB = Button(app.width/2 - 300, app.height/10 * 6, 200, 40, 
                            'slash', 'aquamarine', 'set slash', 20)
        holdB = Button(app.width/2 - 300, app.height/10 * 7, 200, 40, 
                            'hold', 'aquamarine', 'set hold', 20)
        self.menuButtons = self.menuButtons.union({leftB, rightB, jumpB, dashB, slashB, holdB})

    def createSelectDifficulty(self, app):
        easy = Button(app.width/2 + 12, app.height/2 - 65, 90, 25, 
                            'easy', 'turquoise', 'EASY', 14)
        normal = Button(app.width/2 + 122, app.height/2 - 65, 90, 25, 
                            'normal', 'turquoise', 'NORMAL', 14)
        difficult = Button(app.width/2 + 232, app.height/2 - 65, 90, 25, 
                            'difficult', 'turquoise', 'DIFFICULT', 14)
        self.menuButtons = self.menuButtons.union({easy, normal, difficult})

    def drawMenu(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, 
                                fill = 'black', outline = None)
        canvas.create_text(app.width/2, app.height/30 + 20,
                        text = 'Press q to enter game',
                        font = 'Arial 12', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 32,
                        text = 'Press p to play or stop backgound music',
                        font = 'Arial 12', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 44,
                        text = f'Press a key and click to assign its function',
                        font = 'Arial 12', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 56,
                        text = f'You pressed {app.inputKey}',
                        font = 'Arial 12', fill = 'turquoise')
        canvas.create_text(app.width/2, app.height/10 * 9,
                        text = f'controlSettings:\n\
                                left = {self.left}\n\
                                right = {self.right}\n\
                                jump = {self.jump}\n\
                                dash = {self.dash}\n\
                                slash = {self.slash}\n\
                                hold = {self.hold}\n',
                                font = 'Arial 12', fill = 'white')
        canvas.create_text(app.width/2 + 170, app.height/2 - 110,
                        text = f'Hungry Dragon',
                                font = 'Arial 50', fill = 'aquamarine')
        canvas.create_text(app.width/2 + 170, app.height/2 + 20,
                        text = f'Instructions:\n\
                                1. Kill all enemies with slash or shoot\n\
                                2. Reach the EXIT on the celling\n\
                                3. Drag mouse to aim, release to shoot\n\
                                4. Eat the green square to regain health\n\
                                5. Press {self.hold} to move grey blocks',
                                font = 'Arial 12', fill = 'white')
        canvas.create_text(app.width/2 + 163, app.height/2 + 90,
                        text = f'Warning:\n\
                                1. If you stuck by terrain, click refresh\n\
                                2. You cannot push a block',
                                font = 'Arial 12', fill = 'white')
        # print(self.menuButtons)
        for button in self.menuButtons:
            if button.isClicked == False:
                button.drawButton(canvas)
            else:
                button.drawButtonWait(canvas)
