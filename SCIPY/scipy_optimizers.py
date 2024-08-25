import scipy.optimize as spo
import numpy as np
# Roots of an Equation
# root function can find root of only linear equations.
def eqn(x):
  return x + np.cos(x)
myroot = spo.root(eqn, 0)
print(myroot)

# Minimizing a Function
# A function, in this context, represents a curve, curves have high points and low points.
# High points are called maxima.
# Low points are called minima.
# The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.
# The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.
# Methods - 'CG' 'BFGS' 'Newton-CG' 'L-BFGS-B' 'TNC' 'COBYLA' 'SLSQP'
def eqn(x):
  return x**2 + x + 2
mymin = spo.minimize(eqn, 0, method='BFGS')
print(mymin)