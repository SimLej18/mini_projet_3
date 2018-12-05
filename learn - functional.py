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
    blacklist = ['without','com','subject','lines','the','be','are','of','and','a','in','that','have','s','i','it','but','etc','to','for','not','on','with','has','he','as','you','do','at','this','his','by','from','they','we','say','her','she','on','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','me','when','make','can','like','no','just','him','know','take','into','your','good','same','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','first','well','way','even','new','want','because','any','these','give','day','most','us','few','bye','regards','mr','ms','is','or','dt','t','q','why','am','p','had','some','ve','re','thanks','once','','']

    list_words = []

    message_with_spaces = ''

    message = file.read().lower()

    for character in message:
        if character not in characters_allowed:
            message_with_spaces += ' '
        else:
            message_with_spaces += character


    list_words = str.split(message_with_spaces, ' ')
    

    list_words = list(filter(None, list_words))  # Delete empty strings
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
                        - keys are the different themes and 
                        - values are dictionaries of which
                                      - keys are the different words and 
                                      - values are a tuple of the type (probability, non-probability)
    """

    probabilities = {}

    for directory in os.listdir(path):
        dict_probabilities = get_occurence(path + '/' + directory)
        probabilities.update({directory : dict_probabilities})
        
    return probabilities
