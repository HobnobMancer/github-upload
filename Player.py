#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:07:35 2019

@author: pp
"""
from PlayingCard import PlayingCardClass

class PlayerClass:
    
    def __init__(self, name):
        self.playerName = name
        self.hand = []
        

    def displayHand(self):
        display = ""
        for card in self.hand:
            if(display==""):
                display = display + card.MyName()
            else:
                display = display +  ", " + card.MyName()
        return display
    

    def getPlayerScore(self):
        playerScore = 0
        for card in self.hand:
            playerScore = playerScore + card.MyValue()
            
        return playerScore
    
    
    def getIsPlayerBroke(self):
        if self.getPlayerScore() > 21:
            return True
        else:
            return False
        

    def givePlayerCard(self, newCard):
        self.hand.append(newCard)
        