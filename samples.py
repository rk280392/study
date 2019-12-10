# The following snippet generates n number of random samples from a given list using the random library.

import random

my_list = ['a', 'b', 'c', 'd', 'e']

num_samples = 2

samples = random.sample(my_list,num_samples)
print(samples)
