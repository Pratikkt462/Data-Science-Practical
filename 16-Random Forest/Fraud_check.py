# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:23:56 2024

@author: Lenovo
"""

import pandas as pd
#importing dataset
fraud=pd.read_csv('c:/2-datasets/Fraud_check.csv')
fraud.head()
#Spliting dataset into training and testing

x=fraud.drop('Urban',axis='columns')
y=fraud['Urban']

#applying one hot encoding
from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder()
x_encoded=pd.get_dummies(x)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_encoded,y,test_size=0.2)

#applying random forest model

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)

#Checking Acuraccy
model.score(x_test,y_test)
y_predicted=model.predict(x_test)

#generating confusion Matrix

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)
cm

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel("Predicted")
plt.ylabel('Truth')
