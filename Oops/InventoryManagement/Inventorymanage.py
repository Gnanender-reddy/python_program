'''
@Author: P.Gnanender Reddy
@Since : Dec'19
Keywords: json.
Description: In this we created management system to adding data to json file and also I created manager class and
in that adding inventory function is created so that data  will be added to json file.
'''
import json
class Manager:
    '''
    This manager class having functions like inventory factory and adding inventory.
    '''
    def __init__(self,file):
        '''
        Taking file as input
        '''
        self.file=file
        self.inventory=None
    def inventory_factory(self):
        '''
        This function provides total cost of item ny multiplying weight and price of item.
        '''
        with open(self.file) as f:
            #opening file as f
            self.inventory=json.load(f)
            #loading data to inventory
        for item in self.inventory["Inventory"]:
            #looping thrrough the items.
            print({item['weight'] * item['price/kg']})
    def adding_inventory(self):
        '''
        this function provides access to user for adding items to inventory.
        '''
        product=input("enter product name ")
        #user input
        product_weight=int(input("enter product weight"))
        #asking user to provide product weight
        product_price=int(input("enter product price"))
        #asking user to provide product price
        with open(self.file,'r+') as f:
            data={}
            #taking empty dictionary
            data['name']=product
            #adding product
            data['weight']=product_weight
            #adding product weight
            data['price/kg']=product_price
            #adding product price
            self.inventory["Inventory"].append(data)
            #appending data
            json.dump(self.inventory,f,indent=2)
            #dumping data to json file
if __name__ == '__main__':
    manager=Manager("Inventorymanage.json")
    #creating Manager object
    manager.inventory_factory()
    #using Manager object calling inventory factory method.
    manager.adding_inventory()
    #using manager object calling adding inventory method














































# class InventoryManager:
#     def __int__(self):
#         self.list=[]
#
#         # with open("inventorymanage.json") as file:
#         #     data=json.load(file)
#         # for item in data:
#         #     list.append(item)
#
#     def add_inventory(self):
#         inventory={}
#         # inventory={
#         #     'name':' ',
#         #     'weight':' ',
#         #     'price_kg':' '
#         #
#         #        }
#         names=input("enter product name in alphabets")
#         #if not names.isalpha():
#             #names=input("enter product name in alphabets")
#
#         weights=input("enter product weight")
#         #if not weights.isnumeric():
#             #weights=int(input("enter product weight in number formart"))
#
#         price_kgs=input("enter product price per kg ")
#         #if not price_kgs.isalpha():
#             #price_kgs=input("enter product price in number format")
#         # inventory['name']=names
#         # inventory['weight']=weights
#         # inventory['price_kg']=price_kgs
#         # print(inventory)
#
#         inventory={
#             "name":names,
#             "weight":weights,
#             "price":price_kgs
#         }
#         return inventory
#         data=self.list.append(inventory)
#         print(data)
#
#
# inventorymanger=InventoryManager()
# inventorymanger.add_inventory()
# # inventorymanger.write()
# #
# # with open("Inventorymanage.json") as json_file:
# #     data=json.load(json_file)
# #
# #
#


