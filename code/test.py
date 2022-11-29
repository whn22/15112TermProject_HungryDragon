# # Note: Tkinter uses event.keysym for some keys, and event.char
# # for others, and it can be confusing how to use these properly.
# # Instead, cmu_112_graphics replaces both of these with event.key,
# # which simply works as expected in all cases.

# from cmu_112_graphics import *
# from ControlSetClass import ControlSet
# from ButtonClass import Button

# controlSettings = ControlSet('Left', 'Right', 'x', 'z')

# def appStarted(app):
#     app.settings = controlSettings
#     app.inputKey = None
#     menu = Button(10, 10, 60, 20, 
#                         'menu', 'aquamarine', 'menu', 10)
#     app.menu = menu
#     app.mouseX, app.mouseY = (-1, -1)
#     leftB = Button(app.width/2 - 300, app.height/10 * 3, 200, 40, 
#                         'left', 'aquamarine', 'set left', 20)
#     rightB = Button(app.width/2 - 300, app.height/10 * 4, 200, 40, 
#                         'right', 'aquamarine', 'set right', 20)
#     jumpB = Button(app.width/2 - 300, app.height/10 * 5, 200, 40, 
#                         'jump', 'aquamarine', 'set jump', 20)
#     dashB = Button(app.width/2 - 300, app.height/10 * 6, 200, 40, 
#                         'dash', 'aquamarine', 'set dash', 20)
#     app.menuButtons = {leftB, rightB, jumpB, dashB}
#     app.menuOn = False

# def openMenu(app):
#     app.menuOn = True

# def mouseMoved(app, event):
#     app.mouseX, app.mouseY = (event.x, event.y)

# def keyPressed(app, event):
#     app.inputKey = event.key
#     if app.inputKey == 'q':
#         app.menuOn = False

# def mousePressed(app, event):
#     if app.menuOn == False:
#         app.menu.mouseClicked(event.x, event.y, openMenu, app)
#     else:
#         for button in app.menuButtons:
#             button.mouseClicked(event.x, event.y, 
#                                 app.settings.resetKey, (app.inputKey, button))

# def timerFired(app):
#     if app.menuOn == False:
#         app.menu.checkMouseOn(app.mouseX, app.mouseY)
#     else:
#         for button in app.menuButtons:
#             button.checkMouseOn(app.mouseX, app.mouseY)

# def redrawAll(app, canvas):
#     canvas.create_rectangle(0, 0, app.width, app.height, 
#                             fill = 'black', outline = None)
#     app.menu.drawButton(canvas)
#     if app.menuOn == True:
#         app.settings.drawMenu(app, canvas)

# runApp(width=1000, height=600)

# from cmu_112_graphics import *
# # import time # sleep()

# # from NightFuryClass import NightFury
# # from TerrainClass import Terrain
# from ControlSetClass import ControlSet
# from ButtonClass import Button
# from BlockClass import Block
# from NightFuryClass import NightFury
# from EnemyClass import Enemy, FlyEnemy, WalkEnemy

# from GenerateLevel import Level1

# nightFury1 = NightFury(0, 590 - 50, 20, 50, 'blueviolet', 5, 13, 0.7, 20, 10, 
#                        100, 100, 100)
# level1 = Level1(3, 5)

# def appStarted(app):
#     level1.createTerrain(app)
#     app.terrain1 = level1.terrain
#     pass

# # Helper functions for timerFired.
# def timerFired(app):
#     pass

# # helper functions for keyPressed
# def keyPressed(app, event):
#     pass

# # helper functions for redraw All
# def redrawAll(app, canvas):
#     canvas.create_rectangle(0, 0, app.width, app.height, 
#                             fill = 'black', outline = None)
#     Block.drawBlockSet(app.terrain1, canvas)
#     pass

# runApp(width = 1000, height = 600)

l = list(range(1, 101))
print(l)
