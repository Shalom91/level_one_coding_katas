from itertools import zip_longest


def combine(list_1, list_2):
    """"
    combines two lists alternately
    """
    combine_lists = [[value1, value2] for value1, value2 in zip_longest(list_1, list_2)]
    unpack_list = [value for sublist in combine_lists for value in sublist]
    return unpack_list

    