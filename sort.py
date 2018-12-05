"""
This module purpose is to analyse the documents in the unsorted directory
and move them to the correct cirectory in sorted.
"""

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

    file = open(path, 'r', encoding="ISO-8859-1")

    characters_allowed = 'abcdefghijklmnopqrstuvwxyz'
    blacklist = ['come', 'because', 'once', 'may', 'too', 'best', 'thereby', 'after', 'don', 'these', 'gone', 'only',
                 'shall', 'new', 'against', 'out', 'sunday', 'isn', 'where', 'always', 'him', 'without', 'very', 'does',
                 'email', 'quite', 'never', 'before', 'entirely', 'anyways', 'still', 'lines', 'monday', 'thank',
                 'myself', 'from', 'over', 'yet', 'were', 'just', 'will', 'see', 'anymore', 'let', 'while', 'wednesday',
                 'later', 'must', 'your', 'itself', 'well', 'although', 'use', 'many', 'thought', 'them', 'when',
                 'have', 'even', 'having', 'tell', 'however', 'himself', 'what', 'mail', 'going', 'yes', 'regards',
                 'com', 'got', 'his', 'between', 'reply', 'makes', 'two', 'want', 'more', 'not', 'etc', 'though',
                 'someone', 'one', 'could', 'right', 'that', 'neither', 'did', 'saturday', 'much', 'something', 'get',
                 'used', 'like', 'think', 'didn', 'most', 'wouldn', 'haven', 'instead', 'same', 'guess', 'some',
                 'anything', 'those', 'this', 'make', 'know', 'both', 'you', 'need', 'then', 'either', 'subject',
                 'with', 'say', 'largest', 'made', 'back', 'would', 'actually', 'good', 'few', 'way', 'doing',
                 'tuesday', 'had', 'left', 'nothing', 'should', 'friday', 'might', 'and', 'are', 'per', 'rather',
                 'they', 'little', 'since', 'her', 'own', 'she', 'bye', 'lot', 'ones', 'give', 'actual', 'others',
                 'each', 'until', 'was', 'likely', 'said', 'can', 'please', 'who', 'why', 'other', 'our', 'enable',
                 'half', 'perhaps', 'for', 'simple', 'the', 'now', 'means', 'anyone', 'day', 'sorry', 'ought', 'any',
                 'wrong', 'been', 'their', 'also', 'has', 'unless', 'all', 'how', 'better', 'there', 'here', 'mostly',
                 'its', 'things', 'late', 'wanted', 'damn', 'below', 'about', 'than', 'past', 'look', 'gets',
                 'thursday', 'hardly', 'first', 'enough', 'thanks', 'which', 'edu', 'take', 'but', 'into', 'sent',
                 'whole', 'off']

    list_words = []

    message_with_spaces = ''

    message = file.read().lower()

    for character in message:
        if character not in characters_allowed:
            message_with_spaces += ' '
        else:
            message_with_spaces += character

    list_words = str.split(message_with_spaces, ' ')
    list_words = [word for word in list_words if len(word) > 2]  # Delete not-long-enough words
    list_words = list(set(list_words))  # Remove duplicate words

    cleared_list_words = []

    for word in list_words:
        if word not in blacklist:
            cleared_list_words.append(word)

    list_words = cleared_list_words

    file.close()

    return list_words


def get_prob_from_theme(theme_dico, words_list):
    """Return percentage for links between the text and the theme.
    Parameters
    ----------
    theme_dico: dictionary containing all words and their probabilities
    for a given theme
    theme_dico= {word1:[prob, anti-prob], word2:...}

    words_list: all the words of the text (list)

    Return
    ------
    prob_1: the probabilities of being in theme (float)

    """

    from math import log

    # compute probabilities
    probability = 0
    for word in theme_dico:
        # multiplicate the probabilities by the percentage of appeared word

        # slightly modify probabilities to stay in the log function domain
        if theme_dico[word] == (0, 1):
            theme_dico[word] = (0.0000000001, 0.9999999999)
        elif theme_dico[word] == (1, 0):
            theme_dico[word] = (0.9999999999, 0.0000000001)

        if word in words_list:
            probability += log(theme_dico[word][0])
        # multiplicate the probabilities by the percentage of unappeared word
        else:
            probability += log(theme_dico[word][1])

    for word in words_list:
        if word not in theme_dico:
            #  This word doesn't appear in any sorted text of this theme (so it isn't in the theme_dico)
            probability += log(0.0000000001)
    return probability


def get_theme(probabilities, most_probable_theme=('', None)):
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
    if most_probable_theme[1] is None or probabilities[0][1] > most_probable_theme[1]:
        # Checks for a new highest probability
        most_probable_theme = probabilities[0]

    # Calls get_theme() to analyse the next element of list probabilities
    return get_theme(probabilities[1:], most_probable_theme)


def sort(probabilities, path):
    """ For each file, place it within the correct repertory.
    Parameters
    ----------
    probabilities : dictionary which for each file returns both its probabilities to be
    or not to be in a theme
    probabilities= {"theme1":{"word1":(prob, antiprob), "word2":(prob, antiprob),...}, "theme2":...}

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
        text_theme_probs = []
        theme_prob = []
        for theme in probabilities:
            text_theme_probs = get_prob_from_theme(probabilities[theme], words)
            theme_prob += [(theme, text_theme_probs)]

        # Get the most probable theme
        file_theme = get_theme(theme_prob)

        # Move file to the correct repertory
        os.rename(path + '/unsorted/' + file, path + '/sorted/' + str(file_theme) + '/' + file)
