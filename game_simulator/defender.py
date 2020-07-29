from random import shuffle
from game_simulator.player import Player

class Defender(Player):
  def __init__(self, id, rs_nb=1, hp_proportion=0):
    super().__init__(id)
    self.rs_nb = rs_nb
    self.hp_proportion = hp_proportion
    self.init_devices()

  def init_devices(self):
    self.hp_nb = int(self.rs_nb* self.hp_proportion/(1- self.hp_proportion))
    rs_devices = [True for i in range(self.rs_nb)] #rs --> True
    hp_devices = [False for i in range(self.hp_nb)] #hp --> False
    self.devices = rs_devices + hp_devices
    shuffle(self.devices)

  def _to_string(self):
    s = super()._to_string()
    s += ", Defender, hp_proportion=" + self.hp_proportion
    return s

  def confront(self, other):
    if other.__class__ != Defender:
      return - other.confront(self)
    else :
      return 0

  def create_similar_player(self, id):
    p = Defender(id, self.rs_nb, self.hp_proportion)
    p.init_devices()
    return p

  def get_player_type(self):
    return "Defender"