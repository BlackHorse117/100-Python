#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:16:27 2019

@author: charles
"""


def bubblesort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

mylist = [8,9,5,1,3,7,10]
bubblesort(mylist)

