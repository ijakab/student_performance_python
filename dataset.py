import pandas
from numpy import random

SPLIT_RATE = 0.8

random.seed(12)
dataframe = pandas.read_csv('./dataset.csv')

mask = random.rand(len(dataframe)) < SPLIT_RATE
train = dataframe[mask]
test = dataframe[~mask]


def getFullDataset():
    return dataframe

def getTrainDataset():
    return train

def getTestDataset():
    return test
