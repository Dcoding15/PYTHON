#!/usr/bin/python3.11
import numpy.random as rd
import numpy as np
'''
√ 	-> 221a (Square root)
σ 	-> 03c3 (Standard Deviation)
μ 	-> 03bc (Mean)
π 	-> 03c0 (Pi)                                 	~3.14159
e 	-> base of natural logirithm      				~2.71828
∞ 	-> 221e (Infinite)
p 	-> probability of success on single trail
q 	-> probability of failure on single trail
n 	-> number of trails
x   -> number of times event occus
λ   -> 03bb (Lambda) (rate of occurance of events)
α   -> 03b1 (Alpha) (shape parameter)
xm	-> minimum possible positive value of x
'''

'''
Random Number: Number that can't be predicted logically.
Pseudo Random: It generate through a geneartion algorithm.
Radmon Distribution: It is a set of random numbers that follow a certain probability density function.
Probability Density Function: A function that describes  a continuous probability.
Random Permutation: It refers to random arrangement of elements.

Normal(Gaussian) Distribution: -
    Event with limited range and infinite outcomes
    f(x) = (1/σ√2π) * e ^ (-0.5 * ((x-μ)/σ) ^ 2)

Binomial Distribution: -
    Event with 2 outcomes
    P(x) = C(n,x) * (p ^ x) * (q ^ (n-x))

Poisson Distribution: -
    Event with limited time of finite outcomes
    P(x) = ((e ^ -λ) * (λ ^ x)) / factorial(x)

Uniform Distribution: -
    Event with equal intervals of outcomes (between upper and lower bound)
    f(x) = 1 / (b-a)      [If a <= x <= b]

Logistic Distribution: -
	Event with how much item we have and how much time it needed to 

Multinomial Distribution: -
    Event with 2 or more outcomes
    P(x) = (n! / (x1! . . . xk!))

Exponential Distribution: -

Chi Square Distribution: -

Rayleigh Distribution: -

Pareto Distribution: -
    Event where 80% of effect come from 20% of causes
    f(x) = (α * (xm ^ α))/(x^(α+1))        [If x >= xm]

Zipf Distribution: -
'''

# Generate Random Integer
# Generates random number with some user range
# randint(range_start, range_stop, array_size)
'''
a = rd.randint(1,100,size=5)
b = rd.randint(1,100,size=(3,3))
print(a,b,sep="\n")
'''

# Generate Random Float
# Generate random number between 0 and 1
# rand(array_size)
'''
a = rd.rand(5)
b = rd.rand(3,3)
print(a,b,sep="\n")
'''

# Generate Random Number From Array
# Generate random number by choosing elements from array
# choice(list_object, array_size)
'''
a = rd.choice([2,3,1,4,5,6,9,8,0,22,1223,6,2],size=5)
b = rd.choice([2,3,1,4,5,6,9,8,0,22,1223,6,2],size=(3,3))
print(a,b,sep="\n")
'''

# Data Distribution
# Generate a random choice from array elements with probabily distribution correspoding to it.
# choice(list_object, probabily_distribution, array_size)
# The sum of probability is always 1
'''
a = rd.choice([4,2,6,5,7],p=[1/15,2/15,3/15,4/15,5/15],size=5)
b = rd.choice([4,2,6,5,7],p=[1/15,2/15,3/15,4/15,5/15],size=(3,3))
print(a,b,sep="\n")
'''

# Random Permutation
# permutation() returns re-arranged array and doesn't affect original array
# shuffle() reurn re-arraged original array
'''
arr = np.array([1,2,3,4,5,6,7])
a = rd.permutation(arr)
rd.shuffle(arr)
print(arr,a,sep="\n")
'''
