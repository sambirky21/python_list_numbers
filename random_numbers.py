import random

my_randoms = list()

for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""
for number in range(1, 6):
    my_randoms.append(random.randrange(1, 10, 1))
    if number in my_randoms:
        print('my_randoms contain {number}'),
    elif number not in my_randoms:
        print('my_randoms does not contain {number}')