# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RPSDx17Vn4a9UpdA7A5bZdz34CQqjPm4
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt

sonar_data = pd.read_csv('sonar.csv', header=None)
x = sonar_data.iloc[:,:-1]
y = sonar_data.iloc[:,-1]

correlation_matrix = sonar_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Sonar Data Correlation Heatmap')
plt.show()

sonar_data.head()

sonar_data.tail()

sonar_data.shape

sonar_data.info()

sonar_data.isnull()

sonar_data.describe()

sonar_data.columns

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#label encoading
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#histographs
sonar_data.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1, figsize=(12,12))
pyplot.show()

# density
sonar_data.plot(kind='density', subplots=True, layout=(8,8), sharex=False, legend=False, fontsize=1, figsize=(12,12))
pyplot.show()

# box and whisker
#dataset.plot(kind='box', subplots=True, layout=(8,8), sharex=False, sharey=False, fontsize=1)
#pyplot.show()

# correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(sonar_data.corr(), vmin=-1, vmax=1, interpolation='none')
fig.colorbar(cax)
fig.set_size_inches(10,10)
pyplot.show()

# separating data and Labels
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

lr = LogisticRegression()
lr.fit(X_train,Y_train)
y_pred1=lr.predict(X_test)

accuracy_score(Y_test,y_pred1)

rf= RandomForestClassifier()
rf.fit(X_train,Y_train)
Y_pred3=rf.predict(X_test)

accuracy_score(Y_test,Y_pred3)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,Y_train)
Y_pred2=knn.predict(X_test)

accuracy_score(Y_test,Y_pred2)

model = LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)

from sklearn.linear_model import SGDClassifier

sgd=SGDClassifier()

for i in range(len(X_train)):
  sgd.partial_fit(X_train[i:i+1],Y_train[i:i+1],classes=['R','M'])

score=sgd.score(X_test,Y_test)

print("Acc:",score)

model_names = ['LR', 'KNN', 'RF', 'SGD']
accuracy_scores = [accuracy_score(Y_test, y_pred1),  # Replace with your actual predictions
                   accuracy_score(Y_test, Y_pred2),  # Replace with your actual predictions
                   accuracy_score(Y_test, Y_pred3),  # Replace with your actual predictions
                   score]

accuracy_df = pd.DataFrame({'Models': model_names, 'ACC': accuracy_scores})

print(accuracy_df)

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x='Models', y='ACC', data=accuracy_df)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, classification_report

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=101)

test_error_rates = []

for k in range(1, 60):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, Y_train)

    preds = knn_model.predict(X_test)
    test_error_rates.append(1-accuracy_score(Y_test, preds))

plt.plot(range(1, 60), test_error_rates)
plt.xlabel('k values')
plt.ylabel('error')
plt.xlim(0, 10)

knn1=KNeighborsClassifier(n_neighbors=1)
knn1.fit(x,y)

import joblib

joblib.dump(knn1,'rock_mine')

def predict_data():
  file_path=filedialog,askopenfilename(title='select the predection data file')

knn_model=joblib.load('rock_mine')

predicitions=knn_model.predict(X_train)

#@title Default title text
input_data=(0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)

model=LogisticRegression()

model.fit(X_train,Y_train)

#Changing the input_data to a numpy array
input_data_as_numpy_array=np.asarray(input_data)
#Reshape the np array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)

#input_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
input_data = (0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)
#input_data = (0.0164,0.0627,0.0738,0.0608,0.0233,0.1048,0.1338,0.0644,0.1522,0.0780,0.1791,0.2681,0.1788,0.1039,0.1980,0.3234,0.3748,0.2586,0.3680,0.3508,0.5606,0.5231,0.5469,0.6954,0.6352,0.6757,0.8499,0.8025,0.6563,0.8591,0.6655,0.5369,0.3118,0.3763,0.2801,0.0875,0.3319,0.4237,0.1801,0.3743,0.4627,0.1614,0.2494,0.3202,0.2265,0.1146,0.0476,0.0943,0.0824,0.0171,0.0244,0.0258,0.0143,0.0226,0.0187,0.0185,0.0110,0.0094,0.0078,0.0112)

# changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction1 = model.predict(input_data_reshaped)
print(prediction1)

if (prediction1[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a mine')