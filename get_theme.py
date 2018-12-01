def get_theme(probabilities, most_probable_theme):
    """
    Finds the theme of an article by comparing the probabilities of each theme.
    Parameters:
    -----------
    probabilities: list containing a tuple for each theme in the form (theme, probability)
    most_probable_theme: tuple containing the most probable theme found so far and it's probability

    Return:
    -------
    theme : the most probable theme

    Notes:
    ------
    This function is recursive

    Example:
    --------
    >>> get_theme([('sport', 0.4), ('politics', 0.5), ('animals', 0.85)])
    'animals'
    """

    # --- Basic case ---
    if not probabilities:
        # If the probability list is empty, we return the most probable theme found so far
        return most_probable_theme[0]

    # --- Recursive case ---
    if probabilities[0][1] > most_probable_theme[1]:
        # Checks for a new highest probability
        most_probable_theme = probabilities[0][1]

    # Calls get_theme() to analyse the next element of list probabilities
    return get_theme(probabilities[1:], most_probable_theme)
