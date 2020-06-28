import numpy as np

class Battlefield:
    def __init__(self, width_, height_):
        self.width = width_
        self.height = height_
        self.center = np.array([width_/2, height_/2])

    