import dataset
import preprocess
from sklearn.linear_model import LinearRegression, BayesianRidge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor


data_train = dataset.getTrainDataset()
data_test = dataset.getTestDataset()
X_train = preprocess.get_x(data_train)
X_test = preprocess.get_x(data_test)
Y_train = preprocess.get_y(data_train)
Y_test = preprocess.get_y(data_test)


models = {
    'Linear Regression': LinearRegression(),
    'Bayesian Ridge': BayesianRidge(compute_score=True),
    'Lasso': Lasso(alpha=0.1),
    'Random Forest': RandomForestRegressor(max_depth=2, random_state=0),
    'Multilayer Perceptron': MLPRegressor()
}

for modelName in models:
    # train a model
    models[modelName].fit(X_train, Y_train)

    # predict test data
    Y_test_predicted = models[modelName].predict(X_test)
    MSE = mean_squared_error(Y_test, Y_test_predicted)
    print(f'MSE for {modelName} is {MSE}')


def predict_all(dataframe):
    result = {}
    X = preprocess.get_x(dataframe)
    for modelName in models:
        result[modelName] = models[modelName].predict(X)
    return result
