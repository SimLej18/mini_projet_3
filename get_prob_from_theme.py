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
        # Add the percentage of appeared word to the probabilities
        if word in words_list:
            probability += log(theme_dico[word][0])
        # Add the percentage of unappeared word to the probabilities
        else:
            probability += log(theme_dico[word][1])
    return probability
