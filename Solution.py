def number_prediction(self):
    userinput = str(self)
    list_of_string = list(userinput)
    next_char = ""

    for char in range(len(list_of_string)):
        previous_char = list_of_string[char - 1]
        if list_of_string[char] == "_":
            for x in reversed(range(char - 1)):
                if list_of_string[x] == previous_char:
                    next_char = list_of_string[x + 1]
                    break
                else:
                    next_char = previous_char
            list_of_string.remove("_")
            list_of_string.insert(char, next_char)
    result_string = "".join(list_of_string)
    print(result_string)
    return result_string


def number_prediction2(example_string):
    list_of_string = list(example_string)           # Convert string to list
    if "_" in example_string:                       # Check the string contains some underscores
        for x in range(len(example_string)):        # For each character in the range of characters
            if list_of_string[x] == "_":            # Find the characters at which the underscore appears
                char_value = example_string[x]
                prev_char = example_string[x - 1]
                seq_char_0 = list_of_string[x - 11]
                seq_char_1 = list_of_string[x - 10]
                seq_char_2 = list_of_string[x - 9]
                seq_char_3 = list_of_string[x - 8]
                seq_char_4 = list_of_string[x - 7]
                seq_char_5 = list_of_string[x - 6]
                seq_char_6 = list_of_string[x - 5]
                seq_char_7 = list_of_string[x - 4]
                seq_char_8 = list_of_string[x - 3]
                seq_char_9 = list_of_string[x - 2]
                seq_char_10 = list_of_string[x - 1]
                test_sequence_list = [seq_char_0, seq_char_1, seq_char_2, seq_char_3, seq_char_4, seq_char_5,
                                      seq_char_6, seq_char_7, seq_char_8, seq_char_9, seq_char_10]
                for p in reversed(range(10)):
                    if test_sequence_list[p] == "_":
                        test_sequence_list = test_sequence_list[-p:]
                test_sequence_string = "".join(test_sequence_list)
                print(test_sequence_string)


number_prediction("1233456789_233911842_219_192410_123_123124_")

