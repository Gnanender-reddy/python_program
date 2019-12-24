"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Abstraction,Adapter pattern.
@Description:This code is for is one of the structural design pattern and its used so that two unrelated interfaces can
work together. The object that joins these unrelated interface is called an Adapter. Use Adapter design pattern to solve
mobile charger which adapts to a Mobile battery needs 3 volts to charge but the normal socket produces either 120V (US)
or 240V (India). So the mobile charger works as an adapter between mobile charging socket and the wall socket.
"""
from abc import ABC, abstractmethod


class socket(ABC):
    """class socket is a abstract class having an abstract method"""
    @abstractmethod
    def get_volts(self):
        """get and return a value from instance"""
        return

    @abstractmethod
    def set_volts(self):
        """set a value in the instance"""
        return


class socket_adaptor(socket):
    """
    Summary:This class is used to implements a socket class methods
    """
    def __init__(self, volts):
        """
        Summary:Initializing new instance of a class
        """
        self._volts = volts

    def get_volts(self):
        """
        Summary:This function is used to take a value of input voltage from user
        :returns: return a value of input voltage to child class"""
        return self._volts

    def set_volts(self):
        """
        Summary:This function is used to take a input voltage and convert it into required output voltage and return
        :returns: return a required output voltage to child class
        """
        if self._volts == 120:
            self._volts = self._volts // 40
            return self._volts
        else:
            self._volts = self._volts // 80
            return self._volts


class mobile_charger(socket_adaptor):
    """
    summary:- This class is inherited from socket_adaptor class and used to access a method of it
    and display a input and output voltage
    """
    def __init__(self, volts):
        """
        Summary:Initializing new instance of a class and also initializing instance of super class.
        """
        super().__init__(volts)
        self._get_volts = super().get_volts()
        self._set_volts = super().set_volts()

    def display(self):
        print("Input voltage is: ", self._get_volts)
        print("Output Voltage is: ", self._set_volts)

    @property
    def set_volts(self):
        return self._set_volts


def main():
    """Summary:This function is used to perform input operation"""
    while 1:
        try:
            choice = int(
                input("\n1.for input voltage is: 120\n2.for input voltage is: 240\n3.for exit\nEnter a choice for "
                      "input voltage: "))
            if choice == 1:
                m = mobile_charger(120)
                m.display()
            elif choice == 2:
                m = mobile_charger(240)
                m.display()
            elif choice == 3:
                break
            else:
                print("Enter a valid input ")
        except ValueError:
            print("Enter a valid integer input: ")


if __name__ == '__main__':
    """
    Summary:Driver code.
    """
    main()