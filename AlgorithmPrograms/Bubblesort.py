"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for bubbleSort.

"""


from com.bridgelabz.AlgorithmPrograms.util import bubblesort
try:
    nums = []                                  #declaring list
    n = int(input("Enter the list size : "))    #taking list from user
    for i in range(0, n):                        #taking values in range of 0 to n
        print("Enter number at location", i, ":") #printing number at location
        item = int(input())                       #user input
        nums.append(item)                   # append() function is used for adding values to list
        bubblesort(nums)                #calling selection sort function
except ValueError:
    print("enter valid data")
