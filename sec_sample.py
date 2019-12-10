# The following snippet generates n number of random samples from a given list using the "secret" library.

import secrets

secure_rand = secrets.SystemRandom() # creates a secure random object

my_list = ['a','b','c','d','e']
num_samples = 2

samples = secure_rand.sample(my_list,num_samples)
print(samples)
