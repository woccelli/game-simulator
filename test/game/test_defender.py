from .context import Defender
from .context import Attacker
from .context import create_n_defenders

def test_init_devices():
  defender1 = Defender(5)
  assert defender1.devices == [True] 
  defender2 = Defender(5, 3, 0.33)
  assert len(defender2.devices) == 4
  assert defender2.devices.count(False) == 1
  assert defender2.devices.count(True) == 3

def test_confront():
  p1 = Defender(1,4,0.8,30)
  p2 = Defender(2,4,0.2,30)
  p3 = Attacker(3, 1)
  p4 = Defender(4,4,0.8,30)
  p5 = Defender(5,4,0.75,50)
  assert p1.confront(p2)==-1
  assert p1.confront(p3)!=0
  assert p1.confront(p4)==0
  assert p1.confront(p5)==1


def test_create_similar_player():
  p1 = Defender(1,6,0.5)
  p2 = p1.create_similar_player(2)
  assert p2.id == 2 
  assert p2.rs_nb == 6
  assert p2.hp_proportion == 0.5
  assert p2.get_player_type() == "Defender"

def test_create_n_defenders():
  defenders = create_n_defenders(100,4, 0.5)
  assert len(defenders) == 100
  assert defenders[50].id == 50
  assert defenders[75].rs_nb == 4
  assert defenders[0].hp_proportion == 0.5