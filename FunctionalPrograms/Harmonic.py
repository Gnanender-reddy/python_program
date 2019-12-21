from com.bridgelabz.FunctionalPrograms.Utility import harmonic

try:
    n=int(input("enter the n value")) #input from user
    harmonic(n) #calling harmonic function here
except ValueError:
    print("enter valid data") #asking user to provide valid data
