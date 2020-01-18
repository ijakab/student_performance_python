import dataset
import preprocess
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


data_train = dataset.getTrainDataset()
data_test = dataset.getTestDataset()
X_train = preprocess.get_x(data_train)
X_test = preprocess.get_x(data_test)
Y_train = preprocess.get_y(data_train)
Y_test = preprocess.get_y(data_test)


models = {
    'linearRegression': LinearRegression()
}

for modelName in models:
    # train a model
    models[modelName].fit(X_train, Y_train)

    # predict test data
    Y_test_predicted = models[modelName].predict(X_test)
    MSE = mean_squared_error(Y_test, Y_test_predicted)
    print(f'MSE for {modelName} is {MSE}')
