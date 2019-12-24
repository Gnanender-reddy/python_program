"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for QuickSort.

"""

from com.bridgelabz.AlgorithmPrograms.util import quick_sort

try:
    sequence = []      # taking empty list here
    size = int(input("Enter size of list: \t"))  #asking user to provide size of the list
    for n in range(size):
        numbers = int(input("Enter any number: \t"))
        sequence.append(numbers)
    print(quick_sort(sequence))
except ValueError:
    print("Please provide valid data")

