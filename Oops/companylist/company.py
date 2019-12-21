'''
@Author: P.Gnanender Reddy
@Since : Dec'19
@Keywords: json
Description: In this code we are adding company shares to linked list and In this code we created company class,
In this class we created adding list function so that company shares added to linked list.Execution starts from driver code.
'''
import json

from com.bridgelabz.DataStructures.Utility1 import LinkedList


class Company:
    '''
    In this class two methods are defined,one is constructor for object construcrtion and other one is for adding data
    to linked list
    '''
    lst=LinkedList()
    def __init__(self,file):
        '''
        this definition is for constructor
        '''
        self.file=file
        #self.list=[]
    def adding_list(self):
        '''
        this definition is for adding data to linked list
        '''
        lst=LinkedList()
        with open(self.file) as f:
            data=json.load(f)

        for item in data:
            lst.add_element(item)
        print("Company shares added to linked list and shown below")
        lst.display()
class main(Company):
    '''
    In this class, inheritance is used
    '''
    def __init__(self):
        super().__init__() #accessing super class methods and variables

    company = Company("company.json")
    company.adding_list()


