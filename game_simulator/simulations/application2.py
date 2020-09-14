from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.game import Game
from game_simulator.theory.def_theory import find_best_defender_configuration

delta_max = 50
bigdelta = 1000
mu = 500
alpha = 1000 #1500

nb_def=1000
nb_att = 1000
nb_rs = 5
nb_games = 100
nb_turns = 200
def_config = find_best_defender_configuration(nb_rs,delta_max,bigdelta,mu, alpha)

hp_proportion = def_config['theta']
hp_cost = def_config['delta_hp']
print("theory hp_proportion=", hp_proportion, "hp_cost=", hp_cost)
defs1 = create_n_defenders(nb_def,nb_rs,hp_proportion=hp_proportion, hp_unit_cost=hp_cost, name="def_theory")

hp_proportion2 = 0.2
defs2 = create_n_defenders(nb_def,nb_rs,hp_proportion=hp_proportion2, hp_unit_cost=30, offset=nb_def, name="def2")

hp_proportion3 = 0.7
defs3 = create_n_defenders(nb_def,nb_rs,hp_proportion=hp_proportion3, hp_unit_cost=30, offset=nb_def*2, name="def7")

hp_proportion4 = 0.9
defs4 = create_n_defenders(nb_def,nb_rs,hp_proportion=hp_proportion4, hp_unit_cost=30, offset=nb_def*3, name="def9")

"""
atks1 = create_n_attackers(nb_att,attack_proba,offset =nb_def*2, name="atk1")
players = defs1 + atks1 + defs2 + defs3
g = Game(players,nb_turns)
g.play()
g.export_game_results_name("game_results_name.csv")
from basic2 import count_nb_of_games_won
count_nb_of_games_won(players,nb_games,nb_turns)
"""

defs = defs1 + defs2 + defs3 + defs4
atks = []
res = []
step=300
for i in range(step, 4200, step):
  atk = create_n_attackers(step, 0.8, offset=i)
  atks += atk
  players = defs + atks
  nb_games_won_by_atk = 0
  nb_by_name = {}
  for j in range(nb_games):
    game = Game(players, nb_turns)
    game.play()
    winner_name = game.get_winner_name()
    if winner_name in nb_by_name:
      nb_by_name[winner_name] += 1
    else:
      nb_by_name[winner_name] = 1
  res.append((i,nb_by_name))
print(res)

"""
Number of games played:  1000
Number of games with a total winner:  894
Defenders wins:  392 , Attackers wins:  502
Most represented populations at the last turn: {'atk1': 507, 'def_theory': 113, 'def+': 380}
"""