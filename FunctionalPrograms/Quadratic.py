#code for Quadratic.
from com.bridgelabz.FunctionalPrograms.Utility import quadratic

try:
    a=int(input("enter first value")) #user input
    b=int(input("enter second value"))
    c=int(input("enter third value"))
    quadratic(a,b,c) #calling quadratic function
except ValueError:
    print("Enter valid data") #asking user to provide valid data