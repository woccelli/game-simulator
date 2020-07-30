def calculate_theta_max(bigdelta, delta_hp, n_rs):
  return bigdelta/(bigdelta+delta_hp*n_rs)

def calculate_defender_best_cumulative_payoff(n_rs,deltamax,bigdelta,mu,alphamax):
  for delta_hp in range(1,deltamax):
    thetamax = calculate_theta_max(bigdelta,delta_hp,n_rs)