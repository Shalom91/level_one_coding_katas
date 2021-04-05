def triangle(number):
    """
    prints out a triangle
    """
    if number < 0:
        change_to_positive = number * (-1)
        for value in reversed(range(1, change_to_positive + 1)):
            print("#" * value)
    else:
        for value in range(1, number + 1):
            print("#" * value)


