#required library
library(e1071)
library(randomForest)

#variables to be analyzed
variables <- c("speed","time","distance","rating","rating_weather","car_or_bus","rating_bus")

#reading data
data <- read.csv("C:/Sandip_Debjani/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")

#data slicing
slice_data <- data[variables]
train <- slice_data[c(1:150),]
train_x <-subset(train,select = -rating_bus)
train_y <-train["rating_bus"]
test <- slice_data[c(151:nrow(slice_data)),]
test_x <- subset(test,select = -rating_bus)
test_y <- test["rating_bus"]

#model svm
sv=svm(x=train_x,y=train_y,type="C-classification")
sv_predict=predict(sv,test_x)

#naive bayes
train$rating_bus<-as.factor(train$rating_bus)
nb=naiveBayes(train_x,train$rating_bus)
nb_predict=predict(nb,test_x)

#random forest

rf=randomForest(train_x,train$rating_bus)
rf_predict=predict(rf,test_x)

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

