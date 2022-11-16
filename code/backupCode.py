# def drawLeftSlash(app, canvas):
#     nfX, nfY = app.nightFury.getLocation()
#     nfW, nfH = app.nightFury.getSize()
#     nfX += nfW/2
#     canvas.create_polygon(nfX, nfY - 20, 
#                             nfX - 60, nfY - 15, 
#                             nfX - 100, nfY, 
#                             nfX - 120, nfY + 15, 
#                             nfX - 120, nfY + nfH - 15, 
#                             nfX - 100, nfY + nfH, 
#                             nfX - 60, nfY + nfH + 15, 
#                             nfX, nfH + nfY + 20, 
#                             fill = None, outline = 'blue')
                            
# def drawRightSlash(app, canvas):
#     nfX, nfY = app.nightFury.getLocation()
#     nfW, nfH = app.nightFury.getSize()
#     nfX += nfW/2
#     canvas.create_polygon(nfX, nfY - 20, 
#                             nfX + 60, nfY - 15, 
#                             nfX + 100, nfY, 
#                             nfX + 120, nfY + 15, 
#                             nfX + 120, nfY + nfH - 15, 
#                             nfX + 100, nfY + nfH, 
#                             nfX + 60, nfY + nfH + 15, 
#                             nfX, nfH + nfY + 20, 
#                             fill = None, outline = 'blue')

# def drawFlyEnemy(app, canvas):
#     fX, fY = app.flyEnemy.getLocation()
#     fW, fH = app.flyEnemy.getSize()
#     fColor = app.flyEnemy.getColor()
#     # this rectangle is collision box
#     canvas.create_rectangle(fX, fY, fX + fW, fY + fH, 
#                             fill = None, outline = fColor)

def drawLeftSlash(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    nfX += nfW/2
    canvas.create_rectangle(nfX, nfY - 15, nfX - 60, nfY + nfH + 15, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY - 7, nfX - 85, nfY + nfH + 7, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY, nfX - 100, nfY + nfH, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY + 7, nfX - 112, nfY + nfH - 7, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY + 15, nfX - 120, nfY + nfH - 15, 
                            fill = None, outline = 'blue')

def drawRightSlash(app, canvas):
    nfX, nfY = app.nightFury.getLocation()
    nfW, nfH = app.nightFury.getSize()
    nfX += nfW/2
    canvas.create_rectangle(nfX, nfY - 15, nfX + 60, nfY + nfH + 15, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY - 7, nfX + 85, nfY + nfH + 7, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY, nfX + 100, nfY + nfH, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY + 7, nfX + 112, nfY + nfH - 7, 
                            fill = None, outline = 'blue')
    canvas.create_rectangle(nfX, nfY + 15, nfX + 120, nfY + nfH - 15, 
                            fill = None, outline = 'blue')