# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:36:26 2016

@author: Sandip Baishnab
"""
#importing modules
import random
import pandas as pd

#features and class to be analysed
variables=["speed","time","distance","rating","rating_weather","car_or_bus","rating_bus"]

#reading data
data_gps_trajectory=pd.read_csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")

#selecting features from data and slicing
data=data_gps_trajectory[variables]
rows=random.sample(data.index,150)
train=data.ix[rows]
test=data.drop(rows)

#writing file into
train.to_csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/train.csv",index=0)
test.to_csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/test.csv",index=0)



