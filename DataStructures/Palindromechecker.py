from com.bridgelabz.DataStructures.Utility1 import Deque


def palindromeChecker(strin):
        d=Deque()
        for ch in strin:
            d.addRear(ch)
        if d.removeFront()==d.removeRear():
            print("given string is palin")
        else:
            print("Given string is not palindrome")
if __name__ == '__main__':
    strin=input("enter one string")
    print(strin)
    palindromeChecker(strin)


#string