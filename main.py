import character
import team
import battle
import pygame
import numpy as np


class MainRun:
    def __init__(self, display_width_, display_height_, stopped_=False):
        self.dw = display_width_
        self.dh = display_height_
        self.stopped = stopped_
        self.main()

    def show_char(self, x, y):
        window.blit(tusk_icon, (x, y))

    def main(self):

        while self.stopped == False:

            window.fill((255, 255, 255))

            # positioning of characters
            for char in sim.team1.charlist + sim.team2.charlist:
                charX = int(char.position[0])
                charY = int(char.position[1])
                self.show_char(charX, charY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopped = True


            pygame.display.update()







if __name__ == '__main__':

    #### create teams ####

    tmp1 = []
    tmp2 = []
    teamsize = 1

    team1 = team.Team("Team1", tmp1)
    team2 = team.Team("Team2", tmp2)

    #### create new battle ####
    sim = battle.Battle(200, 0, team1, team2, 0.5, 10, 10)

    #### initialize pygame ####
    pygame.init()

    # Window settings
    width = sim.battle_field.width * 100
    height = sim.battle_field.height * 100
    screen_size = (width, height)
    window = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption("Auto Chess Simulator")
    chess_icon = pygame.image.load('Chessicon.png')
    pygame.display.set_icon(chess_icon)

    # Clock
    windowclock = pygame.time.Clock()

    # image files
    tusk_icon = pygame.image.load('Tuskicon.png')

    #### Create characters ####

    for i in range(teamsize):
        tmp1.append(
            character.Character("Tusk1_" + str(i), 100, 0, np.array([100, 100]), 1, 1, None, None, 100, 2, 1,
                                None, 1))
        tmp2.append(
            character.Character("Tusk2_" + str(i), 100, 0, np.array([500, 500]), 1, 1, None, None, 10, 2, 1,
                                None,
                                1))

    #### Set up game ####
    MainRun(width, height)



    #positioning of characters


    while sim.active:
        sim.update()
