"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Abstraction,Observer pattern.
@Description: In observer pattern, the object that watch on the state of another object are called Observer and the obj-
-ect that is being watched is called Subject.This code is for observer pattern.

"""
class Subscriber:
    """
    Summary:This class is for, if subscriber got update, it will notify.
    """
    def __init__(self,name):
        """
        Summary:Initialising new instance of a class.
        """
        self.name=name
    def update(self,message):
        """
        Summary : This function is for updating the subscriber.


        """
        print('{} got message"{}"'.format(self.name,message))
class Publisher:
    """
    Summmary: This class contains methods like register, unregister,dispatch.
    """
    def __init__(self):
        """
        Summary : This is like constructor  used for initializing the new instance of this class.
        """
        self.subscribers=set()

    def register(self,who):
        """
        Summary: This fucntion is used for registration for subscriber.


        """
        self.subscribers.add(who)
    def unregister(self,who):
        """
        Summary: This fuction is used for unregistration.


        """

        self.subscribers.discard(who)
    def dispatch(self,message):
        """
        Summary: This fucntion is used for dispatching the message to subscribers.

        """
        for subscriber in self.subscribers:
            subscriber.update(message)
if __name__ == '__main__':

    """
    Summary : this is the driver code.
    """
    pub=Publisher()
    bob=Subscriber('bob')
    alice=Subscriber('alice')
    john=Subscriber('john')
    pub.register(bob)
    pub.register(alice)
    pub.register(john)
    pub.dispatch("Its lunch time")
    pub.unregister(john)
    pub.dispatch("time for dinner")
