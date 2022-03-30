def double_letters(test_string):
    test = False
    for x in range(len(test_string) - 1):
        if test_string[x] == test_string[x + 1]:
            test = True
            return test
    return test


print(double_letters("Hello"))