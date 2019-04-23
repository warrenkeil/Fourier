import random
import sys
import os   #        We're not using most of these packages.
import math
import numpy as np     # Use every time
import matplotlib.pyplot as plt    # plot package
import IPython       # Interactive python- lets us view variable values like R studio
import scipy as sci  # scientific python
import pylab 
import matplotlib    # already have this. oops
import sympy as sym  # symbolic python.
print("go") 
print("  ") 

def E(x):
	return .01 + x*0

def f(x):
	return np.exp(x)*x

def P6(x):
	return x + x**2 + (x**3/2) + (x**4/6) + (x**5/24) + (x**6/120) 
	
def P5(x):
	return (x**5/24) + (43*x**4/240) + (x**3/2) + (637*x**2/640) + x + 1/3840
	
def P4(x):
	return (43*x**4/240) + (53*x**3/96) + ( (637*x**2/640) ) + (379*x/384)+(1/3840)
	
def P3(x):
	return (117*x**3/160) + (637*x**2/640) + (379*x/384) - (17/768)
	
ccc=np.linspace(-100, 100, 500000)

plt.plot(ccc,f(ccc)-f(ccc), color='tab:orange', label="x*e^x")
plt.plot(ccc, f(ccc)-P6(ccc) , '--', color='tab:blue', label="P6 ")
plt.plot(ccc, f(ccc)-P5(ccc), '-.', color='tab:brown', label = "P5")
plt.plot(ccc, f(ccc)-P4(ccc), ':', color='tab:green', label = "P4")
plt.plot(ccc, f(ccc)-P3(ccc), '--', color='tab:pink', label = "P3")
plt.plot(ccc, E(ccc), ':', color='tab:red', label="Error limit")
plt.plot(ccc, -E(ccc), ':', color='tab:red', label="Error limit")
pylab.legend(loc='upper center')


plt.axis([-9, 9, -13,13])  ###	 CHANGE COORDINATES  [ XMIN, XMAX, YMIN, YMAX ]  #####



# plt.scatter(xs,ys, color= 'tab:green')

pylab.show()
