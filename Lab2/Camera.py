import numpy as np

class Camera:
    def __init__(self,position = (0,0,-1),lookAt = (0,0,0)):
        self.position = list(position)
        self.lookAt = list(lookAt)

    def get_position(self):
        return self.position

    def get_lookAt(self):
        return self.lookAt

