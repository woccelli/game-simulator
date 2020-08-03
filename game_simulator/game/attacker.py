from .defender import Defender
from .player import Player
import random


class Attacker(Player):
  """ Represents the player type: Attacker. 

  The Attacker is one of the two types of players of the game. His behavior
  is aggressive against Defenders and passive against Attackers. 
  When confronting a Defender, the Attacker will attack the Defender's 
  devices with an attack probability.

  ...

  Attributes
  ----------
  attack_probability : float
    the probability of attacking a defender's device when confronting
  name : str
    the name of the Attacker, to be changed if several attackers with
    various attack_proba are present in the game
  """

  def __init__(self, id, attack_proba=1, name="Attacker"):
    super().__init__(id, name)
    self.attack_probability = attack_proba

  def confront(self, other):
    """Simulates the encounter between two players.

    Return
    ----------
      1 if the player wins, 
      -1 if the player looses 
      0 if nothing is to be done 
    """
    if other.__class__ == Defender:
      return self.confront_defender(other)
    else:
      return 0

  def confront_defender(self, other):
    """Simulates the encounter with a defender. The Attacker will attack depending on its attack_probability.

    Return
    ----------
    1 if the attacked device is a Real server
    -1 if the attacked device is a Honeypot
    0 if no attack is launched
    """
    if random.random() < self.attack_probability:
      index = random.randint(0,len(other.devices)-1)
      device = other.devices[index]
      if device == True:
        return 1
      else: 
        return -1
    else: 
      return 0

  def create_similar_player(self, id):
    """Returns a copy of the player: same attributes except the id.
    """
    p = Attacker(id, attack_proba=self.attack_probability, name=self.name)
    return p

  def get_player_type(self):
    return "Attacker"

#duplicate of this method in defender.py
def create_n_attackers(n, attack_probability, offset=0, name=""):
  """Returns n Attackers with the same attributes and with ids ranging from offset to offset+n.
  """
  attackers = []
  for i in range(offset,n+offset):
    if name != "":
      a = Attacker(i,attack_probability, name=name)
    else:
      a = Attacker(i,attack_probability)
    attackers.append(a)
  return attackers