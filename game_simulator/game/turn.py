from random import shuffle

class Turn:
  """Represents a single turn (step) in the full game. When played, makes each player confront another player.

  ...

  Attributes
  ----------
  id : int 
    unique identifier
  players : Player[]
    list of players of the turn. 
    The list of players before the turn is played is different from the list of players after the turn is played.
    The list of players is shuffled when creating the turn.
  isPlayed : boolean
    when False, means that the players haven't confronted each other during that turn
    when True, means that the players have confronted each other and the players have been updated accordingly
  """

  def __init__(self, id, players):
    self.id = id
    self.players = list(players)
    self.isPlayed = False
    shuffle(self.players)

  def play(self):
    """Simulates the encounter of all the players and updates the players accordingly.

    From the players list, makes player A at index n confront player B at index n+1
    Every player of the list plays exactly once (A.confront(B) OR B.confront(A)):
      if player A wins, player B becomes a player with the same type and characteristics as A
      if player B wins, player A becomes a player with the same type and characteristics as B
    if there is an odd number of players, the last player (index len(players - 1)) remains unchanged
    """
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

  def count_players_by_type(self):
    """Count the number of players, classified by type, in the current self.players attribute.
    """
    attackers = 0
    defenders = 0
    for p in self.players:
      if p.get_player_type() == "Defender":
        defenders += 1
      elif p.get_player_type() == "Attacker":
        attackers += 1
    return {"Turn": self.id, "Defenders":defenders, "Attackers": attackers}

  def count_players_by_name(self):
    """Count the number of players, classified by name, in the current self.players attribute.
    """
    turn_players_count = {'Turn':self.id}
    for p in self.players:
      name = p.name
      if name in turn_players_count:
        turn_players_count[name] += 1
      else:
        turn_players_count[name] = 1
    return turn_players_count