import sys
import time
import math
from pyglet.gl import *
from random import *
from pyrr import Vector3
import numpy as np

#Parametri [0] pomak za x koordinate [1] pomak za y koordinate [2] minimalna i maksimalna brzina za x i z [3] početna y brzina [4] maksimalna razlika u y brzini [5] koliko će živjeti

class Particle:
    def __init__(self,position,gravity,parameters,colorSystem,sizeSystem):
        self.position = position.copy()
        self.gravity = gravity.copy()
        self.velocity = Vector3([0,0,0])
        self.lifeTime = time.time()+1
        self.parameters = parameters
        self.colorSystem = colorSystem
        self.sizeSystem = sizeSystem
        self.currentSize = sizeSystem[0]
        self.currentColor = colorSystem[0]

        self.at = 0

    def randomize(self):
        self.position[0]+= gauss(0,self.parameters[0])
        self.position[1]+= uniform(0, self.parameters[1])
        self.velocity = Vector3([uniform((-self.parameters[2]),self.parameters[2]),
                                self.parameters[3] + uniform(-self.parameters[4],self.parameters[4]),
                                uniform((-self.parameters[2]), self.parameters[2])] )
        self.lifeTime = time.time() +abs(gauss(0.0,self.parameters[5]))


    def update(self,dt):

        self.position += self.velocity * dt
        self.velocity += self.gravity * dt
        color0 = linear_interpolation(self.colorSystem[0][0],self.colorSystem[1][0],self.at)
        color1 = linear_interpolation(self.colorSystem[0][1],self.colorSystem[1][1],self.at)
        color2 = linear_interpolation(self.colorSystem[0][2], self.colorSystem[1][2], self.at)
        self.currentColor = [color0,color1,color2]
        size0 = linear_interpolation(self.sizeSystem[0][0],self.sizeSystem[1][0],self.at)
        size1 = linear_interpolation(self.sizeSystem[0][1],self.sizeSystem[1][1],self.at)
        self.currentSize = [size0,size1]

        self.at+= dt

def linear_interpolation(a,b,f):
    return a + f*(b-a)