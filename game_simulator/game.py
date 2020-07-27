
from game_simulator.turn import Turn

class Game:
  def __init__(self, players, nbTurns):
    self.players = players
    self.nbTurns = nbTurns
    self.turns = []

  def play(self):
    players = self.players
    t = Turn(players)
    self.turns.append(t)
    for i in range(self.nbTurns):
      t = Turn(players)
      t.play()
      players = t.players
      self.turns.append(t)

  def count_players_by_type(self, turn_nb):
    attackers = 0
    defenders = 0
    if turn_nb < len(self.turns):
      players_of_turn = self.turns[turn_nb].players
      for p in players_of_turn:
        if p.get_player_type() == "Defender":
          defenders += 1
        elif p.get_player_type() == "Attacker":
          attackers += 1
    return [defenders, attackers]


