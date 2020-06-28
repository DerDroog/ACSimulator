import character
import numpy as np
import pdb
import sys


class Battle:
    def __init__(self, max_time_, time_, team1_, team2_, timestep_, active_=True):
        self.max_time = max_time_
        self.time = time_
        self.team1 = team1_
        self.team2 = team2_
        self.timestep = timestep_
        self.active = active_

    def update(self):
        print("\nCurrent time: ", self.time, "\n")
        for character in self.team1.charlist + self.team2.charlist:
            if character.alive == True:
                enemy_team = self.get_enemy_team(character.team)
                enemies_alive = [char for char in enemy_team.charlist if char.alive == True]
                self.update_target(character, enemies_alive)
                character.update_atk_cd(self.timestep)
                character.update_dmg(self.timestep)
                character.update_heatlh(self.timestep)
                character.update_mana(self.timestep)
                character.update_position(self.timestep)
                character.update_spell_cd(self.timestep)

        for character in self.team1.charlist + self.team2.charlist:
            character.update_alive()
        self.team1.update_state()
        self.team2.update_state()
        self.time += self.timestep

    def get_enemy_team(self, team):
        if team is self.team1:
            return self.team2
        else:
            return self.team1

    def update_target(self, character, enemies_alive):
        character.target = enemies_alive[0]

    def end_battle(self):
        self.active = False
        if self.team1.alive == True and self.team2.alive == False:
            print(self.team1.name, " has won.")
        elif self.team2.alive == True and self.team1.alive == False:
            print(self.team2.name, " has won.")
        else:
            print("Game draw.")
