#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:55:12 2020

@author: jafer
"""
words="""art
hue
ink
"""
tiles="asrtink"
start=0
end=0
space=()
foundwords=()
for i in words:
    if i=="\n":
        space=space+(words[start:end], )
        start=end+1
        end=end+1
    else:
        end=end+1
for word in space:
    tiles_left=tiles
    for letter in word:
        if letter not in tiles_left:
            break
        else:
            index=tiles_left.find(letter)
            tiles_left=tiles_left[:index]+tiles_left[index+1:]
    if len(word)==len(tiles)-len(tiles_left):
        foundwords=foundwords+(word, )
print(foundwords)