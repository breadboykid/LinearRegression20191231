import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error

dataframe = pd.read_csv("student_scores.csv")

X = dataframe["Hours"].values.reshape(-1, 1)
Y = dataframe["Scores"].values.reshape(-1, 1)

plt.title("Exam Results")
plt.suptitle("King's College London")
plt.xlabel("Hours spent studying")
plt.ylabel("Student Score")

trainingCount = math.floor(len(dataframe) * 0.8)
testCount = len(dataframe) - trainingCount
X_train, Y_train = X[0:trainingCount], Y[0:trainingCount]
X_test, Y_test = X[trainingCount-1:], Y[trainingCount-1:]

model = LinearRegression()
reg = model.fit(X_train, Y_train)
regressionLine = model.predict(X)

plt.plot(X, regressionLine)

plt.plot(X_train, Y_train, 'o')
plt.plot(X_test, Y_test, 'o')
plt.show()

y_predictions = model.predict(X_test)

print(mean_squared_error(Y_test, y_predictions))

