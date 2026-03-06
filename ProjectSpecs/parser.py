"""The main parser for our project."""

import pandas as pd



def read_file_subset(filepath, subset=[]):
    """reads the given CSV and returns a dataframe

        Input: 
            - Filepath : path to the file
            - subset : LIST of column names that you want to keep (default is all)
        Output:
            - Dataframe with your csv read, data is NOT cleaned
    """

    # read the file
    df = pd.read_csv(filepath)

    # extract subset of data we want to work with if any
    if not subset:
        return df
    else:
        return df[subset]