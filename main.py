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

    def main(self):

        while self.stopped == False:
            window.fill((255, 255, 255))

            # events here

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopped = True

            pygame.display.update()




if __name__ == '__main__':

    tmp1 = []
    tmp2 = []
    teamsize = 10

    #create teams
    for i in range(teamsize):
        tmp1.append(
            character.Character("Tusk1_" + str(i), 100, 0, np.array([0, i / teamsize]), 1, 1, None, None, 100, 2, 1,
                                None, 1))
        tmp2.append(
            character.Character("Tusk2_" + str(i), 100, 0, np.array([10, i / teamsize]), 1, 1, None, None, 10, 2, 1,
                                None,
                                1))
    team1 = team.Team("Team1", tmp1)
    team2 = team.Team("Team2", tmp2)

    # create new battle
    sim = battle.Battle(200, 0, team1, team2, 0.5, 10, 10)

    #Set up game


    # initialize pygame
    pygame.init()
    # Window settings
    window = pygame.display.set_mode((sim.battle_field.width*100, sim.battle_field.height*100))
    pygame.display.set_caption("Auto Chess Simulator")
    pygame.display.flip()

    # Clock
    windowclock = pygame.time.Clock()

    # image files
    # image = pygame.image.load("foo.png")
    MainRun(sim.battle_field.width, sim.battle_field.height)


    while sim.active:
        sim.update()
