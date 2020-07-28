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

def test_get_players_evolution():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  p4 = Defender(4)
  p5 = Defender(5)
  players = [p1,p2,p3,p4,p5]
  nb_turns = 5
  game = Game(players,nb_turns)
  game.play()
  pev = game.get_players_evolution()
  assert len(pev) == 6

def test_get_players_evolution():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  p4 = Defender(4)
  p5 = Defender(5)
  players = [p1,p2,p3,p4,p5]
  nb_turns = 5
  game = Game(players,nb_turns)
  game.play()
  game.export_game_results()
  