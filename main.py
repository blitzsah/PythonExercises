#!/usr/bin/env python3

import platform


def main():
    message()


def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    print('line 3')


if __name__ == '__main__': main()

class Solution:
    def number_prediction(self):
        userinput = str(self)
        list_of_string = list(userinput)

        for char in range(len(list_of_string)):
            if list_of_string[char] == "_":
                previous_char = list_of_string[char - 1]
                for x in range(len(list_of_string)):
                    if list_of_string[x].__contains__(previous_char):
                        next_char = list_of_string[x + 1]
                    elif not list_of_string[x].__contains__(previous_char):
                        next_char = "2"
                        break
                list_of_string.remove("_")
                list_of_string.insert(char, next_char)
        result_string = "".join(list_of_string)
        return result_string
