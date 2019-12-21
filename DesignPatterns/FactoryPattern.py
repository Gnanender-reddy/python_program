from abc import ABC, abstractmethod
import re

class Computer(ABC):
    @abstractmethod
    def getprocessor(self,processor):
        pass

    @abstractmethod
    def getram(self,ram):
        pass
    @abstractmethod
    def getstorage(self,storage):
        pass



class Server(Computer):
    def __init__(self,ram,storage,processor,skincolor):
        self.skincolor=skincolor
        self.ram=ram
        self.storage=storage
        self.processor=processor
    def getskincolor(self):
        print("skin color",self.skincolor)

    def getram(self):
        print("Ram:",self.ram)


    def getstorage(self):
        print("Storage: ",self.storage)


    def getprocessor(self):
        print("Processor: ",self.processor)


class Laptop(Computer):
    def __init__(self,ram,storage,processor,color):
        self.color=color
        self.ram=ram
        self.storage=storage
        self.processor = processor
    def getcolor(self):
        print("color: ",self.color)
    def getram(self):
        print("Ram: ",self.ram)

    def getstorage(self):
        print("Storage: ",self.storage)

    def getprocessor(self):
        print("Processor: ",self.processor)

def main():
    print("Welcome to computer factory")
    try:
        option = int(input("Enter 1 to buy laptop\nEnter 2 to buy server computer"))

        if option == 1:
            print("please provide your laptop specifications")
            ram=input("Enter ram=")
            storage=input("Enter storage=")
            processor=input("Enter processor=")
            color=input("Enter color=")

            laptop = Laptop(ram, storage, processor, color)
            print("Your laptop is ready")

            laptop.getram()
            laptop.getprocessor()
            laptop.getstorage()
            laptop.getcolor()
        if option == 2:
            print("please provide your server computer specifications")
            ram = input("enter ram=")
            storage = input("enter storage=")
            processor = input("enter processor=")
            skincolor = input("enter color=")
            server = Server(ram,storage,processor,skincolor)
            print("your server computer is ready")
            server.getram()
            server.getprocessor()
            server.getstorage()
            server.getskincolor()
    except ValueError:
        print("Please provide valid data")
        main()

