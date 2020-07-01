import character
import numpy as np


class Team:
    def __init__(self, name_, charlist_, alive_=True):
        self.name = name_
        self.charlist = charlist_
        self.living_chars = [char for char in self.charlist if char.alive == True]
        self.alive = alive_
        for char in self.charlist:
            char.team = self

    def update_state(self):

        statelist = [char.alive for char in self.charlist]
        if np.sum(statelist) == 0:
            self.alive = False
        self.living_chars = [char for char in self.charlist if char.alive == True]



