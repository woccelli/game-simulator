from game_simulator.defender import Defender
from game_simulator.player import Player

class Attacker(Player):
  def __init__(self, id, attack_proba):
    super().__init__(id)
    self.attack_probability = attack_proba

  def _to_string(self):
    s = super()._to_string()
    s+= ", Attacker, attack_probability=" + self.attack_probability
    return s

  def confront(self, other):
    if other.__class__ == Defender:
      return 1
    else:
      return 0

  def create_similar_player(self, id):
    p = Attacker(id, self.attack_probability)
    return p

  def get_player_type(self):
    return "Attacker"