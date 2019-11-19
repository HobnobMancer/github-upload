#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 00:27:37 2019

@author: pp
"""

class PlayingCardClass:
    
    def __init__(self, name, value):
        self._MyName = name
        self._MyValue = value
        
    def MyName(self):
        return self._MyName
    
    def MyValue(self):
        return self._MyValue