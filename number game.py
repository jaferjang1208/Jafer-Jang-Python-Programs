#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:01:23 2020

@author: jafer
"""
play=input("do you want to play a game? Yes or No?")
number=0
while play=="yes"or play=="y":
    number=int(input("enter a number"))
    while number!=3:
        number=int(input("try another number"))
    else:
        print("congrats")
        break
else:
    print("input a valid code")
    

    

        