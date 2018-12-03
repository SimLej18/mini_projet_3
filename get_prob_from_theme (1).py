import math 
def get_prob_from_theme(theme_list, text_list):
    """Return pourcentage for links between the text and the theme.
    Parameters
    ----------
    theme_list: list of theme checked (list)
    text_list: text with all the word in the text (list)
    
    Return
    ------
    prob_1: the probabilities of being in theme (float)

    """
    sibling_word=[]
    #check word by word
    for word_text in text_list:
        if word_text in theme_list:
            sibling_word.append(word_text)
    
    #compute probabilities
    prob_1 = 0
    for prob in sibling_word:
        #multiplicate the probabilities by the pourcentage of appeared word
        prob_1 += math.log(theme_list[prob][0])
    for prob in theme_list:
        #multiplicate the probabilities by the pourcentage of unappeared word 
        if not prob in sibling_word:
            prob_1 += math.log(theme_list[prob][1])
    return prob_1