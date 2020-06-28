import character
import team
import battle
import numpy as np

if __name__ == '__main__':
    tusk1 = character.Character("Tusk1", 100, 0, np.array([0,5]), 1, 1, None, None, 20, 1, 1, None, 1)
    tusk2 = character.Character("Tusk2", 100, 0, np.array([10, 5]), 2, 2, None, None, 10, 1, 1, None, 1)
    team1 = team.Team("Team1", [tusk1])
    team2 = team.Team("Team2", [tusk2])
    game = battle.Battle(20, 0, team1, team2, 0.3, 10, 10)

    while game.active:
        game.update()
        if game.time >= game.max_time or game.team1.alive == False or game.team2.alive == False:
            game.end_battle()
