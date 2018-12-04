def get_occurence(theme):
    """Determines how often a word appears in the texts of each theme.
    Parameters
    ----------
    theme: The themes checked (str)
    Returns
    -------
    words_occurence: The probability that a word is found in the texts of a theme (dic)
    """

    words_occurence = {}
    word_list = get_words_theme(theme)
    text_list = os.listdir("D:/Programmation/UNamur/Mini-projet 3/Archives/archive_1/sorted/" + theme)

    words = 0

    dico_words = {}

    number_texts = 0

    for text in text_list:
        dico_words.update({text : get_words_in_file("D:/Programmation/UNamur/Mini-projet 3/Archives/archive_1/sorted/" + theme + "/" + text)})
        number_texts += 1

    for word in word_list:
        words += 1 
        words_found = 0
        for text in text_list:       
            if word in dico_words[text]:
                words_found += 1

        appearance = words_found / number_texts
        words_occurence.update({word: ("%.5f" % appearance, "%.5f" % (1 - appearance))})

    return words_occurence
