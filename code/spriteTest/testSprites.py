# This demos sprites using Pillow/PIL images
# See here for more details:
# https://pillow.readthedocs.io/en/stable/reference/Image.html

# This uses a spritestrip from this tutorial:
# https://www.codeandweb.com/texturepacker/tutorials/how-to-create-a-sprite-sheet

from cmu_112_graphics import *

def appStarted(app):
    app.NFidle = '001_nf_Idle.png'
    spritestrip = app.loadImage(app.NFidle)
    app.sprites = [ ]
    for i in range(9):
        sprite = spritestrip.crop((61*i, 0, 60+61*i, 200))
        app.sprites.append(sprite)
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))

runApp(width=400, height=400)