from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.game import Game
from game_simulator.game.attacker import Attacker

#Balance 2
"""Simulation algorithm to evaluate the impact of the number of attackers on the number of games won by the attackers
"""
nb_rs = 4
hp_unit_cost=30
nb_def=1000
nb_turns = 100

hp_proportion = 0.5
defenders1 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=0, name="Def5")

hp_proportion = 0.8
defenders2 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=nb_def, name="Def8")

hp_proportion = 0.2
defenders3 = create_n_defenders(nb_def, nb_rs, hp_proportion, hp_unit_cost, offset=nb_def+nb_def, name="Def2")

defs = defenders1 + defenders2 + defenders3
attack_proba=0.75
atks = []
res = []
step=100
for i in range(step, 5000, step):
  atk = create_n_attackers(step, 0.75, offset=i)
  atks += atk
  players = defs + atks
  nb_games_won_by_atk = 0
  for j in range(50):
    game = Game(players, nb_turns)
    game.play()
    if game.get_winner_type() == "Attacker":
      nb_games_won_by_atk +=1
  res.append((i,nb_games_won_by_atk))
#the result is a list of tuples (nb of attackers, number of games won by the attackers)
print(res)