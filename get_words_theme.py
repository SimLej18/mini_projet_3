def get_words_theme(path):
    """Returns all the words of a theme
    
    Parameters:
    ----------
    path : the path to the theme (str)

    Returns:
    --------
    list_words : list of all the words of the theme (list)

    """

    list_words = []
    text_list = os.listdir(path)
    
    for text in text_list:
        list_words.extend(get_words_in_file(path + "/" + text))

    list_words = list(set(list_words)) # Remove duplicate words
    
    return list_words
