from com.bridgelabz.AlgorithmPrograms.util import prime

try:
    n=int(input("enter starting value")) #asking user to provide starting parameter value
    n1=int(input("enter end value")) #asking user to provide end value
    prime(n,n1) #calling prime function here
except ValueError:
    print("Enter valid data")#asking user to provide valid data
