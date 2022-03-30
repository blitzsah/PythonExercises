from pprint import pprint

# Finding the most common letter in a string

sentence = "Hello my name is Steven Hart and I live in the UK"


def most_common_letter(example_sentence):
    list_of_occurrences = []
    list_of_chars = list(example_sentence)
    for x in range(len(list_of_chars)):
        count_of_char_x = list_of_chars.count(list_of_chars[x])
        list_of_occurrences.insert(x, count_of_char_x)
    combined_list = list(zip(list_of_chars, list_of_occurrences))
    combined_set = set(combined_list)
    result_list = list(combined_set)
    result_list.sort(key=lambda occurrence: occurrence[1], reverse=True)
    if " " in result_list[0][0]:
        print(f"The character that occurs the most is: '{result_list[1][0]}' with {result_list[1][1]} occurrences")
    else:
        print(f"The character that occurs the most is: '{result_list[0][0]}' with {result_list[0][1]} occurrences")


def most_common_letter2(example_sentence):
    char_frequency = {}
    for char in example_sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    char_frequency_sorted = sorted(
        char_frequency.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    print(char_frequency_sorted[0])


# Exceptions
def exceptions():
    try:
        with open("Stacks.py") as file:
            print("File opened.")
        age = int(input("Age: "))
        xfactor = 10 / age
    except (ValueError, ZeroDivisionError):
        print("You didn't enter a valid age.")
    else:
        print("No exceptions were thrown")



