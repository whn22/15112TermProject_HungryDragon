class Display():
    def drawPSbar(app, canvas):
        ps = app.nightFury.PS
        canvas.create_text(40, 20,
                        text = 'Stamina',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 30, 10 + ps/100 * 200, 33,
                                fill = 'cyan', outline = 'cyan')

    def drawHPbar(app, canvas):
        hp = app.nightFury.HP
        canvas.create_text(40, 42,
                        text = 'Health  ',
                        font = 'Arial 10', fill = 'white')
        canvas.create_rectangle(20, 50, 10 + hp/100 * 200, 53, 
                                fill = 'turquoise', outline = 'turquoise')
    
    def display(app, canvas):
        Display.drawPSbar(app, canvas)
        Display.drawHPbar(app, canvas)