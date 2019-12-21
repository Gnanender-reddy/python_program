'''
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:json,encapsulation.
@Description:This code is for Stock Symbol Purchased or Sold in a Stack implemented using Linked List to indicate transactions done.

'''



import json

from com.bridgelabz.DataStructures.Utility1 import LinkedList, Stack


class TransactionStack:
    def __init__(self):
        #constructing the object

        self.stack = Stack()
        with open("stack.json") as data:
            try:
                temp = json.load(data)
            except Exception:
                pass
            else:
                for i in temp:
                    self.stack.push(i)

    def transaction_stack(self):
        '''
        This function helps us to push all transactions to stack
        '''
        try:
            transaction = input("Enter transaction amount")
            while not transaction.isnumeric():
                #Checking transaction is in numeric format or not, if it is not in numeric asking again to enter transaction
                #in numerics.
                transaction = input("Enter ammount in Rupees")

            customer_name = input("Enter name")
            while not customer_name.isalpha():
                customer_name = input("Enter name in Alphabets")

            company_name = input("Enter company name")
            while not company_name.isalpha():
                company_name = input("Enter company name in Alphabets")

            no_of_share = input("Enter no. of shares")
            while not no_of_share.isnumeric():
                no_of_share = input("Enter no. of shares in numbers")

            cost = input("Enter cost")
            while not cost.isnumeric():
                cost = input("Enter cost in Numbers")

            time = input("Enter time")
            #asaking user time function
            new_transaction = {"transaction": transaction, "customer_name": customer_name, "company_name": company_name,
                               "no_of_share": no_of_share, "cost": cost, "time": time}
            self.stack.push(new_transaction)
        except ValueError:
            print("You have entered wrong data:")

    def save_transaction(self):
        '''
        this function works like it dumps data to json file, so it saves transaction.
        '''

        temp1 = []
        #taking empty list
        size = self.stack.size()
        for i in range(size):
            #looping through the data
            temp1.append(self.stack.pop())
            #popping data and adding data to list
        with open("stack.json", 'w') as data:
            #dumping data
            json.dump(temp1, data, indent=2)
            print(temp1)


# Main method
if __name__ == "__main__":
    #driver code
    obj = TransactionStack()
    obj.transaction_stack()
    obj.save_transaction()