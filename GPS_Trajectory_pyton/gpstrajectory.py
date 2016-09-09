# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:36:26 2016

@author: Sandip Baishnab
"""
#importing modules
import random
import pandas as pd

from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

from ensemble_learning import mv

#features and class to be analysed
variables=["speed","time","distance","rating","rating_weather","car_or_bus","rating_bus"]

#reading data
data_gps_trajectory=pd.read_csv("C:/Sandip_Dj/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")

#selecting features from data and slicing
data=data_gps_trajectory[variables]
rows=random.sample(data.index,150)
work_train=data.ix[rows]
train_x=work_train.drop("rating_bus",axis=1)
train_y=work_train["rating_bus"]
work_test=data.drop(rows)
test_x=work_test.drop("rating_bus",axis=1)
test_y=work_test["rating_bus"]

#object for classifiers SVM, Naive Bayes, Stochastic Gradient Descent
clf_svm=svm.SVC()
clf_svm.fit(train_x,train_y)
predict_svm=clf_svm.predict(test_x)

clf_bnb = BernoulliNB()
clf_bnb.fit(train_x,train_y)
predict_bnb=clf_bnb.predict(test_x)

clf_SGD =SGDClassifier()
clf_SGD.fit(train_x,train_y)
predict_SGD=clf_SGD.predict(test_x)

#dataframe for combining results
voting=mv()
ensemble=pd.DataFrame({"svm":predict_svm,"bnb":predict_bnb,"SGD":predict_SGD})
ensemble["voting"]=voting.majority_voting(ensemble)
ensemble["original"]=list(test_y)
print ensemble

#accuracy svm bayes random forest
score_svm=accuracy_score(list(test_y), predict_svm)*100
print "score_svm:%f " %score_svm
score_bayes=accuracy_score(list(test_y), predict_bnb)*100
print "score_binomial naivebayes:%f " %score_bayes
score_SGD=accuracy_score(list(test_y), predict_SGD)*100
print "score_SGD:%f " %score_SGD
score_ensemble = accuracy_score(list(test_y), list(ensemble["voting"]))*100
print "score_ensemble:%f " %score_ensemble