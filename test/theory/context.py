import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from game_simulator.theory.def_theory import calculate_defender_best_cumulative_payoff
from game_simulator.theory.def_theory import calculate_theta_max
from game_simulator.theory.def_theory import calculate_attacker_payoff
from game_simulator.theory.def_theory import calculate_defender_payoff_when_attack
from game_simulator.theory.def_theory import calculate_defender_payoff_when_no_attack
from game_simulator.theory.def_theory import find_best_defender_configuration