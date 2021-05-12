# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:58:32 2020

@author: srd
"""
def int2roman(num_in):
    ints = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
    nums = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
    
    out = ''

    
    return out


def test(num_in, expected):
    actual = int2roman(num_in)
    print(f"{num_in:24} Expected: {expected:3} Actual: {actual:3} {'OK' if expected == actual else 'ERROR'}")
    
    
test(19, 'XIX')
