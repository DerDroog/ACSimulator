import character
import team
import battle
import numpy

if __name__ == '__main__':

    tusk1 = character.Character("Tusk1", 100, 0, None, 1, 1, None, None, 20, 1)
    tusk2 = character.Character("Tusk2", 100, 0, None, 2, 2, None, None, 10, 1)
    team1 = team.Team("Team1", [tusk1])
    team2 = team.Team("Team2", [tusk2])
    game = battle.Battle(20, 0, team1, team2, 0.5)

    while game.active:
        game.update()
        if game.time >= game.max_time or game.team1.alive == False or game.team2.alive == False:
            game.end_battle()
