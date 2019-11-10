#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:12:41 2019

@author: charles
"""

import random

suits = ("Hearts", "Spades", "Clubs", "Diamonds" )
ranks = ("Two", "Three", "Four", "Five", "Six", 
         "Seven", "Eight", "Nine", "Ten", 
         "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, 
          "Six":6, "Seven":7, "Eight":8, "Nine":9, 
          "Ten":10, "Jack":10, "Queen":10, 
          "King":10, "Ace":11 }

playing = True

#Consider making a Card class where each Card 
#object has a suit and a rank, then a Deck class 
#to hold all 52 Card objects, and can be shuffled, 
#and finally a Hand class that holds those Cards 
#that have been dealt to each player from the Deck.

class Card:
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                pass
                
    def __str__(self):
        pass
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):    
        pass   
    
test_deck = Deck()
print(test_deck)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        pass
    
    def adjust_for_ace(self):
        pass
    
        