import pandas
from numpy import random
from kod.preprocess import preprocess

SPLIT_RATE = 0.8

random.seed(12)
dataframe_original = pandas.read_csv('./dataset.csv', sep=r'\s*;\s*', engine='python')
dataframe_dropped = dataframe_original.dropna()
dataframe = preprocess(dataframe_dropped)

#display info about dataset
print(dataframe_original.head())
print(len(dataframe_original))
dataframe_original.to_clipboard()


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
