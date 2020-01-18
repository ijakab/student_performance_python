import pandas
from numpy import random


TRACKED_FEATURES = ['age','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','traveltime','studytime','activities','higher','internet','romantic','freetime','goout','Dalc','Walc','absences']
PREDICT_VALUE = 'G3'
SPLIT_RATE = 0.8

random.seed(12)
dataframe = pandas.read_csv('./dataset.csv', sep=r'\s*;\s*')

#select only some columns
tracked_columns = TRACKED_FEATURES.copy()
tracked_columns.append(PREDICT_VALUE)
dataframe = dataframe[tracked_columns]

#remove incomplete columns
dataframe = dataframe.dropna()

mask = random.rand(len(dataframe)) < SPLIT_RATE
train = dataframe[mask]
test = dataframe[~mask]


def getFullDataset():
    return dataframe


def getTrainDataset():
    return train


def getTestDataset():
    return test


def getX(df):
    print(df)