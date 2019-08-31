# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:37:37 2019

@author: siddh
"""

n=1

while True:
    if 100 * (n ** 2) < 2 ** n:
        print(n)
        break
    n += 1