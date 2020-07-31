import numpy as np

def calculate_theta_max(bigdelta, delta_hp, n_rs):
  return bigdelta/(bigdelta+delta_hp*n_rs)

def calculate_attacker_payoff(theta, hp_efficiency, mu, gamma, alpha):
  return max(theta*(-hp_efficiency*mu + (1-hp_efficiency)*mu - gamma) + (1-theta)*(alpha-gamma),0)

def calculate_defender_payoff_when_attack(theta, hp_efficiency, mu, delta, alpha):
  return  theta * (hp_efficiency * mu - (1 - hp_efficiency) * mu - delta) + (1-theta) * (-alpha)

def calculate_defender_payoff_when_no_attack(theta,delta,beta):
  return theta*(-delta) + (1-theta)*beta

def calculate_defender_best_cumulative_payoff(n_rs,delta_max,bigdelta,mu,alpha_max):
  max_cumulative_sums = []
  for delta_hp in range(1,delta_max+1):
    defender_payoff_sums = []
    theta_max = calculate_theta_max(bigdelta,delta_hp,n_rs)
    for theta in np.arange(0,theta_max,0.05):
      hp_efficiency = delta_hp/(delta_max*(1+theta))
      delta = (delta_hp*n_rs*theta)/(1-theta)
      defender_payoff_sum = 0
      for alpha in range(1,alpha_max+1):
        beta = alpha + mu + 1
        gamma = alpha/10
        attacker_payoff = calculate_attacker_payoff(theta,hp_efficiency, mu, gamma, alpha)
        if attacker_payoff > 0 : #we loose precision here due to approximations
          defender_payoff = calculate_defender_payoff_when_attack(theta, hp_efficiency, mu, delta, alpha)
        else:
          defender_payoff = calculate_defender_payoff_when_no_attack(theta, delta, beta)
        defender_payoff_sum += defender_payoff
      defender_payoff_sums.append([defender_payoff_sum,theta,delta_hp])
    max_cumulative_sum = max(defender_payoff_sums)
    max_cumulative_sums.append(max_cumulative_sum)
  return max_cumulative_sums

def find_best_defender_configuration(n_rs,delta_max,bigdelta,mu,alpha_max):
  res = max(calculate_defender_best_cumulative_payoff(n_rs,delta_max,bigdelta,mu,alpha_max))
  theta = res[1]
  delta_hp = res[2]
  return {"theta": theta, "delta_hp": delta_hp }