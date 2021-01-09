import sys, time, math
from pyglet.gl import *
from random import *
from numpy.linalg import norm
from pyrr import Vector3
import copy
import numpy as np

class CrossSystem:
    def __init__(self,particle,num=10):
        self.particles = []
        self.particle = particle
        self.addParticles(num)

    def addParticles(self,num):
        for i in range(num):
            p = copy.deepcopy(self.particle)
            p.randomize()
            self.particles.append(p)

    def update(self,dt):
        for p in self.particles:
            p.update(dt)
        t= time.time()
        for i in range(len(self.particles)-1,-1,-1):
            if (self.particles[i].position[0]>470):

                del self.particles[i]
                self.addParticles(1)

    def draw(self):
        glPushMatrix()
        for p in self.particles:
            position = p.position
            glBegin(GL_QUADS)
            glVertex2f(0+position[0],0+position[1])
            glVertex2f(0+position[0],20+position[1])
            glVertex2f(20+position[0],20+position[1])
            glVertex2f(20+position[0],0+position[1])
            glEnd()
        glPopMatrix()

