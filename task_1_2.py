def search_for_3(number_1, number_2):
    """
    returns true if either of the function
    arguments is a 3 and the sum of arguments
    contains a 3
    """
    sum_of_numbers = number_1 + number_2
    if (number_1 == 3) or (number_2 == 3) and ('3' in str(sum_of_numbers)):
        return True
    else:
        return False
