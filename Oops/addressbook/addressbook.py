'''
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:json,encapsulation.
@Description:In this we defined class along with three definitions.They are Adding details function in address book, updating data in
address book and deleting data in address book.
'''

import json


class Addressbook:
    '''
    In this class we created functions like adding details,updating details,deleting data.
    '''

    def __init__(self, file):
        self.file = file
        self.data1 = None

    def add_details(self):
        '''
        This function helps us in adding details in address book, it takes users first name, last name, address, city,
        phone number, zip code.
        '''

        try:
            __firstname = input("enter your first name")

            # Providing access to user to provide his first name, so that user's data can be added to address book,
            # and also first name attribute is protected here

            while not __firstname.isalpha():
                # if user entered wrong data, this condition asks user again to provide valid data

                __firstname = input("enter your valid first name")

            __lastname = input("enter your last name")

            # Providing access to user to provide his last name,so that user's data can be added to address book,
            # and also last name attribute is protected here

            while not __lastname.isalpha():
                #checking if last name is not in alphabets then asking user again to enter valid data
                __lastname = input("enter your valid last name")

            __address = input("enter your address")

            while not __address.isalpha():
                #  if address is not in alphabets then asking user again to enter valid data
                __address = input("enter your valid address")

            __city = input("enter your city")
            #  if city is not in alphabets then asking user again to enter valid data
            while not __city.isalpha():
                __city = input("enter your valid city name")

            __state = input("enter your state")
            while not __state.isalpha():
                #  if state is not in alphabets then asking user again to enter valid data
                __state = input("enter your valid state name")

            __zp = input("enter your zip code")
            while __zp.isalpha():
                #  if zip code is in alphabets then asking user again to enter valid data
                __zp = input("enter your valid zip code")

            __phone = input("enter your phone number")
            while __phone.isalpha():
                #if phone number is in alphabets then askig user to provide valid data.
                __phone = input("enter your valid phone number")

            with open(self.file, 'r+') as f:
                #opening file
                self.data1 = json.load(f)
                #loading json file
            print("your details are successfully added")

            data = {}
            #empty dictionary

            data["first_name"] = __firstname
            data["last_name"] = __lastname
            data["address"] = __address
            data["city"] = __city
            data["state"] = __state
            data["zip"] = __zp
            data["Phone_number"] = __phone
            self.data1["address"].append(data)

            # adding data to file.

            with open(self.file, 'w') as f:

                # opening json file and dumping data to it

                json.dump(self.data1, f, indent=2)

        except ValueError:
            print("provide valid data")

    def update_details(self):
            '''
            This function works in way that it provides access to user to update his/her details,
            First it opens json file and load data in object and takes input from user, so that it
            adds data to json file.
            '''

            with open(self.file, 'r+') as f:
                # opening file
                self.data1 = json.load(f)
                #loading json data
            first_name = input("enter your first name")
            #Taking input from user
            if not first_name.isalpha():
                #isalpha() function is used for checking if alphabets are present.
                print("please enter your first name in alphabets")
                #if entered name is not in alphabets, then again asking user to enter valid data in alphabets.
            last_name = input("enter your last name")
                #Taking input from user
            if not last_name.isalpha():
                #Checking entered name is in alphabets or not.
                print("enter your last name in alphabets")
                #if entered name is not in alphabets then asking user again to enter valid data
            for item in self.data1['address']:
                #This for loop is for looping(travelling) through the data

                if item['first_name'] == first_name and item['last_name'] == last_name:
                    #if first name in the data is equal to data which is present in json data, then user can update
                    #his details.

                    print(
                        "Enter 1 for editing first name\n Enter 2 for editing last name\n enter 3 for editing your address\n"
                        "Enter 4 for editing your city\n Enter 5 for editing your state\n Enter 6 for editing your zip code\n"
                        "Enter 7 for editing your phone number ")
                    choice = int(input("Enter your choice between 1 to 7"))
                    #providing choice to user.

                    if choice == 1:
                        #for above choice he can update his first name.
                        fn = input("enter your first name to be replaced in old first name")
                        item['first_name'] = fn
                        print("your first name is updated successfully")
                        while not fn.isalpha():
                            fn = input("Please enter your valid first name to be replaced in old first name")
                            item['first_name'] = fn
                            print("your first name is updated successfully")

                    if choice == 2:
                        #For above choice he can update his last name.
                        ln = input("enter your last name to be replaced in old last name ")
                        item['last_name'] = ln
                        print("your last name is updated successfully")
                        while not ln.isalpha():
                            ln = input("Please enter your valid last name to be replaced in old last name ")
                            item['last_name'] = ln
                            print("your last name is updated successfully")


                    if choice == 3:
                        #this option is for updating address
                        ad = input("enter your address to be replaced in old address ")
                        item['address'] = ad
                        print("your address is updated successfully")
                        while not ad.isalpha():
                            ad = input("Please enter your valid address to be replaced in old address ")
                            item['address'] = ad
                            print("your address is updated successfully")


                    if choice == 4:
                        #this option is for updating city name
                        ct = input("enter your city to be replaced in old city name ")
                        item['city'] = ct
                        print("your city name is updated successfully")
                        while not ct.isalpha():
                            ct = input("Please enter your valid city name to be replaced in old city name ")
                            item['city'] = ct
                            print("your city name is updated successfully")

                    if choice == 5:
                        #this option is for updating state name.
                        st = input("enter your state name to be replaced in old state name ")
                        item['state'] = st
                        print("your state name is updated successfully")
                        while not st.isalpha():
                            st = input("please enter valid state name to be replaced in old state name ")
                            item['state'] = st
                            print("your state name is updated successfully")

                    if choice == 6:
                        #this option is for updating zip code
                        zp = input("enter your zip code to be replaced in old zip code ")
                        #
                        item['zip'] = zp
                        print("your zip code is updated successfully")
                        while zp.isalpha():
                            zp = input("please enter your valid zip code to be replaced in old zip code ")
                            item['zip'] = zp
                            print("your zip code is updated successfully")

                    if choice == 7:
                        #this option is for updating phone number
                        phone = input("enter your last number to be replaced in old number ")
                        item['Phone_number'] = phone
                        print("your phone number is updated successfully")
                        while phone.isalpha():
                            phone = input("Please enter your valid last number to be replaced in old number ")
                            item['Phone_number'] = phone
                            print("your phone number is updated successfully")
                    break
                else:
                    print("values are not matching")
                    break


            with open(self.file, 'w') as f:
                #dumping data to json
                json.dump(self.data1, f, indent=2)



    def delete_data(self):
        '''
        This function helps us in deleting data in address book, taking first name as input, using first name data
        will be deleted.
        '''

        with open(self.file, 'r+') as f:
            #this is for opening a file
            self.data1 = json.load(f)

        firstname = input("please enter your first name to delete your whole data")
        #asking user to enter his first name to delete

        while not firstname.isalpha():
            #if entered first name is not in alphabets, asking user again to enter valid first name.
            firstname = input("please enter your valid first name to delete your whole data")

        count = 0
        #initialising count variable to zero value.
        for item in self.data1['address']:
            #looping through data

            if firstname == item['first_name']:
                del (self.data1['address'][count])
                print("Your data is deleted successfully")


            else:
                count += 1
                #incrementing count variable


        with open(self.file, 'w') as f:
            #This is dumping code to json.
            json.dump(self.data1, f, indent=2)

