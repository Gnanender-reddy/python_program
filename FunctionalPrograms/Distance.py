from com.bridgelabz.FunctionalPrograms.Utility import calculateDistance
try:
    x1=int(input("enter value"))   #input from user
    x2=int(input("enter second value"))
    y1=int(input("enter third value"))
    y2=int(input("enter the fourth value"))
    calculateDistance(x1,y1,x2,y2) #calling distance function
except ValueError:
    print("enter valid data") #asking user to provide valid data

