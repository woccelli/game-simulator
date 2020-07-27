from .context import Turn
from game_simulator.defender import Defender
from game_simulator.attacker import Attacker

def test_play():
  p1 = Defender(1,2)
  p2 = Attacker(2,1)
  players = [p1, p2]
  t = Turn(players)
  assert len(t.players) == 2
  t.play()
  i=0
  for player in t.players:
    if player.get_player_type() == "Attacker":
      i+=1
  assert i == 2