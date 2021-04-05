def search_for_65(number_1, number_2):
    """
    returns true if either of the function's
    arguments  is 65 or the sum of the arguments
    is equal to 65
    """
    sum_of_numbers = number_1 + number_2
    if (number_1 == 65) or (number_2 == 65) or (sum_of_numbers == 65):
        return True
    else:
        return False
