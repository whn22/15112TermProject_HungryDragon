class Display():
    def drawPSbar(app, canvas):
        ps = app.nightFury.PS
        canvas.create_text(40, 50,
                        text = 'Stamina',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 60, 10 + ps/100 * 200, 63,
                                fill = 'cyan', outline = 'cyan')

    def drawHPbar(app, canvas):
        hp = app.nightFury.HP
        canvas.create_text(40, 72,
                        text = 'Health  ',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 80, 10 + hp/100 * 200, 83, 
                                fill = 'turquoise', outline = 'turquoise')
    
    def drawLevelNum(app, canvas):
        levelN = app.level.levelOrd
        canvas.create_text(65, 25,
                        text = f'Current level: {levelN}',
                        font = 'Arial 13', fill = 'white')

    def display(app, canvas):
        Display.drawPSbar(app, canvas)
        Display.drawHPbar(app, canvas)
        Display.drawLevelNum(app, canvas)