def get_words_in_file(path):
    """Returns the list of words contained in a file. 

    Parameters:
    ----------
    path: the path of the analyzed file (str)

    Returns:
    -------
    list_words: the list of words contained in the file (list)
    """

    file = open(path, 'r')

    characters_allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    list_words = []

    counter = 1

    message = file.read()

    while counter != len(message):
        if message[counter - 1] not in characters_allowed and message[counter] in characters_allowed: # A word is starting
            word = ''
            while message[counter] in characters_allowed: # While the word is not "finished"
                word += message[counter]
                counter += 1

            list_words.append(word) # The word is added to the list

        counter += 1

    file.close()

    return list_words