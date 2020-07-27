class Player :
  def __init__(self, id):
    self.id = id

  def _to_string(self):
    s = "Player " + str(self.id)
    return s

  def confront(self, other):
    pass

  def create_similar_player(self, id):
    return Player(id)

  def get_player_type(self):
    return "Undefined player"