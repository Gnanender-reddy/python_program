"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code consists all utilities.

"""




#functions for stack
#creating stack(LIFO manner) class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
#=======================================================================================================================

#creating code for Queue
class Queue:
    def __init__(self):
        self.items = []
    #This  function is for checking for empty
    def isEmpty(self):
        return self.items == []

    #This fucntion is for adding value
    def enqueue(self, item):
        self.items.insert(0,item)
    #This function is for removing value
    def dequeue(self):
        return self.items.pop()
    #This function is for determining size
    def size(self):
        return len(self.items)
#=======================================================================================================================
# FOR UNORDERED AND ORDERED*******************************************************************************
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList: #creating the class to write all functions which are releated to the linked list
    def __init__(self): # constructor of linked list
        self.head = None # initially head is initialized with default value

    # It adds the node with given data at the end of the list
    def add_element(self, data): # this function is used to add the elements any whrere
        new_node = Node(data)# creating the node object
        if self.head is None: # when head is empty then new node added to head
            self.head = new_node
        else: # when node is not empty lopp will search until the empty nodes comes
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            return

    def display(self): # this function is used to diaplay the data
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found

            current = current.next

        return False  # Data Not found

    # It inserts data with given node at particular location
    # def insert(self, position, data):
    #     new_node = Node(data)
    #     new_node.next = position.next
    #     position.next = new_node

    # Delete node with given data
    def remove(self, key):  # this functionis used to remove the data in all places using data
        cur_node = self.head
        previous = None
        # Traverse through the list
        while cur_node.data != key:
            previous = cur_node
            cur_node = cur_node.next
        print(f"Removing {key} from Linkedlist.")
        if previous == None:
            self.head = cur_node.next
        else:
            previous.next = cur_node.next

        # Count number nodes in linked list
    def size(self): # this function is used to find the size of the list
        x = 0
        temp = self.head
        while temp:
            x = x + 1
            temp = temp.next
        print("size of the list is",x)
        return x
#=======================================================================================================================
#code for deque
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#=================================================================================================================#
# Code : Binaryv search tree

# A function to find factorial of a given number
def factorial(n):
    res = 1

    # Calculate value of [1*(2)*---*
    # (n-k+1)] / [k*(k-1)*---*1]
    for i in range(1, n + 1):
        res *= i
    return res


def binomialCoeff(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k

    # Calculate value of [n*(n-1)*---*(n-k+1)] /
    # [k*(k-1)*---*1]
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

    # A Binomial coefficient based function to
    # find nth catalan number in O(n) time


def catalan(n):
    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)

    # return 2nCn/(n+1)
    return c // (n + 1)

    # A function to count number of BST
    # with n nodes using catalan


def countBST(n):
    # find nth catalan number
    count = catalan(n)

    # return nth catalan number
    return count

    # A function to count number of binary
    # trees with n nodes


def countBT(n):
    # find count of BST with n numbers
    count = catalan(n)

    # return count * n!
    return count * factorial(n)
#======================================================================================================================










