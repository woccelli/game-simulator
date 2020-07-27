import os
import sys

from pytest_mock import mocker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_simulator.player import Player
from game_simulator.defender import Defender
from game_simulator.attacker import Attacker
from game_simulator.turn import Turn
from game_simulator.game import Game