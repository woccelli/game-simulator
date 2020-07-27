from .context import Attacker
from .context import Defender

def test_confront():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  assert p1.confront(p2)==0
  assert p1.confront(p3)==1

def test_create_similar_player():
  p1 = Attacker(1,0.5)
  p2 = p1.create_similar_player(2)
  assert p2.id == 2
  assert p2.attack_probability == 0.5
  assert p2.get_player_type() == "Attacker"