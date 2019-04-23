import random
import sys
import os   #        We're not using most of these packages.
import math
import numpy as np     # Use every time
import matplotlib.pyplot as plt    # plot package
import IPython       # Interactive python- lets us view variable values like R studio
import scipy as sci  # scientific python
import pylab    # already have this. oops
import sympy as sym  # symbolic python.
print("go") 
print("  ") 



n = 15                 ################ ENTER  N  HERE   

from sympy import *
x = Symbol('x') 

#g=lambdify(x, (x**3)*sin(9*x))  ###################################   ENTER FUNCTION IN SECOND PLACE 

g=lambdify(x, (x)*cos(x))    #################### THIS IS E^X; JUST COMMENT OUT FUNCTION ABOVE 

#g=lambdify(x, x**2)


#g=lambdify(x, 1/(x+3.15) )

# g = lambdify(x, 4*x**5+3 )

a = [None]*(n)
b = [None]*(n) 




print(" g(2.123) is ", g(2.123) )
print('')



from scipy import integrate
h = (  integrate.quad(lambda x : (1/math.pi)*g(x), -math.pi, math.pi) ) 

print( h )

h = h[0]
print(h)



a_knot = h



print(" ")
print("aknot is ", a_knot)
print(" ")


for i in range(1,n+1):
 d = (  integrate.quad(lambda x : (1/math.pi)*g(x)*np.cos(i*x), -math.pi, math.pi) )
 d = d[0]
 a[i-1]=d

print("a is  " , a ) 

for i in range(1,n+1):
	w = (  integrate.quad(lambda x : (1/math.pi)*g(x)*np.sin(i*x), -math.pi, math.pi) )
	w = w[0]
	b[i-1]=w

print(" ") #####################################################################
print("b is " ,  b) 
print(" ")

cterms=[None]*n
sterms=[None]*n 

for i in range(0,n):
	cterms[i] = cos((i+1)*x)

for i in range(0,n):
	sterms[i] = sin((i+1)*x)




F = lambdify(x, a_knot/2 + np.dot(a,cterms) + np.dot(b,sterms)) 


print( 'f'  , 'haha', F(23), g(23))



print(" ") #####################################################################
print("cterms is ",   cterms)
print(" ")
print("sterms is ", sterms) 
print(" ") #####################################################################


# summ = (a[0]/2) + np.dot())

ccc=np.linspace(-100, 100, 500000)

plt.plot(ccc,F(ccc), color='tab:orange', label="Fourier Approx")
plt.plot(ccc, g(ccc) , '--', color='tab:blue', label="f(x)= cos^2 ")
pylab.legend(loc='upper center')


plt.axis([-9, 9, -13,13])  ###	 CHANGE COORDINATES  [ XMIN, XMAX, YMIN, YMAX ]  #####



# plt.scatter(xs,ys, color= 'tab:green')

pylab.show()


print(" ")

print("stop") 


