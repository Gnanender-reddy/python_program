#code for palindrome number
try:
    num=int(input("Enter a number:")) #asking user to provide number
    temp=num                          #num value is assigned to temp
    rev=0                             #assigning zero value to rev
    while(num>0):
        dig=num%10                    #dividing number by 10.
        rev=rev*10+dig
        num=num//10                    #floor division
    if(temp==rev):                      #checking if temp is equal to rev
        print("The number is palindrome!") #printing number is palindrome
    else:                                #if condition doesn't matches then printing that it is not palindrome
        print("Not a palindrome!")
except ValueError:
    print("enter valid data") #asking user to provide valid data
