# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:03:39 2017

@author: Omerta
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 16:45:24 2017

@author: Omerta
"""

import random
import sys
import os   #        We're not using most of these packages.
import math
import numpy as np     # Use every time
import matplotlib.pyplot as plt    # plot package
import IPython       # Interactive python- lets us view variable values like R studio
import scipy, pylab # scientific python
import matplotlib    # already have this. oops
import sympy   # symbolic python. Sage written using this. 

xs=[0,3,5,8,13]
fx=[0,225,383,623,993]
fpx=[75,77,80,74,72]

n=len(xs)-1    # defining n to match the n in pseudo code. 

two=2*len(xs)
z=np.zeros(2*len(xs))  
Q=np.zeros((two,two))

for i in range(0,(len(xs))):
    z[2*i]=xs[i]
    z[2*i+1]=xs[i]
    Q[2*i,0]=fx[i]
    Q[2*i+1,0]=fx[i]
    Q[2*i+1,1]=fpx[i]
    if (i != 0): 
        Q[2*i,1]=(Q[2*i,0]-Q[2*i-1,0])/(z[2*i]-z[2*i-1])
         
for j in range(2, 2*(len(xs)-1)+2):
    for k in range(2,j+1): 
        Q[j,k]=(Q[j,k-1]-Q[j-1,k-1])/(z[j]-z[j-k]) # these two loops make hermite coefficients 

b=np.zeros(2*len(xs))

for i in range(0,2*len(xs)):
    b[i]=Q[i,i]
 
    

from sympy import *
x=Symbol('x')

term=[None]*(len(xs)) # making null vectors to store expressions in i think.
term2=[None]*(len(xs))
ell=[None]*(2*len(xs))

for i in (range(0,len(xs))): #
    term[i]=(x-xs[i])

for i in range(0,len(term)):
    term2[i]=term[i]*term[i]
    
print(term2, "is t2")


j=expand(x**2-1)


for i in range(0, len(ell)): #this loop makes the (x-x0)^2(x-x1)^2(x-x2)... terms
    if i==0:
        ell[i]=term[i]
    elif (i>0) and (i+1)%2==0:    # is i odd checker. 1 3 5 7 ...
        var= int((i+1)*(.5))
        ell[i]=prod(term2[0:var])
        #print("i is ",i)
    elif (i>0) and (i<(len(ell)+1)):          # i's = 2,4,6,8, ... 
        #print("IIIIIIIII",i)
       # print("fffff", int((i+1)/2))
        var2=int((i+1)/2) 
        ell[i]=ell[i-1]*term[var2]
  
Hermite=[None]*(2*len(xs)) 



for i in range(0,2*len(xs)):
    if(i==0):
        Hermite[i]=b[i]
    else:
        Hermite[i]=b[i]*(ell[i-1]) 
        
        
        # lambdify is the one function that I have read the documentation on fully.
        # I believe it it used to evualate a number in a symbolic expression. 
H=lambdify(((x,),),sum(Hermite)) # This is actual Hermite Poly, e.g. type H(1.2) 
 

HP=lambdify(((x,),),diff(H(x),x,1))
'''                                   #   to approximate f(1.2)  
def HP(x):
   return diff(H(x),x,1)

'''
HPP=lambdify(((x,),),diff(HP(x),x,1))

sol1=solve(HP(x)-(242/3),x) 

sol2=solve(HPP(x),x)
#def HPP(x): 
  # return diff(H(x),x,2)

#K=lambdify(((x,),),HP(x))   Trying to turn symbolic derivative into regular function 
# for lambify function look at
        #f = lambdify(((x, y, z),), lagrange_eqs(a))
print("coefs of herm are ", b) 
print("   " ) 
print("Hermite poly is ", H(x))

print(" ")
print('H(10) is ', H(10),  "TEN SECONDS")
print(" " ) 
print("hp", HP(2))
print("hpp" ,HPP(2))

print("sol1; is", sol1)
print("sol2 is " , sol2)

for i in range(0,len(sol2)-2):
    print("The speed at time ", sol2[i], "is ", HP(sol2[i])) 
    
