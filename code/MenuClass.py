from ButtonClass import Button

class Menu():
    def __init__(self, left, right, jump, dash, slash, hold):
        self.left = left
        self.right = right
        self.jump = jump
        self.dash = dash
        self.slash = slash
        self.hold  = hold
        self.menuButtons = {}
        self.menuOn = True
    
    def __repr__(self):
        return f'controlSettings:\n\
                left = {self.left}\n\
                right = {self.right}\n\
                jump = {self.jump}\n\
                dash = {self.dash}\n'
    
    def resetKey(self, p):
        input, button = p
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
        print(self)
    
    def openMenu(self, app):
        self.menuOn = True

    def createMenu(self, app):
        leftB = Button(app.width/2 - 300, app.height/10 * 2, 200, 40, 
                            'left', 'aquamarine', 'set left', 20)
        rightB = Button(app.width/2 - 300, app.height/10 * 3, 200, 40, 
                            'right', 'aquamarine', 'set right', 20)
        jumpB = Button(app.width/2 - 300, app.height/10 * 4, 200, 40, 
                            'jump', 'aquamarine', 'set jump', 20)
        dashB = Button(app.width/2 - 300, app.height/10 * 5, 200, 40, 
                            'dash', 'aquamarine', 'set dash', 20)
        slashB = Button(app.width/2 - 300, app.height/10 * 6, 200, 40, 
                            'dash', 'aquamarine', 'set slash', 20)
        holdB = Button(app.width/2 - 300, app.height/10 * 7, 200, 40, 
                            'dash', 'aquamarine', 'set hold', 20)
        self.menuButtons = {leftB, rightB, jumpB, dashB, slashB, holdB}

    def drawMenu(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, 
                                fill = 'black', outline = None)
        canvas.create_text(app.width/2, app.height/30 + 20,
                        text = 'Press q to enter game',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 30,
                        text = 'Press a key and click to assign its function',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 40,
                        text = f'You pressed {app.inputKey}',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/10 * 9,
                        text = f'controlSettings:\n\
                                left = {self.left}\n\
                                right = {self.right}\n\
                                jump = {self.jump}\n\
                                dash = {self.dash}\n\
                                slash = {self.slash}\n\
                                hold = {self.hold}\n',
                                font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2 + 170, app.height/2 - 70,
                        text = f'Hungry Dargon',
                                font = 'Arial 50', fill = 'aquamarine')
        canvas.create_text(app.width/2 + 170, app.height/2 + 20,
                        text = f'Instructions:\n\
                                1.Kill all enemies with slash or shoot\n\
                                2.Reach the EXIT on the celling\n\
                                Drag mouse to aim, release to shoot\n\
                                3.Press {self.hold} to move grey blocks',
                                font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2 + 170, app.height/2 + 80,
                        text = f'Warning:\n\
                                1.If you stuck by terrain, click refresh\n\
                                2.You cannot push a block',
                                font = 'Arial 10', fill = 'white')
        for button in self.menuButtons:
            if button.isClicked == False:
                button.drawButton(canvas)
            else:
                button.drawButtonWait(canvas)
