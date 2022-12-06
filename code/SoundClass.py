import subprocess, threading, time
from cmu_112_graphics import *

class Sound(object):
    def __init__(self, path):
        self.path = path
        self.process = None
        self.loop = False

    def isPlaying(self):
        return (self.process is not None)

    def checkProcess(self):
        # This method is run inside a separate thread
        # so the main thread does not hang while this runs.
        while self.process is not None:
            if (self.process.poll() is not None):
                self.process = None
            else:
                time.sleep(0.2)
        if self.loop:
            self.start(loop=True)

    def start(self, loop=False):
        self.stop()
        self.loop = loop
        self.process = subprocess.Popen(['afplay', self.path])  
        threading.Thread(target=self.checkProcess).start()

    def stop(self):
        process = self.process
        self.loop = False
        self.process = None
        if (process is not None):
            try: process.kill()
            except: pass

def appStarted(app):
    app.sound = Sound('button.mp3')

def appStopped(app):
    app.sound.stop()

def keyPressed(app, event):
    if (event.key == 's'):
        if app.sound.isPlaying(): app.sound.stop()
        else: app.sound.start()
    elif (event.key == 'l'):
        app.sound.start(loop=True)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2-60,
                       text=f'{app.sound.path} (loop = {app.sound.loop})',
                       font='Arial 30 bold', fill='black')
    canvas.create_text(app.width/2, app.height/2-20,
                       text=f'sound is playing = {app.sound.isPlaying()}',
                       font='Arial 30 bold', fill='black')
    canvas.create_text(app.width/2, app.height/2+20,
                       text='Press s to start/stop sound',
                       font='Arial 30 bold', fill='black')
    canvas.create_text(app.width/2, app.height/2+60,
                       text='Press l to loop sound',
                       font='Arial 30 bold', fill='black')

runApp(width=600, height=200)
