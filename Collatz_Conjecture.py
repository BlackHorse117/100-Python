#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:33:03 2019

@author: charles
"""

def collatz_conjecture(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(num * 3 + 1)    
    else: 
        print(num)
        print('Done!')

collatz_conjecture(100)
