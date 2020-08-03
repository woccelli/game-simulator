from .context import Game
from .context import Defender
from .context import Attacker
from .context import mocker
from .context import create_n_attackers, create_n_defenders

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
  p3 = Defender(3,4,0.7)
  p4 = Defender(4,3,0.5)
  p5 = Defender(5,2,0.6)
  players = [p1,p2,p3,p4,p5]
  nb_turns = 5
  game = Game(players,nb_turns)
  game.play()
  game.export_game_results_type()

def test_game_type(): 
  defs = create_n_defenders(100,4,0.7)
  atks = create_n_attackers(100,0.7,100)
  players = defs + atks
  g = Game(players,100)
  g.play()
  g.export_game_results_type()

def test_game_name(): 
  defs1 = create_n_defenders(100,4,hp_proportion=0.8, hp_unit_cost=30, name="def1")
  defs2 = create_n_defenders(100,4,hp_proportion=0.2, hp_unit_cost=30, offset=100, name="def2")
  atks1 = create_n_attackers(70,0.7,offset =200, name="atk1")
  atks2 = create_n_attackers(30,0.5,offset =270, name="atk2")
  players = defs1 + atks1 + defs2 + atks2
  g = Game(players,100)
  g.play()
  g.export_game_results_name()