# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:16:58 2022
9783
@author: Thomas
"""
#Import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Import from SKLearn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Define predictor function (CHANGE!!)
def gasPredictor(array):
    #Change the predictor machine when necessary
    prediction=nb_clf.predict(np.array([array]))
    prediction=le.inverse_transform(prediction)
    return(prediction)


#Import csvs, add more if needed
dataAir=pd.read_csv('220304_Data.csv')

#Split into input and output
inputData=dataAir.iloc[:,:-1].values
outputData=dataAir.iloc[:,-1].values

#Encode the output label
le=LabelEncoder()
outputData=le.fit_transform(outputData)

#Split Data
X_train, X_test, Y_train, Y_test = train_test_split(inputData, outputData, test_size = 0.2, random_state = 42)

#Feature Scaling
#Not sure if I need to do this actually, but I will try first without
#Use Standardscaler

#Traning models
#I will first try using a Naive Bayes classifer (It's kinda trash)
nb_clf = GaussianNB()
nb_clf.fit(X_train, Y_train)
scores = cross_val_score(nb_clf, X_train, Y_train, scoring='accuracy', cv=5)
print(scores)
print('Averaged prediction accuracy = ', np.average(scores))
pred=gasPredictor([13,69,106,53,8])
print(pred)
