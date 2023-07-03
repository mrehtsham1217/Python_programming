import numpy as np
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

diabets = datasets.load_diabetes()
#print(diabets.keys())
#(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
#print(diabets.DESCR)
diabets_x = diabets.data[:,np.newaxis,2]
#print(diabets_x)
diabets_x_train = diabets_x[:-30]
diabets_x_test = diabets_x[-30:]

diabets_y_train = diabets.target[:-30]
diabets_y_test = diabets.target[-30:]
model = linear_model.LinearRegression()
model.fit(diabets_x_train,diabets_y_train)
diabets_y_predict = model.predict(diabets_x_test)
#Mean square error has two arguements first one is test data and second one is predicted data
print("Mean square value is : ",mean_squared_error(diabets_y_test,diabets_y_predict))
print("Weight: ",model.coef_)
print("Intercept:",model.intercept_)
plt.scatter(diabets_x_test,diabets_y_test)
plt.plot(diabets_x_test,diabets_y_predict)
plt.show()

"""
Mean square value is :  3035.060115291269
Weight:  [941.43097333]
Intercept: 153.39713623331644
"""
