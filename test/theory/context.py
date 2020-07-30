import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from game_simulator.theory.def_theory import calculate_defender_best_cumulative_payoff
from game_simulator.theory.def_theory import calculate_theta_max