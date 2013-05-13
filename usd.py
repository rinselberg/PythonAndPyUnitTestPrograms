#!/usr/bin/env python
"""
RONALD INSELBERG
usd.py

Implements USD (U.S. dollars).
"""

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from HomeWork03Number02 import MakeMoneyString


class Money(object):

    def __init__(self, amount):
        self.amount = amount


class Usd(Money):

    def __init__(self, amount):
        Money.__init__(self, amount)
        self.__normalize()

    def __normalize(self):
        # unitize to 0.01 USD (value of smallest coin--a penny)
        self.amount = round(100 * self.amount) / 100

    def __str__(self):
        return MakeMoneyString(self.amount)

    def __add__(self, other):
        if isinstance(other, Usd):
            return Usd(self.amount + other.amount)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Usd):
            return Usd(self.amount - other.amount)
        else:
            raise TypeError

    def __cmp__(self, other):
        if isinstance(other, Usd):
            return cmp(self.amount, other.amount)
        else:
            raise TypeError

    def __eq__(self, other):
        if abs(self.__cmp__(other)) < 0.01:
            return True
        return False

    def __div__(self, number):
        return Usd(self.amount / number)

    def __mul__(self,  number):
        return Usd(self.amount * number)

    def __rmul__(self, number):
        return Usd(self.amount * number)

    def __neg__(self):
        return Usd(-self.amount)

    def __repr__(self):
        return """Usd(%f)""" % self.amount

    def MakeChange(self, cents):
        money = ()
        cents = abs(cents)
        for coin in [25, 10, 5, 1]:
            num = cents//coin
            if num > 0:
                money += str(coin) + ' * ' + str(num),
            cents -= coin * num
        assert cents == 0
        return money

    def MakeBills(self, dollars):
        money = ()
        dollars = abs(dollars)
        for bill in [100, 50, 20, 10, 5, 1]:
            num = dollars//bill
            if num > 0: 
                money += str(bill) + ' * ' + str(num),
            dollars -= bill * num
        assert dollars == 0
        return money

    def MakeCurrency(self):
        dollars = int(self.amount)
        cents = int(round((self.amount - float(dollars)) * 100))
        return self.MakeBills(dollars), self.MakeChange(cents)
