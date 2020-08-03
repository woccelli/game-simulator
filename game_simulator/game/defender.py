from random import shuffle
from .player import Player

class Defender(Player):
  """ Represents the player type: Defender. 

  The Defender is one of the two types of players of the game. His behavior
  is defensive against Attackers and aggressive against Defenders. 
  When confronting an Attacker, the Defender will survive if the attacker does nothing
  or attacks one of the Defender's honeypots.
  When confronting another Defender, the defender that survives is the one with the 
  lowest defense_cost.

  ...

  Attributes
  ----------
  rs_nb : int
    the number of real servers in the defender's devices
  hp_nb : int 
    the number of honeypots in the defender's devices
  hp_proportion : float
    the percentage of honeypots in the defender's network
  hp_unit_cost : int
    cost of deployment and maintenance of a single honeypot
  name : str
    the name of the Defender, to be changed if several Defenders
    with various attributes are present in the game  
  devices : boolean[]
    list of devices of the Defender, True is a Real server, False is a Honeypot
  defense_cost : int
    total cost of the honeypots' deployment = hp_nb * hp_unit_cost
  """

  def __init__(self, id, rs_nb=1, hp_proportion=0, hp_unit_cost=0, name="Defender"):
    super().__init__(id, name)
    self.rs_nb = rs_nb
    self.hp_proportion = hp_proportion
    self.hp_unit_cost = hp_unit_cost
    self.init_devices()

  def init_devices(self):
    """Creates list of devices of the Defender. Real servers and Honeypots are randomly shuffled.
    """
    self.hp_nb = int(self.rs_nb* self.hp_proportion/(1- self.hp_proportion))
    self.defense_cost = self.hp_nb * self.hp_unit_cost
    rs_devices = [True for i in range(self.rs_nb)] #rs --> True
    hp_devices = [False for i in range(self.hp_nb)] #hp --> False
    self.devices = rs_devices + hp_devices
    shuffle(self.devices)

  def confront(self, other):
    """Simulates the encounter between two players.

    Return
    ----------
      1 if the player wins, 
      -1 if the player looses 
      0 if nothing is to be done 
    """
    if other.__class__ != Defender:
      return - other.confront(self)
    else :
      if self.defense_cost < other.defense_cost:
        return 1
      elif self.defense_cost == other.defense_cost:
        return 0
      else:
        return -1

  def create_similar_player(self, id):
    """Returns a copy of the player: same attributes except the id.
    """
    p = Defender(id, self.rs_nb, hp_proportion=self.hp_proportion, hp_unit_cost=self.hp_unit_cost, name=self.name)
    return p

  def get_player_type(self):
    return "Defender"

#duplicate of this method in attacker.py
def create_n_defenders(n, rs_nb, hp_proportion, hp_unit_cost=0, offset=0, name=""):
  """Returns n Defenders with the same attributes and with ids ranging from offset to offset+n.
  """
  defenders = []
  for i in range(offset,n+offset):
    if(name != ""):
      d = Defender(i,rs_nb,hp_proportion=hp_proportion,hp_unit_cost=hp_unit_cost, name=name)
    else:
      d = Defender(i,rs_nb,hp_proportion=hp_proportion,hp_unit_cost=hp_unit_cost)
    defenders.append(d)
  return defenders
  