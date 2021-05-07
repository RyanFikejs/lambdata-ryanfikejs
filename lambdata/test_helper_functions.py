"""Practice tests for helper functions"""
import pytest
import pandas as pd
from numpy import random
from lambdata.helper_functions import DataFrameHelper as dfh
from lambdata.helper_functions import SeriesHelper as sh


# Create several random dataframes for testing purposes
dfh_dict = {}
for n in range(1, 10):
    df = pd.DataFrame(random.randint(0,100,size=(60,5)),
        columns=list('ABCDE'))
    #TODO insert random number of NaN values into each df
    dfh_dict[f"dfh{n}"] = dfh(df)


### This first group of tests apply to the DataFrameHelper class
def test_null_count():
    """Testing the null count function"""
    for i in dfh_dict:
        total_nulls = 0
        for col in dfh_dict[i].df.columns:
            total_nulls += dfh_dict[i].df[col].isnull().sum()
            assert dfh_dict[i].null_count() == total_nulls

        assert dfh_dict[i].null_count().dtype == 'int64'


def test_train_test_split():
    """Testing the train/test set splitting function"""
    pass


def test_randomize():
    """Testing the randomize function"""
    pass


### This second group of tests apply to the SeriesHelper class
def test_addy_split():
    """Testing the address splitting function"""
    pass


def test_abbr_2_st():
    """Testing the state abbreviation function"""
    pass


def test_list_2_series():
    """Testing the 'list to series' function"""
    pass


def test_split_dates():
    """Testing the date splitting function"""
    pass