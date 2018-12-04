def get_occurence(path):
    """Determines how often a word appears in the texts of each theme.
    
    Parameters:
    ----------
    path: The path to the theme (str)
    
    Returns:
    -------
    words_occurence: The probability that a word is found in the texts of a theme (dict)
    """

    words_occurence = {}
    word_list = get_words_theme(path)
    text_list = os.listdir(path)

    dico_words = {}

    number_texts = 0

    for text in text_list:
        dico_words.update({text : get_words_in_file(path + "/" + text)})
        number_texts += 1

    for word in word_list: 
        words_found = 0
        for text in text_list:       
            if word in dico_words[text]:
                words_found += 1

        appearance = words_found / number_texts
        words_occurence.update({word: ("%.5f" % appearance, "%.5f" % (1 - appearance))})

    return words_occurence
