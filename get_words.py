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
    blacklist = ['the','be','are','of','and','a','in','that','have','s','i','it','but','etc','to','for','not','on','with','has','he','as','you','do','at','this','his','by','from','they','we','say','her','she','on','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','me','when','make','can','like','no','just','him','know','take','into','your','good','same','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','first','well','way','even','new','want','because','any','these','give','day','most','us','few','bye','regards','mr','ms','is','or','dt','t','q','why','am','p','had','some','ve','re','thanks','once','','']

    list_words = []

    counter = 1

    message = file.read()

    while counter != len(message):
        if message[counter - 1] not in characters_allowed and message[counter] in characters_allowed: # A word is starting
            word = ''
            while message[counter] in characters_allowed: # While the word is not "finished"
                word += message[counter]
                counter += 1

            word = word.lower()

            if word not in blacklist:
                list_words.append(word) # The word is added to the list

        counter += 1

    file.close()

    return list_words