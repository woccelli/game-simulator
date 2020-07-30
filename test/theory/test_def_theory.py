from .context import calculate_theta_max

def test_calculate_theta_max():
  assert calculate_theta_max(100,10,5) == 100/(100+10*5)
  for i in range(1,1000):
    for j in range(1,i):
      thetamax = calculate_theta_max(i,j,5)
      assert thetamax < 1
      assert thetamax > 0