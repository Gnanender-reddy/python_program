"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for Balanced Paranthesis.
"""
from com.bridgelabz.DataStructures.Utility1 import Stack


def parChecker(symbolString):
    #creating object for stack
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        #if symbol is equal to providing condition then value is pushed
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                #Here value is removed
                s.pop()
        #Incrementing index by 1
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
