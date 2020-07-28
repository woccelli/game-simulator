from random import shuffle

class Turn:
  def __init__(self, players):
    self.players = list(players)
    self.isPlayed = False
    shuffle(self.players)


  #From the -players- list, makes player A at index n confront player B at index n+1
  #Every player of the list plays extacly once (A.confront(B) OR B.confront(A))
  #if player A wins, player B becomes a player with the same type and characteristics as A
  #if player B wins, player A becomes a player with the same type and characteristics as B
  #if there is an odd number of players, the last player (index len(players - 1)) remains unchanged
  def play(self):
    if len(self.players) == 2: #we do that to avoid an empty list in the for loop (range(0,0) == [])
      res = self.players[0].confront(self.players[1])
      if res == 1 :
        self.players[1] = self.players[0].create_similar_player(self.players[1].id)
      if res == -1 :
        self.players[0] = self.players[1].create_similar_player(self.players[0].id)
    else:
      for i in range(0,len(self.players)-2,2):
        res = self.players[i].confront(self.players[i+1])
        if res == 1 :
          self.players[i+1] = self.players[i].create_similar_player(self.players[i+1].id)
        if res == -1 :
          self.players[i] = self.players[i+1].create_similar_player(self.players[i].id)
    self.isPlayed = True

  #Count the number of players of each type in the current local -players- attribute
  def count_players_by_type(self):
    attackers = 0
    defenders = 0
    for p in self.players:
      if p.get_player_type() == "Defender":
        defenders += 1
      elif p.get_player_type() == "Attacker":
        attackers += 1
    return {"Defenders":defenders, "Attackers": attackers}