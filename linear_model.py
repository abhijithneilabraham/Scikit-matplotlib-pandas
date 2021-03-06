#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:05:10 2019

@author: abhijithneilabraham
"""

import matplotlib.pyplot as plt
x=[[2],[2.5],[1],[5],[8]]
y=[[45],[58],[20],[65],[90]]
plt.figure() #creates a new figure
plt.title('marks obtained plotted against number of study hours')
plt.xlabel('study hours')
plt.ylabel('marks in 100')
plt.plot(x,y,'bo')
plt.axis([0,10,0,100]) #the maximum value in x axis and y axis
plt.grid(True)
plt.show()
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
b=model.predict([[4]])
c=b[0][0]
d='{:.3f}'.format(c)
print("a student who studied 4 hours will get",d)
