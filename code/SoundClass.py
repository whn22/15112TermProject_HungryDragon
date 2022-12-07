# This demos playing sounds using Pygame:

from cmu_112_graphics import *
import pygame

class Sound(object):
    def __init__(self, path):
        self.playing = False
        self.path = path
        self.loops = 1
        self.sound = pygame.mixer.Sound(path)

    # Returns True if the sound is currently playing
    def play(self):
        self.sound.play()

    def playSound(self):
        if self.playing:
            self.sound.stop()
        else:
            self.sound.play()
        self.playing = not self.playing

class BackGroundSound(object):
    def __init__(self, path):
        self.path = path
        self.loops = 1
        pygame.mixer.music.load(path)

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=1):
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        pygame.mixer.music.stop()


# def appStarted(app):
#     pygame.mixer.init()
#     app.sound = Sound("sword_1.wav")

# def appStopped(app):
#     app.sound.stop()

# def keyPressed(app, event):
#     if (event.key == 's'):
#         if app.sound.isPlaying(): app.sound.stop()
#         else: app.sound.start()
#     elif (event.key == 'l'):
#         app.sound.start(loops=-1)
#     elif event.key.isdigit():
#         app.sound.start(loops=int(event.key))

# def timerFired(app):
#     pass

# def redrawAll(app, canvas):
#     canvas.create_text(app.width/2, app.height/2-60,
#                        text=f'{app.sound.path} (loops = {app.sound.loops})',
#                        font='Arial 30 bold', fill='black')
#     canvas.create_text(app.width/2, app.height/2-20,
#                        text=f'sound is playing = {app.sound.isPlaying()}',
#                        font='Arial 30 bold', fill='black')
#     canvas.create_text(app.width/2, app.height/2+20,
#                        text='Press s to start/stop sound',
#                        font='Arial 30 bold', fill='black')
#     canvas.create_text(app.width/2, app.height/2+60,
#                        text='Press l to loop sound',
#                        font='Arial 30 bold', fill='black')

# runApp(width=600, height=200)