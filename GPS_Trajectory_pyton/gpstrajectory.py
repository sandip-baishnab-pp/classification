# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 23:55:01 2016

@author: Sandip Baishnab
"""

#importing modules
import os
import matplotlib
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
matplotlib.style.use("ggplot")

#reading data
go_track_tracks=pd.read_csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")
go_track_trackspoints=pd.read_csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_trackspoints.csv")

print go_track_tracks.head(5)
