import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#% matplotlib inline
from sklearn import linear_model
import warnings
warnings.filterwarnings("ignore")

#importing data from the file
income_sheet = pd.read_csv("canada_per_capita_income.csv")
print(income_sheet.head(3))

#02-->step-->draw a graph using matplotlib
# plt.scatter(income_sheet.year,income_sheet.income)
# plt.xlabel("Year",fontsize=20)
# plt.ylabel("Income",fontsize=20)
# plt.title("Prediction Income of canada",color='red')
# plt.show()

#step three train the data
model = linear_model.LinearRegression()
model.fit(income_sheet[['year']],income_sheet.income)

income_prediction = [[2030]]
print(model.predict(income_prediction))

#Make a graph between actual values and predicted values
# plt.scatter(income_sheet.year,income_sheet.income,color='red')
# plt.plot(income_sheet.year,model.predict(income_sheet[['year']]))
# plt.title("Annual Income if Canada", fontsize=30)
# plt.xlabel("Year",fontsize=20)
# plt.ylabel("Income (US $)",fontsize=20)
# plt.show()