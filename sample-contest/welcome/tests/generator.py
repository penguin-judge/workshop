#!/usr/bin/env python3

def make_file(a, b, prefix, number):
    statement = f'{a} {b}\n'
    with open(f'{prefix}{number:02}.in', 'w') as f:
        f.write(statement)

# define domain of the inputs
min_a, max_a = 1, 100
min_b, max_b = 1, 100000

# sample input in README.md
make_file(10, 20, 'sample', 1)

# maximum inputs
make_file(max_a, max_b, 'maximum', 1)

# minimum inputs
make_file(min_a, min_b, 'minimum', 1)

# random inputs
import random
for number in range(1, 11):
    a = random.randint(min_a, max_a)
    b = random.randint(min_b, max_b)
    make_file(a, b, 'random', number)

