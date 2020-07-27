from random import shuffle

class Turn:
  def __init__(self, players):
    self.players = list(players)
    shuffle(self.players)

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

