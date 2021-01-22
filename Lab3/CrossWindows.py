from pyglet.gl import *
import math
import numpy as np
from numpy.linalg import norm
from pyglet.window import key
import time
from CrossParticle import CrossParticle
from CrossSystem import CrossSystem
import copy


class Window(pyglet.window.Window):
    global pyglet
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update,1/60)
        particle = CrossParticle([-40,50],[630,300])
        system = CrossSystem(particle,20)
        self.system = system
        self.player = [250,0]
        self.score = 0
        self.highscore = 0
        self.score_label = pyglet.text.Label(text="Score:0 Highscore:0", x=10, y=10)
        self.player_image = pyglet.image.load("Kokos.jpg")

    def update(self,dt):
        self.system.update(dt)
        self.update_player()
        self.checkForCollision()



    def on_draw(self):
        self.clear()
        glPushMatrix()
        glColor3f(1,1,1)
        self.system.draw()
        player =pyglet.sprite.Sprite(self.player_image,x=self.player[0],y=self.player[1])
        player.draw()
        glPopMatrix()
        self.score_label.draw()

    def checkForCollision(self):
        all = self.system.particles
        for particle in all:
            if self.checkCollision(particle.position,self.player):
                self.player[1]=0
                self.score = 0
                self.score_label.text = "Score: %s Highscore: %s" % (self.score, self.highscore)


    def update_player(self):
        if self.keys[pyglet.window.key.LEFT] and not self.player[0] < 0:
            self.player[0] -= 2.5
        elif self.keys[pyglet.window.key.RIGHT] and not self.player[0] > 480:
            self.player[0] += 2.5
        elif self.keys[pyglet.window.key.UP] and not self.player[1]>=700:
            self.player[1]+=2.5
        elif self.keys[pyglet.window.key.UP] and self.player[1]==700:
            self.player[1]=0
            self.score+=1
            if self.highscore<self.score:
                self.highscore = self.score
            self.score_label.text = "Score: %s Highscore: %s" % (self.score, self.highscore)
        elif self.keys[pyglet.window.key.DOWN] and not self.player[1]<0:
            self.player[1]-=2.5

    def checkCollision(self,particle,player):
        return ((particle[0]+20)-(player[0]+20))**2 +((particle[1]+20)-(player[1]+20))**2 < 40**2

if __name__ == '__main__':

    window = Window(width=500,height=750)
    pyglet.app.run()