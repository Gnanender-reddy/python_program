from com.bridgelabz.AlgorithmPrograms.util import binarysearch
try:
    lst = []                                                            #declaring empty list
    size = int(input("Enter size of list:"))                         #Asking user to provide size
    for n in range(size):                                               #for iteration
        numbers = int(input("Enter any number: \t"))                    #input from user
        lst.append(numbers)                                             #adding numbers to list
    lst.sort()                                                          #sort function is called here for sorting
    print('\n\nThe list will be sorted, the sorted list is:', lst)      #Printing list
    x = int(input("\nEnter the number to search: "))
    binarysearch(lst, size, x)                                           #calling function here

except ValueError:
    print("enter valid data")
