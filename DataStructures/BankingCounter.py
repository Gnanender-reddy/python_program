from com.bridgelabz.DataStructures.Utility1 import Queue

#creating a class for bankingcashcounter
class BankingCashCounter:
    s=Queue()
    balance=800
    while True:
        panel = int(input("enter number of people")) #creating panel for people
        for i in range(1, panel+1):
            s.enqueue(i)                             #adding people to queue
            print("Enter", i, " person")
            #Providing choice to person for transactions
            choice = int(input(" Enter 1 for deposit\n Enter 2 for withdrawing money\n Enter 3 for displaying amount\n Enter 4 for exit \n Enter 5 to get out from panel"))
            if choice == 1:
                #Asking user to enter amount for deposit
                amount = int(input("enter money to deposited"))
                #Entered amount is added to balance
                balance += amount
                #printing current balance
                print("your current balance is", balance)
                choice = int(input(
                    " Enter 1 for deposit\n Enter 2 for withdrawing money\n Enter 3 for displaying amount\n Enter 4 for exit\n Enter 5 to get out from panel"))

            if choice == 2:
                #Asking user to enter amount for withdrawing
                amount = int(input("enter amount for withdrawing money"))
                if amount > balance:
                    #if amount is greater than balance then user will get output as insufficient balance
                    print("sorry insufficient balance")
                else:
                    #amount is subtracted from current balance, so that balance amount gets updated
                    balance = balance - amount
                    #providing amount to user
                    print("withdraw successfull:",amount)

            if choice == 3:
                #Showing current balance to user
                print("your balance is", balance)
                choice = int(input(
                    " Enter 1 for deposit\n Enter 2 for withdrawing money\n Enter 3 for displaying amount\n Enter 4 for exit \n Enter 5 to get out from panel"))

            if choice == 4:
                #This is for successfull transaction
                print("your transaction is successfull")
            if choice==5:
                print("You exit from panel")
                exit()


    exit()





