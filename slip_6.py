import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


data_set = pd.read_csv("C:\\Users\shahbaz khan\\Downloads\\Position_Salaries.csv")


x = data_set.iloc[:, 1:2].values
y = data_set.iloc[:, 2].values


data_set.head()


lin_regs = LinearRegression()
lin_regs.fit(x, y)


LinearRegression(copy_X =  True, fit_intercept =True, n_jobs=None, normalize=False )
mtp.scatter(x,y,color="blue")
mtp.plot(x, lin_regs.predict(x), color="red")
mtp.title("Salary estimation model using Linear Regression")
mtp.xlabel("Postion Levels")
mtp.ylabel("Salary")
mtp.show()


#Fitting the Polynomial regression of degree-2 to the dataset 
poly_regs= PolynomialFeatures(degree= 2)
x_poly = poly_regs.fit_transform(x) 
lin_reg_2 =LinearRegression()
lin_reg_2.fit(x_poly, y)


#visulaizing the result for Polynomial Regression of degree-2 mtp.scatter(x,y,color="blue")


mtp.plot(x, lin_reg_2.predict(poly_regs.fit_transform(x)), color="red") 
mtp.title("Salary estimation model Polynomial Regression of degree=2") 
mtp.xlabel("Position Levels")
mtp.ylabel("Salary")
mtp.show()


#Fitting the Polynomial regression of degree-3 to the dataset 
poly_regs= PolynomialFeatures(degree= 2)
x_poly = poly_regs.fit_transform(x) 
lin_reg_3 =LinearRegression()
lin_reg_3.fit(x_poly, y)


#visulaizing the result for Polynomial Regression of degree-3 mtp.scatter(x,y,color="blue")


mtp.plot(x, lin_reg_3.predict(poly_regs.fit_transform(x)), color="red") 
mtp.title("Salary estimation model Polynomial Regression of degree=3") 
mtp.xlabel("Position Levels")
mtp.ylabel("Salary")
mtp.show()


#Fitting the Polynomial regression of degree-4 to the dataset 
poly_regs=PolynomialFeatures(degree= 2)
x_poly = poly_regs.fit_transform(x) 
lin_reg_4 =LinearRegression()
lin_reg_4.fit(x_poly, y)


#visulaizing the result for Polynomial Regression of degree-4 mtp.scatter(x,y,color="blue")


mtp.plot(x, lin_reg_4.predict(poly_regs.fit_transform(x)), color="red") 
mtp.title("Salary estimation model Polynomial Regression of degree=4") 
mtp.xlabel("Position Levels")
mtp.ylabel("Salary")
mtp.show()
lin_pred = lin_regs.predict([[6.5]])
print(lin_pred)
poly_pred =lin_reg_2(poly_regs.fit_transform([[6.5]]))
print(poly_pred)
poly_pred =lin_reg_3(poly_regs.fit_transform([[6.5]]))
print(poly_pred)
poly_pred =lin_reg_4(poly_regs.fit_transform([[6.5]]))
print(poly_pred)