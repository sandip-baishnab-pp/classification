# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 01:33:28 2016

@author: Sandip Baishnab
"""

#importing module
import pandas as pd

class mv():
    
    def majority_voting(self,data):
        
        row=len(data.axes[0])
        col=len(data.axes[1])
        new_class=[]
        
        for i in range(0,row):
            
               count_zero=0
               count_one=0
               count_two=0
               count_three=0
               
               for j in range(0,col):
                   
                    if   (data.ix[i,j] == 0):
                             count_zero = count_zero + 1
              
                    elif (data.ix[i,j]==1):
                             count_one = count_one + 1
               
                    elif (data.ix[i,j]==2):
                             count_two = count_two + 1
               
                    elif (data.ix[i,j]==3):
                             count_three = count_three +1
                             
               bigger={"count_zero":count_zero, "count_one":count_one, "count_two":count_two,"count_three":count_three}
               help_max=max(bigger.iterkeys(), key=lambda k: bigger[k])
                            
               if (help_max == "count_zero"):
                   new_class.append(0)
               elif (help_max == "count_one"):
                   new_class.append(1)
               elif (help_max == "count_two"):
                   new_class.append(2)
               elif (help_max == "count_three"):
                   new_class.append(3)
                   
        return new_class
                