import sys, time, math
from pyglet.gl import *
from random import *
from numpy.linalg import norm
from pyrr import Vector3
import copy
import numpy as np


class System:
    def __init__(self,particle,texture,num=10,size = 20):
        self.particles = []
        self.particle = particle
        self.texture = texture
        self.size = size
        self.addParticles(num)


    def addParticles(self,num):
        for i in range(0,num):
            p = copy.deepcopy(self.particle)
            p.randomize()
            self.particles.append(p)

    def update(self,dt):
        for p in self.particles:
            p.update(dt)
        t = time.time()
        for i in range(len(self.particles)-1,-1,-1):
            if (self.particles[i].lifeTime <= t):
                del self.particles[i]
                self.addParticles(1)

    def draw(self,cameraPosition):
        glEnable(self.texture.target)
        glBindTexture(self.texture.target,self.texture.id)
        glEnable(GL_BLEND)
        glBlendFunc(GL_ONE,GL_ONE)
        glPushMatrix()

        for p in self.particles:
            c = p.currentColor
            glColor3f(c[0],c[1],c[2])

            matrix = (GLfloat * 16)()
            glGetFloatv(GL_MODELVIEW_MATRIX,matrix)

            RightCam = np.array([matrix[2],matrix[6],matrix[10]])
            UpCam = np.array([0,1,0])
            size = p.currentSize
            RightCam = np.cross(RightCam,UpCam)

            v1 = p.position + RightCam * 0.5 * size[0] + UpCam * -0.5 * size[1]
            v2 = p.position + RightCam * 0.5 * size[0] + UpCam * 0.5 * size[1]
            v3 = p.position + RightCam * -0.5 * size[0] + UpCam * -0.5 * size[1]
            v4 = p.position + RightCam * -0.5 * size[0] + UpCam * 0.5 * size[1]

            glBegin(GL_QUADS)
            glTexCoord2f(0, 0)
            glVertex3f(v3[0], v3[1], v3[2])
            glTexCoord2f(1, 0)
            glVertex3f(v4[0], v4[1], v4[2])
            glTexCoord2f(1, 1)
            glVertex3f(v2[0], v2[1], v2[2])
            glTexCoord2f(0, 1)
            glVertex3f(v1[0], v1[1], v1[2])

            glEnd()
        glDisable(GL_BLEND)
        glPopMatrix()



