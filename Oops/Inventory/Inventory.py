"""
@Author: P.Gnanender Reddy
@since: Dec'19
Keywords: json
Description: In this code, details of each and every product details like weight, price printed.
"""


import json
class Inven:
    """
    Summary:This Inven class consists of inven details.

    """
    def __init__(self,file):
        """
        Summary:Initializing the instance of this class.
        """
        self.file=file
    def inven_details(self):
        """
        Summary:This function loads data and produce all details of the product
        """
        with open("Inventory.json") as json_file:
            data=json.load(json_file)
        for item in data["Inventory"]:
            total=item['weight']*item['price/kg']
            print("The item is",item["name"],",weight is",item["weight"],",price per kg is",item["price/kg"],
              ",price total is",total)
if __name__ == '__main__':
    """
    Summary:Driver code
    """
    inven=Inven("Inventory.json")
    inven.inven_details()