from com.bridgelabz.DataStructures.Utility1 import LinkedList

def hashfunction():
 try:
    file = open("texttt.txt", 'r')  # here input data is reading ro the file
    # here input data is reading ro the file

    text = file.read()
    list = text.split(" ")  # here data is splittig where ever the space is there
    object = []
    temp = LinkedList()  # here object is created for LinkedLis class to acces their functions
    print("after hashing operation output is")
    for i in range(0, 11):
        object.append(LinkedList())
    for i in range(len(list)):
        position = int(list[i]) % 11  # this statement is used for checking the hash table position
        temp = object[position]
        temp.add_element(list[i])
    for i in range(len(list)):  # this statement iterates the data upto the length of the list
        temp = object[i]

        temp.display()
        print()

    choice1 = int(input("enter 1 to continue or 2 to stop:"))
    if choice1 >= 1 or choice1 <= 2:
        if choice1 == 1:
            hashfunction()
        if choice1 == 2:
            print("thank you...")
 except IndexError:  # here catching the excption to recover
     print("check the index position")

if __name__ == '__main__':
     hashfunction()