import os

def get_words_theme(theme):
    """return all the words of a theme
    parameters:
    ----------
    theme : the theme (list)

    returns:
    --------
    list_word : list of all the word of the theme (list)

    """

    list_word = []
    text_list = os.listdir("./sorted/" + theme)
    for text in text_list:
        list_word.extend(get_words_in_file("./sorted/" + theme + "/" + text))

    list_word = list(set(list_word)) #remove duplicates words
    return list_word