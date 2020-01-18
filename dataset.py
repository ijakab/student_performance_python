import pandas
from numpy import random
from preprocess import preprocess

SPLIT_RATE = 0.8

random.seed(12)
dataframe_original = pandas.read_csv('./dataset.csv', sep=r'\s*;\s*', engine='python')
dataframe_dropped = dataframe_original.dropna()
dataframe = preprocess(dataframe_dropped)

# split train and test data
mask = random.rand(len(dataframe)) < SPLIT_RATE
train = dataframe[mask]
test = dataframe[~mask]


def getFullDataset():
    return dataframe


def getTrainDataset():
    return train


def getTestDataset():
    return test
