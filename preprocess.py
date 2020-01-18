from sklearn.preprocessing import MinMaxScaler
import pandas


TRACKED_FEATURES = ['age','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','traveltime','studytime','activities','higher','internet','romantic','freetime','goout','Dalc','Walc','absences']
PREDICT_VALUE = 'G3'

strMap = {
    "sex": {'M': 0, 'F': 1},
    "address": {'U': 0, 'R': 1},
    "famsize": {'LE3': 0, 'GT3': 1},
    "Pstatus": {'T': 0, 'A': 1},
    'Mjob': {'teacher': 0, 'health': 1, 'services': 2, 'at_home': 3, 'other': 4},
    'Fjob': {'teacher': 0, 'health': 1, 'services': 2, 'at_home': 3, 'other': 4},
    'activities': {'yes': 1, 'no': 0},
    'higher': {'yes': 1, 'no': 0},
    'internet': {'yes': 1, 'no': 0},
    'romantic': {'yes': 1, 'no': 0},
}


def preprocess(dataframe):
    # select only some columns
    tracked_columns = TRACKED_FEATURES.copy()
    tracked_columns.append(PREDICT_VALUE)
    dataframe = dataframe[tracked_columns]

    # convert text to numeric
    for key in strMap:
        dataframe[key] = [strMap[key][item] for item in dataframe[key]]

    # normalize data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(dataframe.values)
    dataframe = pandas.DataFrame(scaled)

    return dataframe
