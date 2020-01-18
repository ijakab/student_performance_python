from sklearn.preprocessing import MinMaxScaler
import pandas


TRACKED_FEATURES = ['age','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','traveltime','studytime','activities','higher','internet','romantic','freetime','goout','Dalc','Walc','absences']
PREDICT_VALUE = 'G3'

strMap = {
    "sex": {'M': 0, 'F': 1},
    "address": {'U': 0, 'R': 1},
    "famsize": {'LE3': 0, 'GT3': 1},
}


def preprocess(dataframe):
    # select only some columns
    tracked_columns = TRACKED_FEATURES.copy()
    tracked_columns.append(PREDICT_VALUE)
    dataframe = dataframe[tracked_columns]

    # convert text to numeric
    for key in strMap:
        print(key)

    # remove incomplete columns
    dataframe = dataframe.dropna()

    # normalize data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(dataframe.values)
    dataframe = pandas.DataFrame(scaled)

    return dataframe
