from ButtonClass import Button

class ControlSet():
    def __init__(self, left, right, jump, dash):
        self.left = left
        self.right = right
        self.jump = jump
        self.dash = dash
    
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

    # def resetLeftKey(self, event):
    #     self.left = event.key
    
    # def resetRightKey(self, event):
    #     self.right = event.key

    # def resetJumpKey(self, event):
    #     self.jump = event.key

    # def resetDashKey(self, event):
    #     self.dash = event.key

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
        for button in app.menuButtons:
            if button.isClicked == False:
                button.drawButton(canvas)
            else:
                button.drawButtonWait(canvas)
