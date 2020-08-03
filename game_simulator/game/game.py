
from .turn import Turn
from .iohandler import write_dict_to_csv_file


class Game:
  """Represents a game which is constituted of players confronting each other in several turns.

  A game is initialized with nbTurns turns and a list of players. 
  A game is played when all turns have been played sequentially, updating the players each time.
  Once the game is played, one can export the results (the evolution of the players throughout the turns).

  ...

  Attributes
  ----------
    players : Player[]
      the list of players of the game (version 1.0: a player is either Defender or Attacker)
    nbTurns : int
      the number of turns that need to be played during the game
    turns : Turn[]
      the list of turns of the game, turns[0] is the inital state of the game
    isPlayed : boolean
      when False, the nbTurns turns haven't been played
      when True, the nbTurns turns have been played
  """
  def __init__(self, players, nbTurns):
    self.players = players
    self.nbTurns = nbTurns
    self.turns = [] #index 0 : initial state, index n : turn n
    self.isPlayed = False

  def play(self):
    """Simulates the encounter of all players over maximum nbTurns turns and updates the players at each turn.

    For each turn until there are no more attackers or defenders, or the nbTurns is reached, 
      Create the turn with the self.players attribute as input.
      Play the turn and update the self.players attribute with the new players of the turn.
      Store the played turn in the self.turns attribute.
    """
    players = self.players
    t = Turn(0,players)
    t.count_players()
    self.turns.append(t)
    for i in range(1,self.nbTurns+1):
      t = Turn(i,players)
      t.play()
      players = t.players
      self.turns.append(t)
      if t.nb_attackers == 0 or t.nb_defenders ==0:
        break
    self.isPlayed = True

  def get_players_evolution_type(self):
    """Returns a list of the number of players, classified by type, for each turn.
    """
    assert self.isPlayed
    players_evolution = []
    for t in self.turns:
      players_evolution.append({'Turn':t.id, 'Defenders':t.nb_defenders, 'Attackers':t.nb_attackers})
    return players_evolution

  def export_game_results_type(self):
    """Exports the number of players, classified by type, for each turn, into a csv file.
    """
    assert self.isPlayed
    players_evolution = self.get_players_evolution_type()
    csv_file = "game_results_type.csv"
    csv_columns = ["Turn", "Defenders","Attackers"]
    write_dict_to_csv_file(csv_file, players_evolution, csv_columns)

  def get_players_evolution_name(self):
    """Returns a list of the number of players, classified by name, for each turn.
    """
    assert self.isPlayed
    players_evolution = []
    for t in self.turns:
      players_evolution.append(t.nb_by_name)
    return players_evolution

  def export_game_results_name(self):
    """Exports the number of players, classified by type, for each turn, into a csv file.
    """
    assert self.isPlayed
    players_evolution = self.get_players_evolution_name()
    csv_file = "game_results_name.csv"
    csv_columns = sorted(players_evolution[0].keys())
    write_dict_to_csv_file(csv_file, players_evolution, csv_columns)

