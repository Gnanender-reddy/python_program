"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code consists all utilities.

"""


#code for to find factorial
def factorial(n): #defining factorial function here
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i


    print("The factorial of {} is : {} ".format(n,fact))  #format() adds values of n and fact to print
    print(fact)
    return fact

#=======================================================================================================================

#code for toss coin.
import random   #importing random library

def tossCoin(n): #defining toss coin function
    heads = 0
    tails = 0
    for i in range(n):
        coin = random.randint(0,1) #it gives random values between 0 and 1
        if coin < .5:
            heads =heads+1
        else:
            tails =tails+ 1

    print("number of heads is {}".format(heads))
    print ("number of tails is {}".format(tails))

#=======================================================================================================================
#code for to find Distance
import math
def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     print(dist)
#=======================================================================================================================
import cmath

def quadratic(a,b,c):


    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print(sol1,sol2)
    return sol1 and sol2
#=======================================================================================================================

#code to find power of number:
def pow(a,b):    #defining power function
     c=a**b
     print(c)    #printing c value


#=======================================================================================================================
#code for harmonic
def harmonic(n): #defining harmonic function
    c=1          #initialising first value
    for i in range(2,n):
        c+=1/i      #Formula for harmonic

    print(c)
    return c

#=======================================================================================================================
#code for stop watch
import time #importing time
def stopwatch():
    print("the timer has started")
    begin = time.time(); #time is function
    endtimer = input("press . and click enter to stop the timer ")
    end = time.time()
    elapsed = end - begin
    elapsed = int(elapsed)
    print("the time elapsed is", elapsed, "seconds")

#=======================================================================================================================
#Code for Temperature Conversion
def TemperatureConversion(n): #defining function for temperature conversion

        celsius=n
        fahrenheit = (celsius * 1.8) + 32
        print("for {0} degrees celsius value it produce {1} degrees fahrenheit".format(celsius,fahrenheit))





#=======================================================================================================================






