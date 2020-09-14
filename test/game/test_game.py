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
  assert len(game.turns) <= 6

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
  assert len(pev) <= 6

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
  g.export_game_results_type("game_results_type.csv")

def test_game_name(): 
  defs1 = create_n_defenders(1000,4,hp_proportion=0.5, hp_unit_cost=30, name="def1")
  defs2 = create_n_defenders(1000,4,hp_proportion=0.2, hp_unit_cost=30, offset=1000, name="def2")
  defs3 = create_n_defenders(1000,4,hp_proportion=0.8, hp_unit_cost=30, offset=2000, name="def3")
  atks1 = create_n_attackers(1000,0.7,offset =3000, name="atk1")
  players = defs1 + atks1 + defs2  + defs3
  g = Game(players,1000)
  g.play()
  g.export_game_results_name("game_results_name.csv")

def test_game_name_freq(): 
  defs1 = create_n_defenders(1000,10,hp_proportion=0.5, hp_unit_cost=30, name="def1")
  atks1 = create_n_attackers(1000,0.9,offset =1000, name="atk1")
  players = defs1 + atks1 
  g = Game(players,100000)
  g.play()
  g.export_game_results_name("game_results_name_freq1.csv")
  defs1 = create_n_defenders(1000,10,hp_proportion=0.5, hp_unit_cost=30, name="def1")
  atks1 = create_n_attackers(1000,0.1,offset =1000, name="atk1")
  players = defs1 + atks1 
  g = Game(players,100000)
  g.play()
  g.export_game_results_name("game_results_name_freq2.csv")

def test_nb_turns_and_winner_type():
  defs = create_n_defenders(1,3,0)
  atks = create_n_attackers(1,1,1)
  players = defs + atks
  g = Game(players,100)
  g.play()
  assert g.get_nb_turns_played() == 1
  assert g.get_winner_type() == "Attacker"

def test_nb_turns_and_winner_name():
  defs = create_n_defenders(1,3,0)
  atks = create_n_attackers(1,1,1, name="Winner")
  players = defs + atks
  g = Game(players,100)
  g.play()
  assert g.get_nb_turns_played() == 1
  assert g.get_winner_name() == "Winner"