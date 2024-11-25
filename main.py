import random

location = [2, 3, 4];
weight = [200, 250, 263]


def verification_weight():
    global weight
    global location

    if sum(weight) == 713:
        print('You found cargo')
    else:
        print("It does not have needed weight")
      
        location = random.sample(range(8), 3)

