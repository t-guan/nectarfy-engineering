# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:16:58 2022
9783
@author: Thomas
"""
#Import libraries
import numpy as np 
import pandas as pd

#Import from SKLearn
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score

#Define predictor function (CHANGE!!)
def gasPredictor(array):
    #Change the predictor machine when necessary
    predictionNT=knn_clf.predict(np.array([array]))
    #predictionNT=nb_clf.predict(np.array([array]))
    prediction=le.inverse_transform(predictionNT)
    totpred=[prediction,predictionNT]
    return(totpred)

def gasModelNaiveBayes():
    nb_clf = GaussianNB()
    nb_clf.fit(X_train, Y_train)
    Y_pred=nb_clf.predict(X_test)
    scores = cross_val_score(nb_clf, X_train, Y_train, scoring='accuracy', cv=10)
    print(scores)
    print('Averaged prediction accuracy for Naive Bayes = ', np.average(scores))
    #Check confusion matrix
    cm=confusion_matrix(Y_test,Y_pred)
    ac=accuracy_score(Y_test,Y_pred)

def gasKNN():
    #Try K Nearest Neighbors
    from sklearn.neighbors import KNeighborsClassifier
    knn_clf = KNeighborsClassifier(n_neighbors=20) # change n_neighbors; boundary becomes smoother with increasing value of K
    knn_clf.fit(X_train, Y_train)
    scores = cross_val_score(knn_clf, X_train, Y_train, scoring='accuracy', cv=5)
    print(scores)
    
#Import csvs, add more if needed
dataAir=pd.read_csv('Data_0329_AirEth.csv')

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
#sc=StandardScaler()
#X_train=sc.fit_transform(X_train)
#X_test=sc.transform(X_test)
#Traning models
#I will first try using a Naive Bayes classifer 

#Okay Naive Bayes kinda sucked I'm going to try using ANN instead
#ANN stored within the function, because it kinda sucked as well.
#Update 03-29 I'm going to try Naive Bayes again but with scaling
from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier(n_neighbors=20) # change n_neighbors; boundary becomes smoother with increasing value of K
knn_clf.fit(X_train, Y_train)
scores = cross_val_score(knn_clf, X_train, Y_train, scoring='accuracy', cv=5)
print(scores)


