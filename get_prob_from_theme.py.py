# -*- coding: utf-8 -*-
def get_prob_from_theme(theme_list, text_list):
    """Return a path? pourcentage? for links between the text and the theme.
    Parameters
    ----------
    theme_list: list of theme checked (list)
    text_list: text with all the word in the text (list)
    
    Return
    ------
    A écrire
    """
    sibling_word=[]
    #check word by word
    for word_theme in theme_list:
        for word_text in text_list:
            if word_text == word_text:
                sibling_word.append(word_text)
    
    #compute probabilities
    prob_1 = 1
    for prob in sibling_word:
        #multiplicate the probabilities by the pourcentage of appeared word
        prob_1 *= theme_list[prob][0]
    for prob in theme_list:
        #multiplicate the probabilities by the pourcentage of unappeared word 
        if not check_sibling(prob, sibling_word):
            prob_1 *= theme_list[prob][1]
            
    
            

def check_sibling(check_word, sibling_word):
    """Return True if the word is in both list. False otherwise
    Parameters
    ----------
    theme_list:
    sibling_word:
    
    Return
    ------
    True if the word is in both list
    False if isn't
    
    """
    #to do