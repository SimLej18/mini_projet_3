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
