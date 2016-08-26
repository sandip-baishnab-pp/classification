#required library
library(e1071)

#variables to be analyzed
variables->c("speed","time","distance","rating","rating_weather","car_or_bus","rating_bus")

#reading data
data->read.csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")

#data slicing
slice_data->data[variables]
train->slice_data[c(1:150),]
test->slice_data[c(151:nrow(slice_data)),]
test->subset(test,select=-c("rating_bus"))




# data_work=subset(data,select=-c(id,linha))
# 
# #slicing
# data_row=nrow(data)
# train=data_work[84:155,]
# train_label=data[84:155,"linha"]
# test=data_work[156:163,]
# test_label=data_work[156:163,"linha"]
# 
# #model building
# model=svm(train_label,data=train,cost=100,gamma=1)
# pred=predict(model,test)
# cm=table(pred=pred,true=test_label)

