import os


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
        if message[counter - 1] not in characters_allowed and message[counter] in characters_allowed:
            # A word is starting
            word = ''
            while message[counter] in characters_allowed:  # While the word is not "finished"
                word += message[counter]
                counter += 1

            list_words.append(word)  # The word is added to the list

        counter += 1

    file.close()

    return list_words


def get_prob_from_theme(theme_list, text_list):
    """Return percentage for links between the text and the theme.
    Parameters
    ----------
    theme_list: list of theme checked (list)
    text_list: text with all the word in the text (list)

    Return
    ------
    prob_1: the probabilities of being in theme (float)

    """

    sibling_word = []

    # check word by word
    for word_theme in theme_list:
        for word_text in text_list:
            if word_theme == word_text:
                sibling_word.append(word_text)

    # compute probabilities
    prob_1 = 1
    for prob in sibling_word:
        # multiplicate the probabilities by the pourcentage of appeared word
        prob_1 *= theme_list[prob][0]
    for prob in theme_list:
        # multiplicate the probabilities by the pourcentage of unappeared word
        if not check_sibling(prob, sibling_word):
            prob_1 *= theme_list[prob][1]
    return prob_1


def check_sibling(check_word, sibling_word):
    """Return True if the word is in both list. False otherwise
    Parameters
    ----------
    check_word: the word to check (str)
    sibling_word: list of words in theme_list and text_list (list)

    Return
    ------
    True if the word is in both list
    False if isn't

    """
    for test_word in sibling_word:
        if check_word == test_word:
            return True
    # after checked the whole list, and there is no sibling
    return False


def get_theme(probabilities, most_probable_theme=('', 0)):
    """
    Finds the theme of an article by comparing the probabilities of each theme.
    Parameters:
    -----------
    probabilities: list containing a tuple for each theme in the form (theme, probability)
    most_probable_theme: tuple containing the most probable theme found so far and it's probability

    Return:
    -------
    theme : the most probable theme

    Notes:
    ------
    This function is recursive

    Example:
    --------
    >>> get_theme([('sport', 0.4), ('politics', 0.5), ('animals', 0.85)])
    'animals'
    """

    # --- Basic case ---
    if not probabilities:
        # If the probability list is empty, we return the most probable theme found so far
        return most_probable_theme[0]

    # --- Recursive case ---
    if probabilities[0][1] > most_probable_theme[1]:
        # Checks for a new highest probability
        most_probable_theme = probabilities[0]

    # Calls get_theme() to analyse the next element of list probabilities
    return get_theme(probabilities[1:], most_probable_theme)


def sort(probabilities, path):
    """ For each file, place it within the correct repertory.
    Parameters
    ----------
    probabilities : dictionary which for each file returns both its probabilities to be or not to be in a theme
    probabilities = {"theme1":{"word1": (prob, antiprob), "word2": (prob, antiprob), ...}, "theme2": ...}

    path : the path of the repertory where archives can be found

    """

    # Initialize all themes
    themes = []
    for key in probabilities:
        themes += key

    files = [file for file in os.listdir(path+'/unsorted/') if not file == '.DS_Store']
    for file in files:
        # Get all the words used in the file
        words = get_words_in_file(path+'/unsorted/'+file)

        # Get all the probabilities for the file to be in one theme
        theme_probabilities = get_prob_from_theme(themes, words)

        # Get the most probable theme
        file_theme = get_theme(theme_probabilities, ('', 0))

        # Move file to the correct repertory
        os.rename(os.getcwd() + '/unsorted/' + file, path + '/sorted/' + file_theme + '/' + file)
