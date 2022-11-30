from ButtonClass import Button

class Menu():
    def __init__(self, left, right, jump, dash):
        self.left = left
        self.right = right
        self.jump = jump
        self.dash = dash
        self.menuButtons = {}
        self.menuOn = False
    
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
        print(self)
    
    def openMenu(self, app):
        self.menuOn = True

    def createMenu(self, app):
        leftB = Button(app.width/2 - 300, app.height/10 * 3, 200, 40, 
                            'left', 'aquamarine', 'set left', 20)
        rightB = Button(app.width/2 - 300, app.height/10 * 4, 200, 40, 
                            'right', 'aquamarine', 'set right', 20)
        jumpB = Button(app.width/2 - 300, app.height/10 * 5, 200, 40, 
                            'jump', 'aquamarine', 'set jump', 20)
        dashB = Button(app.width/2 - 300, app.height/10 * 6, 200, 40, 
                            'dash', 'aquamarine', 'set dash', 20)
        self.menuButtons = {leftB, rightB, jumpB, dashB}

    def drawMenu(self, app, canvas):
        canvas.create_rectangle(0, 0, app.width, app.height, 
                                fill = 'black', outline = None)
        canvas.create_text(app.width/2, app.height/30,
                        text = 'Press q to exit',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 10,
                        text = 'Press a key and click to assign its function',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/30 + 20,
                        text = f'You pressed {app.inputKey}',
                        font = 'Arial 10', fill = 'white')
        canvas.create_text(app.width/2, app.height/10 * 9,
                        text = f'controlSettings:\n\
                                left = {self.left}\n\
                                right = {self.right}\n\
                                jump = {self.jump}\n\
                                dash = {self.dash}\n',
                        font = 'Arial 10', fill = 'white')
        for button in self.menuButtons:
            if button.isClicked == False:
                button.drawButton(canvas)
            else:
                button.drawButtonWait(canvas)
