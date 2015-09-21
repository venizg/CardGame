# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 17:03:15 2014

@author: George
"""
#Imports
import random
from GlobalVariables import *



#Classes

class Player:
    def __init__(self, name = None):
        self.name = name
        self.hand = []
        
    

class Card:
    
    def __init__(self, rank = None, suit = None):
        self._rank = rank
        self._suit = suit
    
    def printSuit(self):
        print(self._suit)
    
    def printRank(self):
        print(self._rank)
        
    def printCard(self):
        print(self._rank + ' of ' + self._suit + 's')
    
    
    
class Deck:
    
    def __init__(self, deckType = None):
        self._cards = []
        self._deckType = None
        
        if deckType is standardDeck:
            self.makeStandardDeck()
        if deckType is emptyDeck:
            self.makeEmptyDeck()
        else:
            self.makeStandardDeck()
            
    def makeStandardDeck(self):
        self._deckType = standardDeck
        self._cards = []        
        
        tempCardSuits = cardSuits[:]
        tempCardRanks = cardRanks[:]
        tempCardRanks.remove(joker)

        for i in tempCardRanks:
            for j in tempCardSuits:
                self._cards.append(Card(rank = i, suit = j))
    
    def makeEmptyDeck(self):
        self._deckType = emptyDeck
        self._cards = []
    
    def drawCards(self, number = 1):
        if type(number) is not int or number < 1:
            number = 1
            
        cardsDrawn = []
        for i in range(number):
            cardsDrawn.append(self._cards.pop(0))
            if self._cards == []:
                return cardsDrawn
        return cardsDrawn
       
    def shuffle(self):
        random.shuffle(self._cards)   
        
    def getSize(self):
        return len(self._cards)
        
    def printDeck(self):
        for x in range(self.getSize()):
            self._cards[x].printCard()
        

        
        
        
#Testing Ground
#myDeck = Deck()
#myDeck.shuffle()
#hand = []
#hand.extend(myDeck.drawCards(7))
#
#myDeck.printDeck()
#print('-----------------------')
#for i in range(len(hand)):
#    hand[i].printCard()        
#        
#        
        
        
        
        
        