# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 18:20:58 2014

@author: George
"""

from CardGameBasics import Deck, Player
from GlobalVariables import *

trump = 'Spade'

class HeartsPlayer(Player):
    def __init__(self, name = None, game = None):
        Player.__init__(self, name)
        self.game = None
        self.score = 0
        self.tricks = []
        
        
    def playCard(self, Card):
        if self.hand.count(Card):
            self.hand.remove(Card)
            self.game.stack.addCardToStack(Card, self)
            
    def takeTrick(self, trick):
        self.tricks.append(trick)
            
    def printHand(self):
        for card in self.hand:
            card.printCard()
                
    def printAllTricks(self):
        for trick in self.tricks:
            for card in trick:
                card.printCard()                
            print('-----------')    
        
class Stack:
    def __init__(self):
        self.firstSuit = None
        self.cardsInStack = []
        self.cardOwners = {}
        
    def givePlayerTrick(self, Player):
        trick = self.cardsInStack
        self.cardsInStack = []
        self.cardOwners = {}
        Player.takeTrick(trick)
        
    def addCardToStack(self, Card, Player):
        self.cardsInStack.append(Card)
        self.cardOwners[Card] = Player
        
    def printStack(self):
        for card in self.cardsInStack:
            card.printCard()
        

class HeartsGame:
    def __init__(self):
        self.deck = Deck(standardDeck)
        self.deck.shuffle()
        self.players = []
        self.stack = Stack()
        self.isTrumpBroken = False
#        self.previousTrickWinner
        
        

heartsGame = HeartsGame()        
johny = HeartsPlayer()
johny.name = 'johny'
johny.game = heartsGame


johny.hand.extend(johny.game.deck.drawCards(8))
#johny.printHand()
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
#print('-------------')
#johny.printHand()
heartsGame.stack.givePlayerTrick(johny)
johny.printAllTricks()
print('***********')
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
johny.playCard(johny.hand[0])
heartsGame.stack.givePlayerTrick(johny)
johny.printAllTricks()