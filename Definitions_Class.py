# Class: Blueprint for creating new objects
# Object: Instance of a class

# Example...
# Class: Human
# Objects: John, Mary, Jack

class Point:
    default_colour = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.default_colour = "yellow"
print(point.default_colour)
print(Point.default_colour)
point.draw()


def is_power_of_two(candidate):
    if candidate <= 0:
        return False

    if candidate == 1:
        return True

    if candidate % 2 != 0:
        return False

    print(candidate)
    return is_power_of_two(candidate / 2)


test = 1073741820


print(f"{test} is power of two: {is_power_of_two(test)}")
