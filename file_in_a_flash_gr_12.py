import learn
import sort

def files_in_a_flash(path):
    """
    PARAMETERS:
    -----------
    path: the path to the emplacement of the archives file in memory
    """
    probabilities = learn.learn(path)
    sort.sort(probabilities, path)
