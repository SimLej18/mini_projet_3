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

    file = open(path, 'r')

    characters_allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    blacklist = ['the', 'be', 'are', 'of', 'and', 'a', 'in', 'that', 'have', 's', 'i', 'it', 'but',\
    'etc', 'to', 'for', 'not', 'on', 'with', 'has', 'he', 'as', 'you', 'do', 'at', 'this', 'his',\
    'by', 'from', 'they', 'we', 'say', 'her', 'she', 'on', 'an', 'will', 'my', 'one', 'all',\
    'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',\
     'which', 'me', 'when', 'make', 'can', 'like', 'no', 'just', 'him', 'know', 'take',\
     'into', 'your', 'good', 'same', 'should', 'them', 'see', 'other', 'than', 'then',\
     'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after',\
      'use', 'two', 'how', 'our', 'first', 'well', 'way', 'even', 'new', 'want',\
     'because', 'any', 'these', 'give', 'day', 'most', 'us', 'few', 'bye',\
     'regards', 'mr', 'ms', 'is', 'or', 'dt', 't', 'q', 'why', 'am', 'p', 'had', 'some', 've', \
     're', 'thanks', 'once', '', '']

    list_words = []

    counter = 1

    message = file.read()

    while counter != len(message):
        # A word is starting
        if message[counter - 1] not in characters_allowed \
        and message[counter] in characters_allowed:
            while message[counter] in characters_allowed: # While the word is not "finished"
                word += message[counter]
                counter += 1

            word = word.lower()

            if word not in blacklist and len(word) > 2:
                list_words.append(word) # The word is added to the list

        counter += 1

    file.close()

    return list_words


def get_words_theme(path):
    """ Returns all the words of a theme
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

def learn(path):
    """ For every theme in a directory, ...

        Parameters:
        ----------
        path: the path to the directory containing the themes (str)

        Returns:
        -------
        probabilities:dictionary of which
                        - keys are the different themes and
                        - values are dictionaries of which
                                      - keys are the different words and
                                      -values are a tuple of the type (probability, non-probability)
    """

    probabilities = {}

    for directory in os.listdir(path):
        dict_probabilities = get_occurence(path + '/' + directory)
        probabilities.update({directory : dict_probabilities})
    return probabilities
   
