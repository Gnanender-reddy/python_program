'''
@Author:P.Gnanender Reddy
@Since:dec'19
@Keywords:json
@Description: This code is for shuffling the cards using Random method and then distribute 9 Cards to 4 Players.

'''
import random
class card:
    """
    Summary:This class is for providing cards for deck of cards.
    """
    def __init__(self,suit,rank):
        """

        Summary: This function is for initializing instance.

        """
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    suits=["diamonds","club","spade","heart"]
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    def __init__(self):
        """
        Summary:In initializing instance for this  class.
        """
        self.deck=[]
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(card(suit,rank))
    def shuffle(self):
        """
        Summary:this function shuffles cards,like mixing cars
        """
        number=int(input("enter any number to shuffle"))
        for i in range(number):
            random.shuffle(self.deck)
    def deal(self):
        """
        Summary: This function provides deal to players
        """
        return self.deck.pop()
    def show(self):
        """
        Summary:This function provides displaying cards
        """
        for item in self.deck:
            print(item)
    def distribute_to_players(self):
        """
        Summary:This function distributes card to players
        """
        player=[]
        #taking an empty list
        for i in range(4):
            #looping
            players=[]
            for j in range(9):
                player.append(self.deal())
            players.append(player)
        return players
















# from random import random
#
#
# class card:
#     def __init__(self,suit,val):
#         self.suit=suit
#         self.value=val
#     def show(self):
#         print("{} of {}".format(self.value,self.suit))
#
# card=card("card",6)
# card.show()
#
# class Deck:
#     def __init__(self):
#         self.cards=[]
#         self.build()
#     def build(self):
#         for s in ["spades","clubs","diamonds","hearts"]:
#             for v in range(1,14):
#                 self.cards.append(card(s,v))
#     def show(self):
#         for c in self.cards:
#             c.show()
#
#
#     def shuffle(self):
#         for i in range(len(self.cards)-1,0,1):
#             r=random.radint(0,i)
#             self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
#
#
#     def drawcard(self):
#         self.hand.append(deck.drawcard())
#         return self
#
#
#
#
#
#
#
#
# class player:
#     def __init__(self,name):
#         self.name=name
#         self.hand=[]
#     def draw(self,deck):
#         self.hand.append(deck.drawcard())
#         return self
#     def showhand(self):
#         for card in self.hand:
#             card.show()
# deck=Deck()
# deck.shuffle()
# bob=player("Bob")
# bob.draw(deck)
# bob.showhand()

