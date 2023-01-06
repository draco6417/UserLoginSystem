import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# Reading the dataset
dataset = pd.read_csv("C:\\Users\\shahbaz khan\\Downloads\\advertising.csv")
dataset.head()
# Setting the value for X and Y
x = dataset[['TV', 'Radio', 'Newspaper']]
y = dataset['Sales']
#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)
# Fitting the Multiple Linear Regression model
mlr = LinearRegression()
mlr.fit(x_train, y_train)
#Intercept and Coefficient
# Printing the model coefficients
print(mlr.intercept_)
# pair the feature names with the coefficients
list(zip(x, mlr.coef_))
# Predicting the Test and Train set result
y_pred_mlr = mlr.predict(x_test)
x_pred_mlr = mlr.predict(x_train)
print("Prediction for test set: {}".format(y_pred_mlr))
# Actual value and the predicted value
mlr_diff = pd.DataFrame(
    {'Actual value': y_test, 'Predicted value': y_pred_mlr})
mlr_diff
# Predict for any value
mlr.predict([[56, 55, 67]])
# print the R-squared value for the model
print('R squared value of the model: {:.2f}'.format(mlr.score(x, y)*100))
# 0 means the model is perfect. Therefore the value should be as close to 0 as possible
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))


print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)