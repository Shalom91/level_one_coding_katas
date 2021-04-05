def longest(list_of_words):
    """
    prints out the longest
    string in a list of 
    words
    """
    length_of_strings = [len(word) for word in list_of_words]
    max_length = max(length_of_strings)
    for word in list_of_words:
        if len(word) == max_length:
            print(word)

