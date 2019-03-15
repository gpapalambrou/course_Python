#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 05:59:25 2019

@author: gpapalambrou
"""

def test(x, y):
    a=x/y
    b=x%y
    return a,b

test(5,2)

c, d = test(5,2)

print(c)
    