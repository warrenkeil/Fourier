#######################
# Warren Keil hw 2.3 newton method. 
####################
#         rm(list=ls())
#6e 
##################

##################################
#  14
##################################       rm(list=ls())
# Use Newton method to find closest point of graph f(x)= 1/x to the point (2,1). 
#
#Newton Algo x in [0,1] and x in [3,5] 

f <- function(x){ exp(x)-3*x^{2} }
fprime <- function(x){ exp(x) - 6*x} 

p0 <- 4.1

tol <- 10^{-5} 
maxn <-1100
i <- 1

while(i<=maxn){
  p <- p0 - f(p0)/fprime(p0)
  if( abs(p-p0)<tol){
    cat("p = ", p, ", iterations = ", i)
    break
  }
  i<-i+1
  p0 <- p
}

# Note: I first made a distance function of x to calculate the distance. 
# I then used the second derivative of this function to find the crit point of 
# the first derivative. My answer also assume that the closest distance lies somewhere between
# (0, infinity) on the x axis. While this is obvious for this problem, mathematically, I did not
# show that answers elsewhere weren't the solution. 


# f <- function(x){ 1/x }
# fprime <- function(x){ -1/(x^{2})}  

dist<- function(x){(x^{2}-4*x+5-2*x^{-1}+x^{-2})^{.5}}
distp <-function(x){(1/2)*((x^{2}-4*x+5-2*x^{-1}+
                                  x^{-2})^{-.5})*(2*x-4+2*x^{-2}-2*x^{-3})}
distpp<-function(x){
(-1/4)*((x^{2}-4*x+5-2*x^{-1}+x^{-2})^{-3/2})*(2*x-4+2*x^{-2}-2*x^{-3})*(2*x-4+x^{-2}-2*x^{-3})+(.5)*((x^{2}-4*x+5-2*x^{-1}+x^{-2})^{-1/2})*(2-4*x^{-3}+6*x^{-4})
  }
p0 <- 1.7

tol <- 10^{-8} 
maxn <-2100
i <- 1

while(i<=maxn){
  p <- p0 - distp(p0)/distpp(p0)
  #browser()
  if( abs(p-p0)<tol){
    cat("p = ", p, ", iterations = ", i, ". Distance to (2,1) is ", dist(p))
    break
    } 
    
    i<-i+1
  p0 <- p
}




