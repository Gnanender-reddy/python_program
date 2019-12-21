from com.bridgelabz.FunctionalPrograms.Utility import tossCoin
try:
    n=int(input("enter the number of times to flip")) #user input
    tossCoin(n) #tosscoin function is called here
except ValueError:
    print("enter valid data") #asking user to provide valid data