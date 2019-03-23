#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:45:39 2019

@author: kartiktanksali
"""
dict_roman = {"I":1,"V":5,"X":10, "L":50, "C":100, "D":500, "M":1000}

string = input()

sums = 0
i=0
while(i<len(string)):
    if i==len(string)-1:
        sums+=dict_roman[string[i]]
        break;
        
    if dict_roman[string[i]] >= dict_roman[string[i+1]]:
        sums += dict_roman[string[i]]
        i+=1
    else:
        sums += abs(dict_roman[string[i+1]]-dict_roman[string[i]])
        i+=2

print(sums)