
def main():
    y = (20, 2012, 232, 219, 'skj')
    kitten(*y)


def kitten(*args):
    if len(args):
        for s in args:
            print(s, s(id))
    else: print('Meow')


if __name__ == '__main__': main()

