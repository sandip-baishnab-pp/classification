#ensemble learning majority voting

#required library
library(rpart)
library(caret)

library(e1071)
library(randomForest)

#ensemble learning majority voting function
majority_voting <- function(data)
{
   #class to be returned
   class=c()
   for( i in 1:nrow(data))
   {
       count_zero <-0
       count_one <-0
       count_two <-0
       count_three <-0
       
       for(j in 1:ncol(data))
       {
               if(data[i,j] == 0)
               {
                  count_zero <- count_zero + 1
               }
               else if(data[i,j]==1)
               {
                  count_one <- count_one + 1
               }
               else if(data[i,j]==2)
               {
                  count_two <- count_two + 1
               }
               else if(data[i,j]==3)
               {
                  count_three <- count_three +1
               }
       }
       
       help <- c("count_zero", "count_one", "count_two","count_three")[which.max(c(count_zero, count_one, count_two,count_three))]

       if(help=="count_zero")
         class=c(class,0)
       else if(help=="count_one")
         class=c(class,1)
       else if(help=="count_two")
         class=c(class,2)
       else if(help=="count_three")
         class=c(class,3)
    }
   return(class)
}
  
#variables to be analyzed
variables <- c("speed","time","distance","rating","rating_weather","car_or_bus","rating_bus")

#reading data
data <- read.csv("C:/Sandip_Dj/Sandip/Git/program/data/GPS_Trajectory_classification/go_track_tracks.csv")

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
nb <-naiveBayes(train_x,train$rating_bus)
nb_predict <-predict(nb,test_x)

#random forest
rf <-randomForest(train_x,train$rating_bus)
rf_predict <-predict(rf,test_x)

#ensemble learning
sv_predict <-as.vector(sv_predict)
nb_predict <-as.vector(nb_predict)
rf_predict <-as.vector(rf_predict)

#prediction dataframe
s_n_r <-data.frame(sv_predict,nb_predict,rf_predict)
colnames(s_n_r) <-c("svm","naivebayes","randomforest")

#calling majority voting
result <- cbind(s_n_r,vote=majority_voting(s_n_r),original=test_y)
print (result)

#confusion matrix
#cm <-table(pred=as.factor(unlist(result["vote"])),true=as.factor(unlist(test_y)))
cm <-confusionMatrix(result["vote"],test_y)