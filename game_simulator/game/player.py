class Player :
  """Represents an abstract player of the game.

  ...

  Attributes
  ----------
  id : int
    unique identifier
  name : str
    name of the player, used for practical differentiation between players
  """

  def __init__(self, id, name="Player"):
    self.id = id
    self.name = name

  def confront(self, other):
    """Simulates the encounter between two players. implemented in children classes.
    """
    pass

  def create_similar_player(self, id, name):
    """Returns a copy of the player: same attributes except the id.
    """
    return Player(id, name)

  def get_player_type(self):
    return "Undefined player"