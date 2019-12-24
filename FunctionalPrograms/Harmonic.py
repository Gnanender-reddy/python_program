"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for finding harmonic value.

"""


from com.bridgelabz.FunctionalPrograms.Utility import harmonic

try:
    n=int(input("enter the n value")) #input from user
    harmonic(n) #calling harmonic function here
except ValueError:
    print("enter valid data") #asking user to provide valid data
