#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 00:40:54 2019

@author: pp
"""

from PlayingCard import PlayingCardClass
from Dealer import DealerClass
from Player import PlayerClass
import time

print("GAME STARTS \n \n")

theDeck = DealerClass()
humanPlayer = PlayerClass("Player 1")
aiPlayer = PlayerClass("The Dealer")

print("Dealing cards.. \n \n")

theDeck.ShuffleCards()
humanPlayer.givePlayerCard(theDeck.topCard())
aiPlayer.givePlayerCard(theDeck.topCard())
humanPlayer.givePlayerCard(theDeck.topCard())
aiPlayer.givePlayerCard(theDeck.topCard())

print("Game begins.. \n")
Winner = None

#Player turn
playerTurnEnded = False
while playerTurnEnded is not True:
    print("\n============================================================ \n")
    print("Current hand: ", humanPlayer.displayHand(), "(current score: ", humanPlayer.getPlayerScore(),")")
    playerTurnInput = input("Do you want to Stop (S) or Hit (H)?")
    
    if playerTurnInput.upper() == "S":
        playerTurnEnded = True
        print("Player decided to stick")
    elif playerTurnInput.upper() == "H":
        humanPlayer.givePlayerCard(theDeck.topCard())
        print("\ncard dealt: ", humanPlayer.hand[-1].MyName(), "(bringing your score to: ", humanPlayer.getPlayerScore(),")")
        if humanPlayer.getIsPlayerBroke() is True:
            playerTurnEnded = True
            print("You've gone bust!!!")
            Winner = aiPlayer
    else:
        print("You stupid! Try again Fool!")
    time.sleep(1) #delay for visual effect
        
#Dealer Turn
aiPlayerTurnEnded = False
if Winner is aiPlayer:
    aiPlayerTurnEnded = True
while aiPlayerTurnEnded is not True:
    print("\n============================================================ \n")
    print("Dealer's current hand: ", aiPlayer.displayHand(), "(Dealer's current score: ", aiPlayer.getPlayerScore(), ")")
    
    if aiPlayer.getPlayerScore() < humanPlayer.getPlayerScore():
        aiPlayer.givePlayerCard(theDeck.topCard())
        print("\ncard dealt: ", aiPlayer.hand[-1].MyName(), "(bringing the dealer's score to: ", aiPlayer.getPlayerScore(),")")
        if aiPlayer.getIsPlayerBroke() is True:
            aiPlayerTurnEnded = True
            print("Dealer went bust!!!")
            Winner = humanPlayer
    else:
        print("\nDealer decided to stick")
        aiPlayerTurnEnded = True
        Winner = aiPlayer
    time.sleep(2) #delay for visual effect
    
    

print("\n============================================================ \n")
print("\nPlayer's final hand: ", humanPlayer.displayHand(), "(final score: ", humanPlayer.getPlayerScore(), ")")
print("\nDealer's final hand: ", aiPlayer.displayHand(), "(final score: ", aiPlayer.getPlayerScore(), ")")
print("\n The Winner was ", Winner.playerName, "!!!!!")