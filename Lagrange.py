
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
print("go") 
print("  ") 



##################################################### 8.1 1 ##################

xs = [- .92388 ,  -.382683 , .382683 ,    .92388 ]

ys = np.exp(xs)

lnum = [None]*len(xs)
ldem = [None]*len(xs)

terms = [None]*len(xs)

from sympy import *
x = Symbol('x')

lzero= lambdify(x, ((x-xs[1])*(x-xs[2])*(x-xs[3]))/((xs[0]-xs[1])*(xs[0]-xs[2])*(xs[0]-xs[3])))
lone= lambdify(x, ((x-xs[0])*(x-xs[2])*(x-xs[3]))/((xs[1]-xs[0])*(xs[1]-xs[2])*(xs[1]-xs[3])))
ltwo= lambdify(x, ((x-xs[0])*(x-xs[1])*(x-xs[3]))/((xs[2]-xs[0])*(xs[2]-xs[1])*(xs[2]-xs[3])))
lthree= lambdify(x, ((x-xs[0])*(x-xs[1])*(x-xs[2]))/((xs[3]-xs[0])*(xs[3]-xs[1])*(xs[3]-xs[2])))

print(terms)

print(" ")

print(lzero(5), "ppppp")
print(lone(5), "eeeeee")
print(ltwo(5), "qqq")
print(lthree(5), "zzzz")

P = lambdify(x, ys[0]*lzero(x) + ys[1]*lone(x) + ys[2]*ltwo(x) + ys[3]*lthree(x))

Err = lambdify(x, np.abs(P(x)-exp(x)))

print("e", P(x))

ccc=np.linspace(-1.2,1.2,1000)

plt.plot(ccc, Err(ccc), color='tab:orange')
#plt.scatter(xs,ys, color= 'tab:green')
plt.xlabel('x')
plt.ylabel('Absolute Error of Approx')
pylab.show()


