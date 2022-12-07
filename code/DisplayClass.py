class Display():
    def drawPSbar(app, canvas):
        ps = app.nightFury.PS
        maxPS = app.nightFury.maxPS
        canvas.create_text(40, 50,
                        text = 'Stamina',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 60, 20 + ps/maxPS * 200, 63,
                                fill = 'cyan', outline = 'cyan')

    def drawHPbar(app, canvas):
        hp = app.nightFury.HP
        maxHP = app.nightFury.maxHP
        canvas.create_text(40, 72,
                        text = 'Health  ',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 80, 20 + hp/maxHP * 200, 83, 
                                fill = 'turquoise', outline = 'turquoise')
    
    def drawLevelNum(app, canvas):
        levelN = app.level.levelOrd
        canvas.create_text(110, 25,
                text = f'Current level: {levelN}, Mode: {app.menu.levelSelect}',
                font = 'Arial 13', fill = 'white')

    def display(app, canvas):
        Display.drawPSbar(app, canvas)
        Display.drawHPbar(app, canvas)
        Display.drawLevelNum(app, canvas)