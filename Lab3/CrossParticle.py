import sys
import time
import math
from pyglet.gl import *
from random import *
import numpy as np
import random


class CrossParticle:
    def __init__(self,position,parameters):
        self.position = position.copy()
        self.velocity = [0,0]
        CrveniAuto = pyglet.image.load('CrveniAuto.jpg')
        PolicijskiAuto = pyglet.image.load('PolicijskiAuto.jpg')
        RoziAuto = pyglet.image.load('RoziAuto.jpg')
        self.car_images = [CrveniAuto,PolicijskiAuto,RoziAuto]
        self.parameters = parameters
        self.image = CrveniAuto
        self.at = 0

    def randomize(self):
        self.position[0] += 0
        self.position[1] += uniform(0,self.parameters[0])
        self.velocity = [uniform(40,self.parameters[1]),0]
        self.image = self.car_images[randint(0,2)]

    def update(self,dt):
        self.position[0] +=self.velocity[0]*dt
        self.position[1]+=self.velocity[1]*dt
        self.at+=dt