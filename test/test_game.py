from .context import Game
from .context import Defender
from .context import Attacker
from .context import mocker

def test_play():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  p4 = Defender(4)
  p5 = Defender(5)
  players = [p1,p2,p3,p4,p5]
  nb_turns = 5
  game = Game(players,nb_turns)
  game.play()
  assert len(game.turns) == 6

def test_count_players_by_type():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  players = [p1,p2,p3]
  nb_turns = 5
  game = Game(players,nb_turns)
  game.play()
  players_nb = game.count_players_by_type(0)
  assert players_nb[0] == 1
  assert players_nb[1] == 2
