from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.game import Game
from game_simulator.theory.def_theory import find_best_defender_configuration

delta_max = 30
bigdelta = 1000
mu = 250
alpha = 1000

nb_def=100
nb_att = 50
nb_rs = 5
attack_proba = 1
nb_games = 1000
nb_turns = 500
def_config = find_best_defender_configuration(nb_rs,delta_max,bigdelta,mu, alpha)
hp_proportion = def_config['theta']
hp_cost = def_config['delta_hp']

theory_defenders = create_n_defenders(nb_def,nb_rs,hp_proportion, hp_cost,name='theory')

attackers = create_n_attackers(nb_att, attack_probability=attack_proba,offset = nb_def)
players = theory_defenders + attackers

from basic1 import count_average_nb_of_turns
print("Average number of turns for", nb_def, "defenders (nb_rs=",nb_rs,",hp_proportion=", hp_proportion,") and", nb_att, "attackers (attack_proba=", attack_proba,"), for", nb_games, "games played, is :")
print(count_average_nb_of_turns(players,nb_games,nb_turns))

from basic2 import count_nb_of_games_won
count_nb_of_games_won(players,nb_games,nb_turns)
