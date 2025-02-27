

import numpy as np

print(np.random.rand())
print(np.random.rand(10))
print(np.random.rand(3, 3))

print(np.random.randint(100))
print(np.random.randint(100, size=10))
print(np.random.randint(100, size=(3, 3)))
print(np.random.randint(low=100, high=200, size=(3, 3)))

# Generate a random number from a normal distribution with mean 0 and standard deviation 1
print(np.random.randn())

# Generate a 2D array of 3x3 random numbers from a uniform distribution between 0 and 1
print(np.random.uniform(size=(3, 3)))

# Generate a 2D array of 3x3 random numbers from a binomial distribution with n=10 and p=0.5
print(np.random.binomial(10, 0.5, size=(3, 3)))

# Poisson ,Exponential, Gamma, Chi-squared, T-distribution, F-distribution Beta Log-normal Laplace