import os
import sys

from pytest_mock import mocker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_simulator.player import Player
from game_simulator.defender import Defender
from game_simulator.attacker import Attacker
from game_simulator.turn import Turn
from game_simulator.game import Game
from game_simulator.iohandler import write_dict_to_csv_file
from game_simulator.defender import create_n_defenders
from game_simulator.attacker import create_n_attackers