#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 03:40:17 2019

@author: kartiktanksali
"""

def isPalindrome(x):
        if x<0:
            return False
        else:
            x = str(x)
            rev = x[::-1]
            if rev == x:
                return True
            else:
                return False


x =int(input("Enter a number: "))
print(isPalindrome(x))