# -*- coding: utf-8 -*-
"""Rock or Mine Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BXhfICcjG1H9mDetEfgaD_VEH6bv6pSq

Importing The Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score

"""Data Collection and Data Processing"""

sonar_data =pd.read_csv('/content/sonar data.csv',header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe() #Describe gives statistical measure of data

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#separating data and labels
a = sonar_data.drop(columns=60,axis=1)
b= sonar_data[60]

print(a)
print(b)

"""Testing and Training data

"""

a_train,a_test,b_train,b_test = train_test_split(a,b,test_size= 0.1,stratify=b,random_state=1)

print(a.shape,a_train.shape,a_test.shape)

print(a_train)
print(b_train)

"""Model Training"""

model = LogisticRegressionCV(max_iter=1000)

model.fit(a_train,b_train)

"""Model Evaluation"""

#accuracy on training
a_train_prediction = model.predict(a_train)
training_data_accuracy = accuracy_score(a_train_prediction,b_train)

print('Accuracy on training data:',training_data_accuracy)

a_test_prediction = model.predict(a_test)
test_data_accuracy = accuracy_score(a_test_prediction,b_test)

print('Accuracy on test data:',test_data_accuracy)

"""Making a Predictive System

"""

input_data = (0.0323,0.0101,0.0298,0.0564,0.0760,0.0958,0.0990,0.1018,0.1030,0.2154,0.3085,0.3425,0.2990,0.1402,0.1235,0.1534,0.1901,0.2429,0.2120,0.2395,0.3272,0.5949,0.8302,0.9045,0.9888,0.9912,0.9448,1.0000,0.9092,0.7412,0.7691,0.7117,0.5304,0.2131,0.0928,0.1297,0.1159,0.1226,0.1768,0.0345,0.1562,0.0824,0.1149,0.1694,0.0954,0.0080,0.0790,0.1255,0.0647,0.0179,0.0051,0.0061,0.0093,0.0135,0.0063,0.0063,0.0034,0.0032,0.0062,0.0067)

 #changing input_data to numpy array
 input_data_as_numpy_array = np.array(input_data)

#reshaping the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

print(prediction)
if(prediction[0]=='R'):
  print('The Object Is Rock')
else:
  print('The Object Is a Mine')