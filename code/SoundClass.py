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