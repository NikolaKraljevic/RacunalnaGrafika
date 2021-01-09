import sys
import time
import math
from pyglet.gl import *
from random import *
import numpy as np


class CrossParticle:
    def __init__(self,position,parameters):
        self.position = position.copy()
        self.velocity = [0,0]

        self.parameters = parameters
        self.at = 0

    def randomize(self):
        self.position[0] += 0
        self.position[1] += uniform(0,self.parameters[0])
        self.velocity = [uniform(40,self.parameters[1]),0]


    def update(self,dt):
        self.position[0] +=self.velocity[0]*dt
        self.position[1]+=self.velocity[1]*dt
        self.at+=dt