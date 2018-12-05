import learn
import sort
from check_accuracy import *
import time


def files_in_a_flash(path):
    """
    PARAMETERS:
    -----------
    path: the path to the emplacement of the archives file in memory
    """
    probabilities = learn.learn(path+'/sorted')
    sort.sort(probabilities, path)


start_time = time.clock()
files_in_a_flash('/Users/simonlejoly/Documents local/Project/Archives/archive_4')
accuracy, placed_files_info = check_accuracy('/Users/simonlejoly/Documents local/Project/Archives')
end_time = time.clock()

print('The sort AI has a %.3f %% of accuracy (%d well placed files, %d badly placed files)'
      % (accuracy, placed_files_info[0], placed_files_info[1]))

nb_hours = int(end_time-start_time) // 3600
nb_min = (int(end_time-start_time) % 3600) // 60
nb_sec = (int(end_time-start_time) % 60)
print('Process took %d h %d min %d sec' % (nb_hours, nb_min, nb_sec))
