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
    word_list = get_word_theme(theme)
    text_list = os.listdir("./sorted/" + theme)

    for word in word_list:
        number_texts = 0
        word_found = 0
        for text in text_list:
            number_texts += 1
            if word in get_words_in_file("./sorted/" + theme + "/" + text):
                word_found += 1
            else:
                word_found += 0

        appearance = word_found / number_texts
        no_appearance = 1 - appearance
        words_occurence.update({word: ("%.1f" % appearance, "%.1f" % no_appearance)})

    return words_occurence