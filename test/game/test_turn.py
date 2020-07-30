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

def test_count_players_by_type():
  p1 = Attacker(1, 0.8)
  p2 = Attacker(2, 0.7)
  p3 = Defender(3)
  players = [p1,p2,p3]
  t = Turn(0,players)
  players_nb = t.count_players_by_type()
  assert players_nb["Turn"] == 0
  assert players_nb["Defenders"] == 1
  assert players_nb["Attackers"] == 2