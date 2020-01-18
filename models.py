import dataset
from sklearn.linear_model import LinearRegression

data_train = dataset.getTrainDataset()
data_test = dataset.getTestDataset()
X_train = dataset.getX(data_train)
X_test = dataset.getX(data_train)

linearRegression = LinearRegression()
