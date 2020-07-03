import character
import team
import battle
import pygame
import numpy as np
import time


class MainRun:
    def __init__(self, display_width_, display_height_, stopped_=False):
        self.dw = display_width_
        self.dh = display_height_
        self.stopped = stopped_




    def main(self):

        while sim.active == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopped = True

            window.fill((0, 255, 255))

            # quit condition (press x)

            sim.update()
            pygame.display.update()
            time.sleep(0.1)


if __name__ == '__main__':

    #### initialize pygame ####
    pygame.init()

    # image files
    tusk_icon = pygame.image.load('Tuskicon.png')
    goblin_icon = pygame.image.load('goblin.png')

    #### create teams ####

    tmp1 = []
    tmp2 = []
    teamsize = 3

    team_1 = team.Team("Team1", tmp1, tusk_icon)
    team_2 = team.Team("Team2", tmp2, goblin_icon)


    # Window settings
    width = 1000
    height = 1000
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Auto Chess Simulator")
    chess_icon = pygame.image.load('Chessicon.png')
    pygame.display.set_icon(chess_icon)

    # Clock
    windowclock = pygame.time.Clock()




    #### Create characters ####
    # name_, health_, mana_, position_, max_atk_cd_, atk_cd_, max_spell_cd_, spell_cd_, atk_, armor_,
    # mv_speed_, mv_dir_, atk_range_, team_=None, target_=None, alive_=True)
    health_1 = 100
    health_2 = 100
    mana1 = 0
    mana2 = 0
    max_atk_cd_1 = 3
    max_atk_cd_2 = 3
    atk_cd_1 = 3
    atk_cd_2 = 3
    max_spell_cd_1 = 0
    max_spell_cd_2 = 0
    spell_cd_1 = 0
    spell_cd_2 = 0
    atk_1 = 10
    atk_2 = 20
    armor_1 = 2
    armor_2 = 2
    mv_speed_1 = 10
    mv_speed_2 = 10
    mv_dir_both = None
    atk_range_1 = 100
    atk_range_2 = 100

    for i in range(teamsize):
        team_1.charlist.append(
            character.Character("Tusk1_" + str(i), health_1, mana1, np.array([width * i / teamsize, 0]), max_atk_cd_1,
                                atk_cd_1, max_spell_cd_1, spell_cd_1, atk_1, armor_1, mv_speed_1, mv_dir_both,
                                atk_range_1, team_1))
        team_2.charlist.append(
            character.Character("Tusk2_" + str(i), health_2, mana1, np.array([width * i / teamsize, 300]), max_atk_cd_2,
                                atk_cd_2, max_spell_cd_2, spell_cd_2, atk_2, armor_2, mv_speed_2, mv_dir_both,
                                atk_range_2, team_2))

    #### Set up game ####
    ACRun = MainRun(width, height)

    #### create new battle ####
    # class Battle:
    # (max_time_, time_, team1_, team2_, timestep_, width_, height_, active_=True)
    sim = battle.Battle(200, 0, team_1, team_2, 0.5, width, height, window)

    ACRun.main()

    # while sim.active:
    #    sim.update()
