from com.bridgelabz.AlgorithmPrograms.util import selectionsort

try:
    num = []                                  #declaring list
    n = int(input("Enter the list size : "))   #taking list from user
    for i in range(0, n):                      #taking values in range between o and n
        print("Enter number at location", i, ":")
        item = int(input())#user input
        num.append(item) #append function adds values
    selectionsort(num) # selection sort function is called here
except ValueError:
    print("enter valid data") #asking user to provide valid data