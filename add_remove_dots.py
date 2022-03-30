def add_dots(input_string):
    return ".".join(input_string)


def remove_dots(input_string):
    return str(input_string).replace(".", "")


def div_3(s):
    return s % 3 == 0


print(div_3(300))
