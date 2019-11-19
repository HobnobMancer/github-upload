#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 00:48:26 2019

@author: pp
"""
import random
from PlayingCard import PlayingCardClass

class DealerClass:
       
    def __init__(self):
         self.myDeck = []
         self.lastCard=-1
    
    def ShuffleCards(self):
        suits = ["♠","♥","♦","♣"]
        faceCards = {11:"J", 12:"Q", 13:"K", 1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6",7:"7", 8:"8", 9:"9", 10:"10"}
        tempDeck = []
        
        for mySuit in suits:
            numberRan = range(1,14)
            for cardNo in numberRan:  
                cardScore = cardNo
                if cardScore>10:
                    cardScore=10
                newCard =  PlayingCardClass(faceCards.get(cardNo)+mySuit, cardScore)
                tempDeck.append(newCard)
                
        while len(tempDeck) > 0:
            myRandomNumber = random.randint(0,len(tempDeck)-1)
            self.myDeck.append(tempDeck[myRandomNumber])
            tempDeck.remove(tempDeck[myRandomNumber])

    def topCard(self):
        self.lastCard = self.lastCard + 1
        return self.myDeck[self.lastCard]