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
        find()


def find():
    a = int(input('Enter fisrt location of the box in km: '))
    b = int(input('Enter fisrt location of the box in km: '))
    c = int(input('Enter fisrt location of the box in km: '))

    global location
    if [a,b,c] != location:
        print('Cargo is not discovered')
        location = random.sample(range(8), 3)
        find()
    else:
        verification_weight()
