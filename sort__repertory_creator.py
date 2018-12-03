import os 

def repertories_creator(theme_list):
    """ Create a repertory for each theme list (those present in a given 
    archive.
    
    Parameters
    -----------
    theme_list : list containing all the themes that can be found in a given 
    archive
    
    """
    
    for element in theme_list:
        path = os.getcwd() + '/' + element
        os.mkdir(path)
        

def sort(probabilities):

    """ For each file, place it within the correct repertory.
    Parameters
    ----------
    probabilities : dictionnary which for each file returns both its
    probabilities to be or not to be in a theme
    
    Notes
    -----
    
    Also create a repertory for each theme.
    
    """
    repertories_creator(theme_list)
    
    for key in probabilities:
        fh = open(key,r)
        source = os.getcwd()
        dest = get_theme(probabilities,most_probable_theme) + '/' + key
        os.rename(source,dest)
        
        
    
    
    
    