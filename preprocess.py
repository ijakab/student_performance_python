from sklearn.preprocessing import MinMaxScaler
import pandas

TRACKED_FEATURES = ['age','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','traveltime','studytime','activities','higher','internet','romantic','freetime','goout','Dalc','Walc','absences']
#sample = [15,"F","U","LE3","T",3,4,"health","teacher",2,3,"yes","no","yes","yes",1,3,2,4,23]
PREDICT_VALUE = 'G3'
tracked_columns = TRACKED_FEATURES.copy()
tracked_columns.append(PREDICT_VALUE)

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
    dataframe = dataframe[tracked_columns]

    # convert text to numeric
    for key in strMap:
        dataframe[key] = [strMap[key][item] for item in dataframe[key]]

    # normalize data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(dataframe.values)
    dataframe_scaled = pandas.DataFrame(scaled, columns=dataframe.columns.tolist())

    return dataframe_scaled


def get_x(dataframe):
    return dataframe[TRACKED_FEATURES]


def get_y(dataframe):
    return dataframe[PREDICT_VALUE]


def preprocess_and_get_x(dataframe):
    preprocessed = preprocess(dataframe)
    return get_x(preprocessed)


def dataframe_from_features(features):
    new_dataframe = pandas.DataFrame(columns=tracked_columns)
    new_dataframe.loc[0] = features
    return new_dataframe
