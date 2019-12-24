"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for CountCurrency.

"""

from com.bridgelabz.AlgorithmPrograms.util import countCurrency

try:
    amount=int(input("enter amount")) #user input
    countCurrency(amount) #countcurrent function is called
except ValueError:
    print("Enter valid data")#asking user to provide valid data