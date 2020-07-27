from .context import Player

def test_to_string():
  p = Player(10)
  assert p._to_string() == "Player 10"

def test_confront():
  p1 = Player(1)
  p2 = Player(2)
  assert p1.confront(p2) == None

def test_createSimilarPlayer():
  p1 = Player(5)
  p2 = p1.create_similar_player(4)
  assert p2.id == 4