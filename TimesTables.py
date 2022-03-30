# Function calculates the times table of the inputted number up to 1000


def times_table():
    print('Please input the number for the times table required')
    n = int(input())
    if n <= 0:
        print('Please ensure the value entered is greater than 0')
        return False
    e = range(0, 1000, n)  # iterates from 0 to 10000 in steps of n
    for iteration, i in enumerate(e):
        if iteration > 0:
            print(f'{n} x {iteration} is {i}')
    print('Would you like to continue? For yes enter Y, for no press enter')
    s = input()
    if s == 'Y':  # This line enables to user to try again if Y is entered
        times_table()
    else:
        return False


times_table()




