"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:mediator pattern.
@Description:This code Mediator pattern focuses on provide a mediator between objects for communication and help in
implementing loose-coupling between objects.

"""

class Mediator():
    """
    Summary: This mediator class contains method like message transfer which mediates between objects.
    """
    def __init__(self):
        """
        Summary: This fucnction is for initializing the instance.
        """

        self.colleage1=colleage1(self)
        self.colleage2=colleage2(self)
    def messageTransfer(self):
        mediator=self.colleage1.send("colleage1:He is telling to mediator that Iam here")
        print(mediator)
        print("Mediator transfered this message")
        print(self.colleage2.receive("colleage2:Yes i received"))


class colleage1():
    """
    Summary
    """
    def __init__(self,mediator):
        """
        Summary:Initialising the instance.

        """
        self.mediator=mediator

    def send(self,msg):
        """
        Summary:This for sending the message to mediator.

        """
        return msg



class colleage2():
    """
    Summary: This class is for colleage2 in which he is receiving message from mediator.
    """
    def __init__(self,mediator):
        """

        Summary: Initializing the instance.
        """
        self.mediator=mediator
    def receive(self,mediator):
        """
        Summary : This function is for receiving message from mediator which is sent by colleage2.
        :param mediator:

        """
        return mediator


if __name__ == '__main__':
    """
    Summary: Driver Code
    """
    mediator=Mediator()
    mediator.messageTransfer()
