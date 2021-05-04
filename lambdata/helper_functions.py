"""Python file containing a package of functions created with
helper functions for LS DS Unit 3, Sprint 1"""

def randomize(df, seed):
    '''This function is meant to randomize, or shuffle the rows of
    a dataframe (by the index) preserving the observations, but
    changing the order in which they appear.
    
    Parameters are a Pandas dataframe and integer to be used as
    a random seed.
    
    Returns the "shuffled" dataframe.'''

    # Shuffle the df by using pd.sample and frac set to 1 to sample
    # the entire dataframe
    df = df.sample(frac=1, random_state=seed)
    
    return df

def null_count(df):
    '''This function checks the dataframe for null values.

    Parameter is a dataframe.

    Returns an integer that is the total count of null values.'''

    count = df.isnull().sum().sum()

    return count