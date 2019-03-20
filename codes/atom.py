#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:30:29 2019

@author: gpapalambrou
"""

class AtomClass:
    def __init__(self, Velocity, Element = 'C', Mass = 12.0):
        self.Velocity = Velocity
        self.Element = Element
        self.Mass = Mass

    def Momentum(self):
        return self.Velocity * self.Mass