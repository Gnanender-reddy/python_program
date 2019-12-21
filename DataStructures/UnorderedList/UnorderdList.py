
from com.bridgelabz.DataStructures.Utility1 import LinkedList, Node,Queue,Stack

def unordered_list():
   file = open('/home/admin1/PycharmProjects/FellowShipPrograms/com/bridgelabz/'
             'DataStructures/UnorderedList/Text.txt', "r") # file is created and from that file iam reading the data

   data = file.read()  # read  is inbuilt function to read the data from the file
   array = data.split(" ")  # here iam splitting the data where ever the space is there
   l1 = LinkedList()  # creating the object for linkedList
   try:  # try block is used to handle the exception

       for data in range(len(array)):
           l1.add_element(array[data])  # here the elements are added to the list


       try:
           option = int(input(
               "enter choose below options:\n Enter 1.To display the data\nEnter 2.To size of the list\nEnter 3.To remove data from list\nEnter 4.To rempve last \nEnter 5 to exit"))
           if 1 <= option <= 5:
               if option == 1: # if choice is 1 then interpreter goes to display function and prints the data
                   print("unordered list elements are:")
                   l1.display()  # by using the variable iam calling the display function to print data
               if option == 2: #if option is 2 then interpreter goes to size functon and prints the data
                   l1.size()
               if option == 3: # if option is 3 then interpreter goes to remove function and prints the data
                   a = str(input("enter name to remove:"))
                   l1.remove(a)
                   l1.display()
               if option ==4: # if option is 4 then interpreter goes to pop function and removes the data
                   q= Stack()
                   q.pop()
               if option==5:
                   print("thank you...")
               if option >5:
                   print("enter valid data between 1-5")
                   unordered_list()
           else:
               print("enter valid input between 1-5")
               unordered_list()

       except ValueError:
           print("enter valid data")

       try:
           choice1 = int(input("\nenter 1 to continue or 2 to stop:"))
           if choice1 >= 1 or choice1 <= 2:
               if choice1 == 1:
                   unordered_list()
               if choice1 == 2:
                   print("thank you...")
       except ValueError:
           print("enter only numeric values between 1-2")


   except NameError:  # if there have any exception except catch the exception
       print("enter valid data... ")


if __name__ == '__main__':
   unordered_list()


#f = open('/home/admin1/PycharmProjects/FellowShipPrograms/com/bridgelabz/'
            #'DataStructures/UnorderedList/Text.txt', "r")#