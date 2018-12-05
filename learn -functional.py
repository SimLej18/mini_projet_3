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

    file = open(path, 'r', encoding="ISO-8859-1")

    characters_allowed = 'abcdefghijklmnopqrstuvwxyz'
    blacklist = ['come', 'because', 'once', 'may', 'too', 'best', 'thereby', 'after', 'don',
                 'these', 'gone', 'only', 'shall', 'new', 'against', 'out', 'sunday', 'isn',
                 'where', 'always', 'him', 'without', 'very', 'does', 'email', 'quite',
                 'never', 'before', 'entirely', 'anyways', 'still', 'lines', 'monday', 'thank',
                 'myself', 'from', 'over', 'yet', 'were', 'just', 'will', 'see', 'anymore',
                 'let', 'while', 'wednesday', 'later', 'must', 'your', 'itself', 'well',
                 'although', 'use', 'many', 'thought', 'them', 'when', 'have', 'even', 'having',
                 'tell', 'however', 'himself', 'what', 'mail', 'going', 'yes', 'regards', 'com',
                 'got', 'his', 'between', 'reply', 'makes', 'two', 'want', 'more', 'not', 'etc',
                 'though', 'someone', 'one', 'could', 'right', 'that', 'neither', 'did', 'saturday',
                 'much', 'something', 'get', 'used', 'like', 'think', 'didn', 'most', 'wouldn',
                 'haven', 'instead', 'same', 'guess', 'some', 'anything', 'those', 'this', 'make',
                 'know', 'both', 'you', 'need', 'then', 'either', 'subject', 'with', 'say',
                 'largest', 'made', 'back', 'would', 'actually', 'good', 'few', 'way', 'doing',
                 'tuesday', 'had', 'left', 'nothing', 'should', 'friday', 'might', 'and', 'are',
                 'per', 'rather', 'they', 'little', 'since', 'her', 'own', 'she', 'bye', 'lot',
                 'ones', 'give', 'actual', 'others', 'each', 'until', 'was', 'likely', 'said',
                 'can', 'please', 'who', 'why', 'other', 'our', 'enable', 'half', 'perhaps', 'for',
                 'simple', 'the', 'now', 'means', 'anyone', 'day', 'sorry', 'ought', 'any', 'wrong',
                 'been', 'their', 'also', 'has', 'unless', 'all', 'how', 'better', 'there', 'here',
                 'mostly', 'its', 'things', 'late', 'wanted', 'damn', 'below', 'about', 'than',
                 'past', 'look', 'gets', 'thursday', 'hardly', 'first', 'enough', 'thanks', 'which',
                 'edu', 'take', 'but', 'into', 'sent', 'whole', 'off']

    message_with_spaces = ''

    message = file.read().lower()

    for character in message:
        if character not in characters_allowed:
            message_with_spaces += ' '
        else:
            message_with_spaces += character

    list_words = str.split(message_with_spaces, ' ')
    list_words = [word for word in list_words if len(word) > 2]  # Delete not-long-enough words
    list_words = list(set(list_words))  # Remove duplicate words

    cleared_list_words = []

    for word in list_words:
        if word not in blacklist:
            cleared_list_words.append(word)

    list_words = cleared_list_words

    file.close()

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

    text_list = os.listdir(path)

    words_occurence = {}

    for text in text_list:
        for word in get_words_in_file(path + '/' + text):
            if word in words_occurence:
                words_occurence[word] += 1
            else:
                words_occurence[word] = 1

    for element in words_occurence:
        words_occurence[element] /= len(text_list)

        # Put the elements in the form (Probability, Anti-probability)
        words_occurence[element] = (words_occurence[element], 1 - words_occurence[element])

    return words_occurence


def learn(path):
    """ For every theme in a directory, ...
        Parameters:
        ----------
        path: the path to the directory containing the themes (str)
        Returns:
        -------
        probabilities: dicionary of which
                        -keys are the different themes and
                        -values are dictionaries of which
                                      -keys are the different words and
                                      -values are a tuple of the type (probability, non-probability)
    """

    probabilities = {}

    for directory in os.listdir(path):
        dict_probabilities = get_occurence(path + '/' + directory)
        probabilities.update({directory: dict_probabilities})
        
    return probabilities
