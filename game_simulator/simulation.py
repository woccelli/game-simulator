from game.attacker import create_n_attackers
from game.defender import create_n_defenders
from game.game import Game
from theory.def_theory import find_best_defender_configuration

n_rs = 2
delta_max = 30
bigdelta = 70
mu = 250
alpha = 1000
n_def = 200
n_att = 100
n_turns = 100
def_config = find_best_defender_configuration(n_rs,delta_max,bigdelta,mu, alpha)
hp_proportion = def_config['theta']
hp_cost = def_config['delta_hp']
defenders = create_n_defenders(n_def, n_rs, hp_proportion)
attackers = create_n_attackers(n_att, 0.75, n_def)
players = defenders + attackers
game = Game(players, n_turns)
game.play()
game.export_game_results()
