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
    
    # A blacklist of the most common English words 
    blacklist = ['the','be','are','of','and','a','in','that','have','s','i','it','but','etc','to','for','not','on','with','has','he','as','you','do','at','this','his','by','from','they','we','say','her','she','on','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','me','when','make','can','like','no','just','him','know','take','into','your','good','same','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','first','well','way','even','new','want','because','any','these','give','day','most','us','few','bye','regards','mr','ms','is','or','dt','t','q','why','am','p','had','some','ve','re','thanks','once','','']

    list_words = []

    character_index = 1

    message = file.read()

    while character_index != len(message):
        if message[character_index - 1] not in characters_allowed and message[character_index] in characters_allowed: # A word is starting
            word = ''
            while message[character_index] in characters_allowed: # While the word is not "finished"
                word += message[character_index]
                character_index += 1

            word = word.lower()

            if word not in blacklist and len(word) > 2:
                list_words.append(word) # The word is added to the list

        character_index += 1

    file.close()

    return list_words
