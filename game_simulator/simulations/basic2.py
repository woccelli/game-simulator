from game_simulator.game.attacker import create_n_attackers
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.game import Game

#Basic-2
def count_nb_of_games_won(players, nb_games, nb_turns):
  """Simulation algorithm used to count the number of games won by each players for a given number of games
  """
  nb_by_name = {}
  def_wins = 0
  atk_wins = 0
  for i in range(nb_games):
    game = Game(players, nb_turns)
    game.play()
    winner = game.get_winner_type()
    winner_name = game.get_winner_name()
    if winner == "Defender":
      def_wins += 1
    elif winner == "Attacker":
      atk_wins += 1
    if winner_name in nb_by_name:
      nb_by_name[winner_name] += 1
    else:
      nb_by_name[winner_name] = 1
  print("Number of games played: ", nb_games)
  print("Number of games with a total winner: ", def_wins+atk_wins)
  print("Defenders wins: ", def_wins, ", Attackers wins: ", atk_wins)
  print("Most represented populations at the last turn:", nb_by_name)

"""
nb_def = 1000
nb_att = 1000
hp_proportion = 0.5
nb_rs = 10
nb_turns = 200
attack_proba=0.25
defenders = create_n_defenders(nb_def, nb_rs, hp_proportion)
attackers = create_n_attackers(nb_att, attack_proba, nb_def)
players = defenders + attackers
nb_games = 1000
count_nb_of_games_won(players,nb_games, nb_turns)
"""