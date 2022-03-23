# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:16:58 2022
9783
@author: Thomas
"""
#Import libraries
import numpy as np 
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

#Import from SKLearn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Define predictor function (CHANGE!!)
def gasPredictor(array):
    #Change the predictor machine when necessary
    predictionNT=knn_clf.predict(np.array([array]))
    prediction=le.inverse_transform(predictionNT)
    totpred=[prediction,predictionNT]
    return(totpred)
def gasModelANN():
    #Actiavte ANN using Sequential Model
    GasModel=tf.keras.models.Sequential()
    #Input layer, modify activation where required
    GasModel.add(tf.keras.layers.Dense(units=5,input_dim=5,activation='relu'))
    #Hidden Layers
    GasModel.add(tf.keras.layers.Dense(units=9,activation='relu'))
    GasModel.add(tf.keras.layers.Dense(units=7,activation='relu'))
    GasModel.add(tf.keras.layers.Dense(units=9,activation='relu'))
    GasModel.add(tf.keras.layers.Dense(units=7,activation='relu'))
    GasModel.add(tf.keras.layers.Dense(units=9,activation='relu'))
    GasModel.add(tf.keras.layers.Dense(units=7,activation='relu'))
    #Output Layers
    GasModel.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    GasModel.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    GasModel.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    
    #Compile ANN
    GasModel.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    #Run ANN
    history=GasModel.fit(X_train,Y_train,validation_split=0.33,batch_size=32,epochs=100,verbose=1)
    
    #Check error
    Y_pred=GasModel.predict(X_test)
    Error=Y_test-Y_pred
    print('The average ANN error is:',np.average(Error))
def gasModelNaiveBayes():
    nb_clf = GaussianNB()
    nb_clf.fit(X_train, Y_train)
    scores = cross_val_score(nb_clf, X_train, Y_train, scoring='accuracy', cv=5)
    print(scores)
    print('Averaged prediction accuracy for Naieve Bayes = ', np.average(scores))
    

#Import csvs, add more if needed
dataAir=pd.read_csv('220308_DataRH+DLL.csv')

#Split into input and output
inputData=dataAir.iloc[:,:-1].values
outputData=dataAir.iloc[:,-1].values

#Encode the output label
le=LabelEncoder()
outputData=le.fit_transform(outputData)

#Split Data
X_train, X_test, Y_train, Y_test = train_test_split(inputData, outputData, test_size = 0.2, random_state = 42)

#Feature Scaling
#I am attempting feature scaling now
#Use Standardscaler


#Traning models
#I will first try using a Naive Bayes classifer (It's kinda trash)


#Okay Naive Bayes kinda sucked I'm going to try using ANN instead
#ANN stored within the function, because it kinda sucked as well.

#Try K Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier(n_neighbors=10) # change n_neighbors; boundary becomes smoother with increasing value of K
knn_clf.fit(X_train, Y_train)
scores = cross_val_score(knn_clf, X_train, Y_train, scoring='accuracy', cv=5)
print(scores)
