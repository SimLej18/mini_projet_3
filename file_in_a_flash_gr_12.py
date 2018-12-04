import learn
import sort
from check_accuracy import *


def files_in_a_flash(path):
    """
    PARAMETERS:
    -----------
    path: the path to the emplacement of the archives file in memory
    """
    # probabilities = learn.learn(path+'/sorted')
    # sort.sort(probabilities, path)


files_in_a_flash('/Users/simonlejoly/Documents local/Project/Archives/archive_2')
accuracy = check_accuracy('/Users/simonlejoly/Documents local/Project/Archives')
print('The sort AI has a %.3f %% of accuracy' % accuracy)
