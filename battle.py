import character
import team
import battlefield
import numpy as np
import pdb
import sys


class Battle:
    def __init__(self, max_time_, time_, team1_, team2_, timestep_, width_, height_, screen_, active_=True):
        self.max_time = max_time_
        self.time = time_
        self.team1 = team1_
        self.team2 = team2_
        self.timestep = timestep_
        self.battle_field = battlefield.Battlefield(width_, height_)
        self.screen = screen_
        self.active = active_

    def update(self):

        for character in self.team1.charlist + self.team2.charlist:
            if character.alive == True:
                print("\nCurrent time " + str(self.time))
                print(repr(character))
                self.team1.update_state()
                self.team2.update_state()
                if self.time >= self.max_time or self.team1.alive == False or self.team2.alive == False:
                    self.end_battle()
                    break

                self.update_target(character)
                if character.target is None:
                    mv_target = self.battle_field.center
                else:
                    mv_target = character.target.position
                character.update_mv_dir(mv_target)
                if character.target is None:
                    character.update_position(self.timestep)
                self.screen.blit(character.team.icon, (character.position[0], character.position[1]))
                character.update_atk_cd(self.timestep) #calls hit --> calls update_alive --> call update_states

                character.update_dmg(self.timestep)
                character.update_heatlh(self.timestep)
                character.update_mana(self.timestep)
                character.update_spell_cd(self.timestep)

        self.time += self.timestep

    def get_enemy_team(self, team):
        if team is self.team1:
            return self.team2
        else:
            return self.team1

    def update_target(self, character):

        enemy_team = self.get_enemy_team(character.team)
        enemy_distances = np.array(
            [np.linalg.norm(enemy.position - character.position) for enemy in enemy_team.living_chars])

        closest_enemy_index = np.argmin(enemy_distances)

        if enemy_distances[closest_enemy_index] <= character.atk_range:
            character.target = enemy_team.living_chars[closest_enemy_index]
            print("\n", character.name, " updated target to: ", enemy_team.living_chars[closest_enemy_index].name)
        else:
            character.target = None

    def end_battle(self):
        self.active = False
        if self.team1.alive == True and self.team2.alive == False:
            print(self.team1.name, " has won.")
        elif self.team2.alive == True and self.team1.alive == False:
            print(self.team2.name, " has won.")
        else:
            print("Game draw.")
