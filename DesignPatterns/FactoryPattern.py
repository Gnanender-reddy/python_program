"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Abstraction,Factory pattern.
@Description:This code is for Computer Factory that can Produce Laptop and Server Class Computers.Abstract class for
Computer is designed and  Laptop, Server inherit from Computer and computerFactory is able to create the corresponding
Computer Object on request.
"""
from abc import ABC, abstractmethod


class Computer(ABC):
    """
    Summary: This computer class is abstraction class. And it contains abstract methods like get color,get ram,display
    specifications.
    """
    @abstractmethod
    def getColor(self):
        """
        Summary:This method is an abstract method, which is incomplete method(no definition).And this method is impleme-
        -nted in subclass.
        """
        pass

    @abstractmethod
    def getRam(self):
        """
        Summary:This method is an abstract method, which is incomplete method(no definition).And this method is impleme-
        -nted in subclass.
        """
        pass

    @abstractmethod
    def displaySpecifications(self):
        """
        Summary:This method is an abstract method, which is incomplete method(no definition).And this method is impleme-
        -nted in subclass.
        """
        pass


class Server(Computer):
    """
    summary: This sever class provides server computer according to specifications provided by customer.
    """
    def __init__(self):
        """
        Summary:Initializes new instance of this class, inheriting super class here.
        """
        super().__init__()
        self.color = self.getColor()
        self.ram=self.getRam()
        self.processor=self.getProcessor()


    def getColor(self):
       col = input("Input Color :\t")
       return col

    def getRam(self):
        """
        Summary: This function provides ram to server computer.
        """
        ram=int(input("input ram:\t"))
        return ram

    def getProcessor(self):
        """
        Summary: This function provides processsor for server computer.
        """
        processor = int(input("Input processor :\t"))
        return processor

    def displaySpec(self):
        """
        Summary:This function display specifications of server computer.
        """
        print("Your server computer is ready")
        print("color: ", self.color)
        print("Ram: ", self.ram)
        print("processor: ", self.processor)


class Laptop(Computer):
    """
    Summary:This laptop class contains three methods,get color for laptop, get ram for laptop, get processor for laptop.
    """
    def __init__(self):
        """
        Summary:Initializes new instance of this class, and also inheriting computer class and also initializing super
        class methods.
        """
        super().__init__()
        self.color = self.getColor()
        self.ram=self.getRam()
        self.processor=self.getProcessor()

    def getcolor(self):
        """
        Summary:This function getcolor provides color to laptop.
        """
        col = input("Please provide your Color :\t")
        return col

    def getProcessor(self):
        """
        Summary:This function getprocessor provides processor to laptop.
        """
        processor = int(input("please provide your processor :\t"))
        return processor

    def getRam(self):
        """
        Summary:This function get ram provides ram to laptop.
        """
        ram=int(input("please provide your ram :\t"))
        return ram

    def displaySpec(self):
        """
        Summary:This function provides specifications of laptop.
        """
        print("Your server is ready")
        print("Color: ",self.color)
        print("Ram: ",self.ram)
        print("processor: ",self.processor)




class ComputerFactory():
    """
    Summary:This computer factory class takes input from user, according to user wish, this computer factory produces
    laptop or server computer.
    """

    def choice(self):
        """
        Summary: This choice function provides options to user, so that customer can select according to his wish,
        if customer chooses 1st option  it produces laptop, and if customer chooses then it produces server computer.
        """
        try:
            user_choice = int(input("Enter 1 to  buy a laptop \nEnter 2 for server computer"))
            if user_choice>2:
                print("please enter data in 1 or 2")
                self.choice()
            else:
                if user_choice==1:
                    return Laptop()
                elif user_choice==2:
                    return Server()
        except ValueError:
            print("please enter data in number formnat")
            self.choice()

if __name__ == '__main__':
    """
    Main driver code.
    """

    cf = ComputerFactory()
    c = cf.choice()#o/p:Laptop or server
    c.displaySpec()