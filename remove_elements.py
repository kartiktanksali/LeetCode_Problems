#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:29:31 2019

@author: kartiktanksali
"""

#Remove Elements LeetCode

lst = [1,2,3,4,4,5]

val = int(input())

while val in lst:
    lst.pop(lst.index(val))
        
    
print(len(lst))
    
    