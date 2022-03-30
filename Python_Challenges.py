import random
from collections import Counter


def mid(test):
    if len(test) % 2 == 0:
        i = ""
        return i
    return test[len(test)//2]


def online_count(dictionary):
    return Counter(dictionary.values())


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def random_number():
    return random.randint(1, 100)


def only_ints(test1, test2):
    if type(test1) is int and type(test2) is int:
        return True
    else:
        return False


def consecutive_zeros(binary_string):
    count_of_zeros = 0
    stored_count = 0
    for x in binary_string:
        if x == "0":
            count_of_zeros += 1
            if stored_count < count_of_zeros:
                stored_count = count_of_zeros
        else:
            count_of_zeros = 0
    return stored_count


def add12(string, modules):
    for x in range(modules):
        if x == 0:
            continue
        multiplier = x * 12
        print(string + "[" + str(multiplier) + "]")


add12("Modules", 10)


def pos_finder(value):
    for x in range(10):
        print(value + (x * 20))


pos_finder(1058)

