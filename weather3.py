

import random
import sys
import os   #        
import math
import numpy as np     # Use every time
import matplotlib.pyplot as plt    # plot package
import IPython       # Interactive python-
import scipy, pylab # scientific python
import matplotlib    
import sympy   # symbolic 
import pandas as pd


print("go")
print("  ")

weather = r'weather.txt'

df = pd.read_csv(weather)
df = pd.DataFrame(df)

print('ijij', len(df.Time))

m = np.array(pd.read_csv(weather))
y = m[:,1]
y = np.array(y)
x = m[:,0]

D = np.zeros((len(x),4))
a = np.zeros(4)



for j in range(0,4):
    for i in range(0,len(x)):
        if(j==0):
         D[i,j]=1
        elif(j==1):
         D[i,j]= x[i]
        elif(j==2):
         D[i,j]= np.sin(2*np.pi*x[i])
        else:
         D[i,j]= np.cos(2*np.pi*x[i])
                
print()

a = np.linalg.solve(np.matmul(np.transpose(D),D), np.matmul(np.transpose(D),y)) 


D2 = np.zeros((len(x),6))
a2 = np.zeros(6)



for j in range(0,6):
    for i in range(0,len(x)):
        if(j==0):
         D2[i,j]=1
        elif(j==1):
         D2[i,j]= x[i]
        elif(j==2):
         D2[i,j]= np.sin(2*np.pi*x[i])
        elif(j==3):
         D2[i,j]= np.cos(2*np.pi*x[i])
        elif(j==4):
         D2[i,j] = np.sin(np.pi*x[i])
        else:
         D2[i,j] = np.cos(np.pi*x[i])
         
a2 = np.linalg.solve(np.matmul(np.transpose(D2),D2), np.matmul(np.transpose(D2),y)) 

xxx = np.arange(-1, 4, .0001)

def f(x):
    return a[0]+a[1]*x + a[2]*np.sin(2*np.pi*x) + a[3]*np.cos(2*np.pi*x) 

def f2(x):
    return a2[0]+a2[1]*x + a2[2]*np.sin(2*np.pi*x) + a2[3]*np.cos(2*np.pi*x)+a2[4]*np.sin(np.pi*x)+a2[5]*np.cos(np.pi*x)

A = np.matmul(np.transpose(D),D)

plt.scatter(x, y, color = 'brown', label='Original Data')
plt.plot(xxx, f2(xxx), color='orange', label='Six Term F(x)')
plt.plot(xxx,f(xxx), label='Four Term F(x)')
pylab.legend(loc='upper right')

plt.show()


print(D2)











