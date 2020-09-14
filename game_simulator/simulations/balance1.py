from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
#Balance 1
"""Simulation algorithm to count the number of games won by each player when there are several variations of a same type of player
"""

nb_rs = 4
hp_unit_cost=30
nb_def=1000
nb_turns = 100
nb_games = 1000
nb_att = 200
attack_proba=1

hp_proportion = 0.5
defenders1 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=0, name="Def5")

hp_proportion = 0.8
defenders2 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=nb_def, name="Def8")

hp_proportion = 0.2
defenders3 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=nb_def+nb_def, name="Def2")

defs = defenders1 + defenders2 + defenders3

attackers = create_n_attackers(nb_att, attack_proba, nb_def*3)

players = defs + attackers

from basic2 import count_nb_of_games_won
count_nb_of_games_won(players,nb_games,nb_turns)
