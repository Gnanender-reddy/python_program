"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is about Temperature Conversion.

"""


from com.bridgelabz.FunctionalPrograms.Utility import TemperatureConversion
try:
    n=int(input("enter celsius value")) #user input
    TemperatureConversion(n) #calling temperature conversion function here
except ValueError:
    print("enter valid data") #asking user to provide valid data
    n = int(input("enter celsius value"))
    TemperatureConversion(n) #calling temperature function here



