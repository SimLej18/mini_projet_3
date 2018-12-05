def check_accuracy(path):
    """
    Analyse the content of directories in sorted directory and check
    that each file is were it is intended to be.

    Parameters:
    -----------
    path: sorted directory location in computer (str)

    Return:
    -------
    accuracy: number between 0 and 100 representing the percentage of
    well-placed files.
    """

    from os import listdir
    import os.path

    well_placed_files = 0
    badly_placed_files = 0

    archives = listdir(path)

    archives.remove('.DS_Store')  # To prevent weird bug adding a ghost file in archives

    for archive in archives:
        labels = open(path+'/'+archive+'/labels.txt', 'r').readlines()

        # Checks that file classed in labels.txt is well_placed
        for label in labels:
            file_id, theme = label.split(' ')
            theme = theme[:-1]  # remove the carriage return at the end of theme

            if os.path.exists(path+'/'+archive+'/sorted/'+theme+'/'+file_id):
                well_placed_files += 1
            else:
                badly_placed_files += 1

    # To prevent division by zero, checks that both variables don't worth 0
    if not well_placed_files * badly_placed_files == 0:
        return well_placed_files/(well_placed_files + badly_placed_files) * 100, (well_placed_files, badly_placed_files)
    return 0, (0, 0)
