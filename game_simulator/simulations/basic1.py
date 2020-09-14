from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.game import Game

#Basic-1
def count_average_nb_of_turns(players, nb_games, nb_turns):
  """Simulation algorithm used to count the average number of turns played in a game.
  The number of turns of a game is either :
    - The maximum number of turns set when creating the game if both types of player survive during all previous turns
    - The number of the first turn having the population of one its type of players equal to 0
  """
  turns = 0
  for i in range(nb_games):
    game = Game(players, nb_turns)
    game.play()
    turns += game.get_nb_turns_played()
  return turns/nb_games

"""
nb_def=1000
nb_att = 500
nb_rs = 10
hp_proportion = 0
attack_proba = 1
nb_games = 10000
nb_turns = 100
defenders = create_n_defenders(nb_def, nb_rs, hp_proportion)
attackers = create_n_attackers(nb_att, attack_proba, nb_def)
players = defenders + attackers

print("Average number of turns for", nb_def, "defenders (nb_rs=",nb_rs,",hp_proportion=", hp_proportion,") and", nb_att, "attackers (attack_proba=", attack_proba,"), for", nb_games, "games played, is :")
print(count_average_nb_of_turns(players,nb_games,nb_turns))
"""