import os


def sort(probabilities, path):
    """ For each file, place it within the correct repertory.
    Parameters
    ----------
    probabilities : dictionary which for each file returns both its probabilities to be or not to be in a theme
    probabilities = {"theme1":{"word1": (prob, antiprob), "word2": (prob, antiprob), ...}, "theme2": ...}

    path : the path of the repertory where archives can be found

    """

    # Initialize all themes
    themes = ()
    for key in probabilities:
        themes += key

    for file in os.listdir(os.getcwd() + 'unsorted/'):
        # Get all the words used in the file
        words = get_words(path + 'file')

        # Get all the probabilities for the file to be in one theme
        theme_probabilities = get_prob_from_theme(themes, words)

        # Get the most probable theme
        file_theme = get_theme(theme_probabilities, 0)

        # Move file to the correct repertory
        os.rename(os.getcwd() + 'unsorted/' + file, os.getcwd() + 'sorted/' + file_theme + '/' + file)
