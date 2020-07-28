
from game_simulator.turn import Turn

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
    t = Turn(players)
    self.turns.append(t)
    for i in range(self.nbTurns):
      t = Turn(players)
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
  


