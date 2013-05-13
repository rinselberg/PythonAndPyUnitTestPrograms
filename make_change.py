#!/usr/bin/env python
"""
RONALD INSELBERG
HomeWork02Number01A.py
"""

def MakeChange(amount):
    money = ()
    for coin in [25, 10, 5, 1]:
        num = amount//coin
        money += (coin,) * num
        amount -= coin * num
    return money

for i in range(100):
    print MakeChange(i)


"""Copy and paste of program tests

"""
