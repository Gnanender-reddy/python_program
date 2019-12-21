from com.bridgelabz.FunctionalPrograms.Utility import factorial

try:
    n=int(input("enter the number to find factorial")) #input from user
    factorial(n) #calling factorial function from utility
except ValueError:
    print("enter valid data") #asking user to provide valid data