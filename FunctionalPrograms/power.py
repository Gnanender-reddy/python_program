"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for finding power of number.

"""


from com.bridgelabz.FunctionalPrograms.Utility import pow

try:
    a=int(input("enter a value")) #input from user
    b=int(input("enter b value"))
    pow(a,b) #power function is called here
except ValueError:
    print("please provide valid data") #asking user to provide valid data
