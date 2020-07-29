from game_simulator.defender import Defender
from game_simulator.player import Player
import random

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
      return self.attack(other)
    else:
      return 0 #do nothing

  def create_similar_player(self, id):
    p = Attacker(id, self.attack_probability)
    return p

  def get_player_type(self):
    return "Attacker"

  def attack(self, other):
    if random.random() < self.attack_probability: #attack
      index = random.randint(0,len(other.devices)-1)
      device = other.devices[index]
      if device == True: #rs
        return 1
      else: #hp
        return -1
    else: #do not attack
      return 0

#duplicate of this method in defender.py
def create_n_attackers(n, attack_probability, offset=0):
  attackers = []
  for i in range(offset,n+offset):
    d = Attacker(i,attack_probability)
    attackers.append(d)
  return attackers