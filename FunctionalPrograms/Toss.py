"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for finding count for heads and tails.
"""



from com.bridgelabz.FunctionalPrograms.Utility import tossCoin
try:
    n=int(input("enter the number of times to flip")) #user input
    tossCoin(n) #tosscoin function is called here
except ValueError:
    print("enter valid data") #asking user to provide valid data