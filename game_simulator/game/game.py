
from .turn import Turn
from .iohandler import write_dict_to_csv_file


class Game:
  def __init__(self, players, nbTurns):
    self.players = players
    self.nbTurns = nbTurns
    self.turns = [] #index 0 : initial state, index n : turn n
    self.isPlayed = False

  #Play -nbTurns- squentially
  #Store the played turns into -turns-
  #Update the current -players- with the last played turn
  def play(self):
    players = self.players
    t = Turn(0,players)
    self.turns.append(t)
    for i in range(1,self.nbTurns+1):
      t = Turn(i,players)
      t.play()
      players = t.players
      self.turns.append(t)
    self.isPlayed = True

  def get_players_evolution(self):
    assert self.isPlayed
    players_evolution = []
    for t in self.turns:
      players_evolution.append(t.count_players_by_type())
    return players_evolution

  def export_game_results(self):
    assert self.isPlayed
    players_evolution = self.get_players_evolution()
    csv_file = "game_results.csv"
    csv_columns = ["Turn", "Defenders","Attackers"]
    write_dict_to_csv_file(csv_file, players_evolution, csv_columns)


