"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for all utilities.

"""



#code for Anagram

def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("then {0} and {1} are anagrams".format(s1,s2))
    else:
        print("both are not anagrams")

#=======================================================================================================================
#code for Bubble Sort
def bubblesort(nums):                 #defining bubblesort function
    for i in range(len(nums)-1,0,-1): #for iteration process
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return  nums
#=======================================================================================================================
def selectionsort(num):
    # This value of i corresponds to how many values were sorted
    for i in range(len(num)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(num)):
            if num[j] < num[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        num[i], num[lowest_value_index] = num[lowest_value_index], num[i]
    print(num)

#=======================================================================================================================
def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)



#=======================================================================================================================
def countCurrency(amount):
    notes = [2000, 500,200,100,50,20,10,5,2,1]    #these are notes
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #list of notes counter
    print("Currency Count ->")
    for i,j in zip(notes, noteCounter):
        if amount >=1:
            j = amount // i
            amount = amount -j * i
            print(i, ":", j)                     #printing number of notes with respect to amount
#=======================================================================================================================
#code for finding prime numbers
def prime(n,n1):
    # Python program to print all
    # prime number in an interval

    start = n
    end = n1

    for val in range(start, end + 1):

    # If num is divisible by any number
    # between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                print(val)
#=======================================================================================================================
#code for binary search
def binarysearch(lst, length, key):
    start = 0                                   #starting value of list
    end = length - 1                            #ending  value of list
    while start <= end:
        mid = int((start + end) / 2)
        if key == lst[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < lst[mid]:
            end = mid - 1
        elif key > lst[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1

#=======================================================================================================================

def palindrome(my_str):
   my_str = my_str.casefold()                                           # make it suitable for caseless comparison
   rev_str = reversed(my_str)                          # reverse the string
   if list(my_str) == list(rev_str):
      print("The string is a palindrome.")
   else:
      print("The string is not a palindrome.")

#=======================================================================================================================
#code for monthly payment
def monthlypayment():
            try:

                p = float(input('Enter principle loan amount'))
                y = int(input('Enter the years'))
                R = float(input('Percentage of interest'))
                n = 12 * y
                r = R / (12 * 100)
                payment = p * r / (1 - (1 + r) ** (-n))
                print(payment)
            except ValueError:
                print("enter valid data")
                monthlypayment()
