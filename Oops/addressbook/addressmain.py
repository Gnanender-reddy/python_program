'''
@Author: P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Exception handling,abstraction,encapsulation,abstraction.
@Description:This is graphical user interface for addressbook. In this we created main function for address book and imported functions from addressbook class.
'''

from com.bridgelabz.Oops.addressbook.addressbook import Addressbook


class Address_Main(Addressbook):
    '''
    This is main class, inheritance is used so that we can reuse the code and also functions like adding data, deleting
    data, updating data which are from other class are called here.
    '''


    def __init__(self,file):
        '''
        This funcion is called constructor, which is used for constructing object.
        '''


        self.file=file



    def main(self):
        '''
        This function provides options for user, so that user can choose options according to his requirement.
        '''


        print("Welcome to Address Book")

        while True:

            #This loop iterates until user exit from this function.After user exit, this loop will be terminated.
            


            try:
                print("Enter 1 for adding details\nEnter 2 for updating\nEnter 3 for deleting whole data\nEnter 4 for exit")

                option = int(input("Please choose your option between 1 to 4"))

                #providing access to user so that he choose option between 1 to 4.

                if 1 <= option <= 4:

                    #If user enter options between 1 to 4, execution enters here.


                    if option == 1:

                        #Option 1 is for adding details.

                        address.add_details()

                    if option == 2:

                        #Option 2 is for updating details.

                        address.update_details()

                    if option == 3:

                        #Option 3 is for deleting data.

                        address.delete_data()

                    if option == 4:

                        #Option 4 is for exit.

                        print("Thank you for choosing us")
                        exit()
                if option > 4 and option ==0:

                    #If option is greater than 4 and equal to 0, asking user provide valid data.

                    print("enter valid data")
                    address.main()
            except ValueError:
                print("Please provide valid data")
                address.main()


if __name__ == '__main__':


    #Interpretor starts execution here.


    address=Address_Main("addressbook.json")
    address.main()