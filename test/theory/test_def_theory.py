from .context import calculate_theta_max
from .context import calculate_attacker_payoff
from .context import calculate_defender_payoff_when_attack
from .context import calculate_defender_payoff_when_no_attack
from .context import find_best_defender_configuration

def test_calculate_theta_max():
  assert calculate_theta_max(100,10,5) == 100/(100+10*5)
  for i in range(1,1000):
    for j in range(1,i):
      thetamax = calculate_theta_max(i,j,5)
      assert thetamax < 1
      assert thetamax > 0

def test_calculate_attacker_payoff():
  theta = 0.8
  hp_efficiency = 0.7
  mu = 250
  gamma = 100
  alpha = 1000
  res = calculate_attacker_payoff(theta, hp_efficiency, mu, gamma, alpha)
  assert abs(res -20) < 0.001
  hp_efficiency = 0.95
  res = calculate_attacker_payoff(theta, hp_efficiency, mu, gamma, alpha)
  assert res == 0


def test_calculate_defender_payoff_when_attack():
  theta = 0.8
  hp_efficiency = 0.7
  mu = 250
  delta = 150
  gamma = 100
  alpha = 1000
  res = calculate_defender_payoff_when_attack(theta, hp_efficiency, mu, delta, alpha)
  assert abs(res - (-240)) < 0.001

def test_calculate_defender_payoff_when_no_attack():
  theta = 0.8
  hp_efficiency = 0.7
  mu = 250
  delta = 150
  gamma = 100
  alpha = 1000
  beta = alpha + mu + 1
  res = calculate_defender_payoff_when_no_attack(theta,delta,beta)
  assert abs(res - 130.2) < 0.001

def test_find_best_defender_configuration():
  n_rs = 2
  delta_max = 30
  bigdelta = 200
  mu = 250
  alpha = 1000
  res = find_best_defender_configuration(n_rs,delta_max,bigdelta,mu,alpha)
  assert res['theta'] == 0.65
  assert res['delta_hp'] == 30
  n_rs = 3
  bigdelta = 70
  res = find_best_defender_configuration(n_rs,delta_max,bigdelta,mu,alpha)
  assert res['theta'] == 0.45
  assert res['delta_hp'] == 28