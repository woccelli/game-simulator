from .context import Turn
from .context import Defender
from .context import Attacker

def test_play():
  p1 = Defender(1,2)
  p2 = Attacker(2,1)
  players = [p1, p2]
  t = Turn(0,players)
  assert len(t.players) == 2
  t.play()
  i=0
  for player in t.players:
    if player.get_player_type() == "Attacker":
      i+=1
  assert i == 2

def test_count_players_by_name():
  p1 = Attacker(1, 0.8, 'Attacker1')
  p2 = Attacker(2, 0.7, 'Attacker2')
  p3 = Attacker(3, 0.7, 'Attacker3')
  p4 = Defender(4,name='Def1')
  p5 = Defender(5,name='Def1')
  p6 = Defender(6,name='Def1')
  p7 = Defender(7)
  players = [p1,p2,p3,p4,p5,p6,p7]
  t = Turn(0,players)
  t.count_players()
  assert t.id == 0
  assert t.nb_attackers == 3
  assert t.nb_defenders == 4
  assert t.nb_by_name['Turn'] == 0
  assert t.nb_by_name["Attacker1"] == 1
  assert t.nb_by_name["Attacker2"] == 1
  assert t.nb_by_name["Attacker3"] == 1
  assert t.nb_by_name['Def1'] == 3
  assert t.nb_by_name['Defender'] == 1