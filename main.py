import character
import team
import battle
import numpy as np

if __name__ == '__main__':
    tmp1 = []
    tmp2 = []
    teamsize = 6

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

    game = battle.Battle(20, 0, team1, team2, 0.5, 10, 10)

    while game.active:
        game.update()
