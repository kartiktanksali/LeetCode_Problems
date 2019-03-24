#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:21:15 2019

@author: kartiktanksali
"""


s = input()

def lengthofLastWord(s):
    if s.isspace():
        return 0
    elif len(s)==1:
        return 1
    else:
        return (len(s.split()[-1]) if s.split()!=[] else 0)


res = lengthofLastWord(s)

print(res)