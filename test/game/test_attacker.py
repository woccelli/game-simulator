from .context import Attacker
from .context import Defender
from .context import create_n_attackers

def test_confront():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  res1 = p1.confront(p3)
  assert p1.confront(p2)==0
  assert res1==1 or res1==0

def test_create_similar_player():
  p1 = Attacker(1,0.5)
  p2 = p1.create_similar_player(2)
  assert p2.id == 2
  assert p2.attack_probability == 0.5
  assert p2.get_player_type() == "Attacker"

def test_attack_simple():
  p1 = Defender(1,5,0)
  p2 = Attacker(2,1)
  assert p2.confront_defender(p1) == 1

def test_attack():
  p1 =Defender(1,4,0.5)
  p2 = Attacker(2,1)
  for i in range(100):
    assert p2.confront_defender(p1) != 0

def test_attack_noattack():
  p1 =Defender(1,4,0.5)
  p2 = Attacker(2,0)
  assert p2.confront_defender(p1) == 0

def test_create_n_attackers():
  attackers = create_n_attackers(100,1,100)
  assert len(attackers) == 100
  assert attackers[50].id == 150
  assert attackers[75].attack_probability == 1
