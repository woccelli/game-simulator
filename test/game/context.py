import os
import sys

from pytest_mock import mocker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from game_simulator.game.player import Player
from game_simulator.game.defender import Defender
from game_simulator.game.attacker import Attacker
from game_simulator.game.turn import Turn
from game_simulator.game.game import Game
from game_simulator.game.iohandler import write_dict_to_csv_file
from game_simulator.game.defender import create_n_defenders
from game_simulator.game.attacker import create_n_attackers