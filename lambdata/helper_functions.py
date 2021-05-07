"""Python file containing a package of functions created with
helper functions for LS DS Unit 3, Sprint 1
This file is under construction, but I tried to make sure that
the requirements for the assignment were at least met so I could
tinker with this more later, as time allows.
"""


# Future revisions will substitute functional code for the passes
# below, but I wanted to sketh the overarching idea first. 
class DataFrameHelper:
    """This class containss helper functions for a dataframe.
    Parameters are df, frac, seed, addy_series
    """
    
    
    def __init__(self, df=None, frac=.33, seed=73):
        
        self.df = df
        self.frac = frac
        self.seed = seed


    def null_count(self):
        '''This function checks the dataframe for null values.
        Parameter is a dataframe.
        Returns an integer that is the total count of null values.'''

        count = self.df.isnull().sum().sum()

        return count


    def train_test_split(df, frac=0.33, seed=73):
        pass                                    # come back to this later
        # test = df.sample(frac=frac, random_state=seed)
        # train = df.loc
        # return (train, test)


    def randomize():
        '''This function is meant to randomize, or shuffle the rows of
        a dataframe (by the index) preserving the observations, but
        changing the order in which they appear.
        Parameters are a Pandas dataframe and integer to be used as
        a random seed.
        Returns the "shuffled" dataframe.
        '''

        # Shuffle the df by using pd.sample and frac set to 1 to sample
        # the entire dataframe
        new_df = self.df.sample(frac=1, random_state=seed)
        
        return new_df


class SeriesHelper:
    """This class containss helper functions for a series.
    Parameter is a series.
    """


    def __init__(self, series):
        self.series = series


    def addy_split(self):
        pass


    def abbr_2_st(self, abbr_2_st=True):
        pass


    def list_2_series(self, df):
        pass


    def split_dates(self):
        pass