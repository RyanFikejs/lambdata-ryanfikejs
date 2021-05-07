"""Python file containing a package of functions created with
helper functions for LS DS Unit 3, Sprint 1"""

import pandas as pd
import numpy as np

# Create a stock dataframe for testing functions in the repl
test_df = pd.read_csv('data/test.csv')

def null_count(df):
    '''This function checks the dataframe for null values.
    Parameter is a dataframe.
    Returns an integer that is the total count of null values.'''

    count = df.isnull().sum().sum()

    return count

def train_test_split(df, frac=0.33, seed=73):
    pass # come back to this later
    test = df.sample(frac=frac, random_state=seed)
    train = df.loc
    return (train, test)

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

def addy_split(addy_series):
    pass

def abbr_2_st(state_series, abbr_2_st=True):
    pass

def list_2_series(list_2_series, df):
    pass

def rm_outlier(df):
    pass

def split_dates(date_series):
    pass