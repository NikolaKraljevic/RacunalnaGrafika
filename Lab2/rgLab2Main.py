from pyglet.gl import *
import math
import numpy as np
from numpy.linalg import norm
from pyglet.window import key
import time
import cProfile
from Camera import Camera
from pyrr import Vector3
from Particle import Particle
from System import System
import copy

class Window(pyglet.window.Window):
    global pyglet
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        start = time.time()
        self.POV = 60
        self.source = [0,0,0]
        pyglet.clock.schedule_interval(self.update,1.0/60.0)
        self.camera = Camera((0,1000,1000))

        starText = pyglet.image.load('light_01.png').get_texture()
        # Parametri [0] pomak za x koordinate [1] pomak za y koordinate [2] minimalna i maksimalna brzina za x i z [3] početna y brzina [4] maksimalna razlika u y brzini [5] koliko će živjeti

        particlesWorld =  Particle(Vector3([0, -1, -5]), gravity=Vector3([0, 5000, 0]), parameters=[
                                         0, 0, 100., 50., 100., 3.],        colorSystem = [[0.8, 0.1, 0.1], [0, 1, 1]], sizeSystem = [[500, 600], [50, 800]])

        starParticleSystem = System(particlesWorld, starText, 150)
        self.system = starParticleSystem

    def update(self,dt):
        self.system.update(dt)
        if len(self.system.particles) == 0:
            del self.system
    def drawOrigin(self):
        glPushMatrix()

        glPopMatrix()

    def on_draw(self):
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT)
        self.drawOrigin()
        camera_pos = self.camera.get_position()
        lookAt = self.camera.get_lookAt()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.POV,2,0.05,10000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(camera_pos[0],camera_pos[1],camera_pos[2],lookAt[0],lookAt[1],lookAt[2],0.0,1.0,0.0)
        glPushMatrix()
        self.system.draw(camera_pos)
        glPopMatrix()

        glFlush()

if __name__ == '__main__':

    window = Window(width=1000,height=500)
    pyglet.app.run()