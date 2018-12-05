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

    characters_allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    blacklist = [' ', 'the', 'be', 'are', 'of', 'and', 'a', 'in', 'that', 'have', 's', 'i', 'it', 'but', 'etc', 'to',
                 'for', 'not', 'on', 'with', 'has', 'he', 'as', 'you', 'do', 'at', 'this', 'his', 'by', 'from', 'they',
                 'we', 'say', 'her', 'she', 'on', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
                 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'me', 'when', 'make', 'can', 'like', 'no',
                 'just', 'him', 'know', 'take', 'into', 'your', 'good', 'same', 'could', 'them', 'see', 'other', 'than',
                 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two',
                 'how', 'our', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day',
                 'most', 'us', 'few', 'bye', 'regards', 'mr', 'ms', 'is', 'or', 'dt', 't', 'q', 'why', 'am', 'p', 'had',
                 'some', 've', 're', 'thanks', 'once', '', '']

    list_words = []

    message_with_spaces = ''

    message = file.read().lower()

    for character in message:
        if character not in characters_allowed:
            message_with_spaces += ' '
        else:
            message_with_spaces += character

    list_words = str.split(message_with_spaces, ' ')

    for word in list_words:
        if word in blacklist:
            list_words.remove(word)

    list_words = list(filter(None, list_words))  # Deletes empty strings

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
