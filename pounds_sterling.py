#!/usr/bin/env python
"""
RONALD INSELBERG
pounds_sterling.py

Implements the United Kingdom's pounds sterling (GBR)
"""

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from HomeWork03Number02 import MakeMoneyString

from usd import Money, Usd


class Gbr(Money):

    def __init__(self, amount):
        Money.__init__(self, amount)
        self.__normalize()

    def __normalize(self):
        # unitize to 0.01 GBR (value of smallest coin--1 pence)
        self.amount = round(100 * self.amount) / 100

    def __str__(self):
        x = MakeMoneyString(self.amount)
        if x[0] == '-':
            return '-GBR' + x[2:]     # use 'GBR' instead of '$'
        else:
            return 'GBR' + x[1:]

    def __add__(self, other):
        if isinstance(other, Gbr):
            return Gbr(self.amount + other.amount)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Gbr):
            return Gbr(self.amount - other.amount)
        else:
            raise TypeError

    def __cmp__(self, other):
        if isinstance(other, Gbr):
            return cmp(self.amount, other.amount)
        else:
            raise TypeError

    def __eq__(self, other):
        if abs(self.__cmp__(other)) < 0.01:
            return True
        return False

    def __div__(self, number):
        return Gbr(self.amount / number)

    def __mul__(self,  number):
        return Gbr(self.amount * number)

    def __rmul__(self, number):
        return Gbr(self.amount * number)

    def __neg__(self):
        return Gbr(-self.amount)

    def __repr__(self):
        return """Gbr(%f)""" % self.amount

    def MakeChange(self, pence):
        money = ()
        pence = abs(pence)
        for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
            num = pence//coin
            if num > 0:
                money += str(coin) + ' * ' + str(num),
            pence -= coin * num
        assert pence == 0
        return money

    def MakeBills(self, pounds):
        money = ()
        pounds = abs(pounds)
        for bill in [50, 20, 10, 5]:
            num = pounds//bill
            if num > 0:
                money += str(bill) + ' * ' + str(num),
            pounds -= bill * num
        assert pounds == 0
        return money

    def MakeCurrency(self):
        pounds = int(self.amount / 5) * 5
        pence= int((self.amount - pounds) * 100)
        return self.MakeBills(pounds), self.MakeChange(pence)



def Gbr_to_Usd(x):
    if isinstance(x, Gbr):
        file_object = open('currency_exchange_rates.py')
        exec file_object
        file_object.close()
        return Usd(x.amount * GBR_to_USD)
    else:
        raise TypeError

def Usd_to_Gbr(x):
    if isinstance(x, Usd):
        file_object = open('currency_exchange_rates.py')
        exec file_object
        file_object.close()
        return Gbr(x.amount * USD_to_GBR)
    else:
        raise TypeError

