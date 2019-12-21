'''
@Author:P.Gnanender Reddy
@Since: Dec'19
Description: This code is implemented for finding top companies shares..etc.
'''



import json


class Stock:
    '''
    This stock class contains functions like stock calculation and calculation for one company
    '''
    def __init__(self,file):
        self.file=file
        self.data1=None

    def stock_calculation(self):
        '''
        this function works like, it provides each and every company stock calculation
        '''
        print("Here you can find each and every company's calculation\n")
        with open(self.file) as f:
            self.data1=json.load(f)
        with open(self.file,'r+') as f:
            for item in self.data1['stock']:
                    print("The company name is",item['names'],",its share is",item['share'],"and its price is",item['price'],"total price is", item['share']*item['price'])
            print("\n")

    def calculation_one(self):
            '''
            this function provides one report according to company name provided by user
            '''
            try:
                company_name=input("Enter company name for which you want to find total price")
                with open(self.file) as f:
                    self.data1=json.load(f)
                with open (self.file,'r+') as f:
                    for item in self.data1['stock']:
                        if item['names']==company_name:
                            print("The company name is",item['names'],"and its share is",item['share'],"and its price is ",item['price'],"total price is ",item['price']*item['share'])

            except NameError:
                print("Enter correct data")




def main():
    '''
    Driver code: Execution starts here
    '''
    if __name__ == '__main__':
        stock=Stock("stock.json")
        print("welcome to stock management")
        while True:

                try:

                    option=int(input("Enter 1 for finding each company total price\nEnter 2 for finding only one company total price according to your opinion\nEnter 3 for exit"))
                    if option==1:
                        stock.stock_calculation()
                        main()
                    if option==2:
                        stock.calculation_one()
                    if option==3:
                        print("Thank you for choosing us")
                        exit()
                        break
                    if option>3:
                        print("Enter values below 4 ")
                        main()
                except ValueError:
                    print("Enter Valid data")
                    main()
main() #calling main function here