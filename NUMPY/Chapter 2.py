import numpy.random as rd
import numpy as np
'''
Random Number: Number that can't be predicted logically.
Pseudo Random: It generate through a geneartion algorithm.
Radmon Distribution: It is a set of random numbers that follow a certain probability density function.
Probability Density Function: A function that describes  a continuous probability.
Random Permutation: It refers to random arrangement of elements.

Normal(Gaussian) Distribution: Event with limited range and infinite outcomes
    loc - (Mean) where peak of the bell exits
	scale - (Standard Deviation) flatness of distribution
	size - shape of array
	random.normal(loc=, scale=, size=)

Binomial Distribution: Event with 2 outcomes
    n - no. of trails
	p - probablity of occurance of each trial
	size - shape of array
	random.binomial(n=, p=, size=)

Poisson Distribution: Event with limited time of finite outcomes
    lam - no. of occurance
	size - shape of array
	random.poisson(lam=, size=)

Uniform Distribution: Event with equal intervals of outcomes (between upper and lower bound)
	a - lower bound, default value is 0.0
	b - upper bound, default value is 1.0
	size - shape of array
	random.uniform(a=, b=, size=)

Logistic Distribution: Event with limited range and progressive outcomes
	loc - (Mean) where peak of the bell exits
	scale - (Standard Deviation) flatness of distribution
	size - shape of array
	random.logistic(loc=, scale=, size=)

Multinomial Distribution: Event with 2 or more outcomes
	n - no. of possible outcomes
	pvals - list of possible outcomes
	size - shape of array
	random.multinominal(n=, pvals=, size=)

Exponential Distribution: Event with
	scale - inverse rate of lam in poisson
	size - shape of array
	random.exponential(scale=, size=)

Chi Square Distribution: Measure observed events differ from expected events
	df - degree of freedom
	size - shape of array
	random.chisquare(df=, size=)

Rayleigh Distribution: Event occurrence based on variable magnitude outcomes
	scale - (Standard Deviation) flatness of distribution
	size - shape of array
	random.rayleigh(scale=, size=)

Pareto Distribution: Events occurs with varying frequiences
	a - shape parameter
	size - shape of array
	random.pareto(a=, size=)

Zipf Distribution: Sample data is based on zipf's law
	a - distribution parameter
	size - shape of array
	random.zipf(a=, size=)
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
