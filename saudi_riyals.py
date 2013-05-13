#!/usr/bin/env python
"""
RONALD INSELBERG
saudi_riyals.py

Implements Saudi riyals.
"""

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from HomeWork03Number02 import MakeMoneyString

from usd import Money, Usd


class Sar(Money):

    def __init__(self, amount):
        Money.__init__(self, amount)
        self.__normalize()

    def __normalize(self):
        # unitize to 0.05 Riyals (value of smallest coin--the 5 halalas piece)
        self.amount = round(20 * self.amount) / 20

    def __str__(self):
        x = MakeMoneyString(self.amount)
        if x[0] == '-':
            return '-SAR' + x[2:]     # use 'SAR' instead of '$'
        else:
            return 'SAR' + x[1:]

    def __add__(self, other):
        if isinstance(other, Sar):
            return Sar(self.amount + other.amount)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Sar):
            return Sar(self.amount - other.amount)
        else:
            raise TypeError

    def __cmp__(self, other):
        if isinstance(other, Sar):
            return cmp(self.amount, other.amount)
        else:
            raise TypeError

    def __eq__(self, other):
        if abs(self.__cmp__(other)) < 0.01:
            return True
        return False

    def __div__(self, number):
        return Sar(self.amount / number)

    def __mul__(self,  number):
        return Sar(self.amount * number)

    def __rmul__(self, number):
        return Sar(self.amount * number)

    def __neg__(self):
        return Sar(-self.amount)

    def __repr__(self):
        return """Sar(%f)""" % self.amount

    def MakeChange(self, halalas):
        money = ()
        halalas = abs(halalas)
        for coin in [50, 25, 10, 5]:
            num = halalas//coin
            if num > 0:
                money += str(coin) + ' * ' + str(num),
            halalas -= coin * num
        assert halalas == 0
        return money

    def MakeBills(self, riyals):
        money = ()
        riyals = abs(riyals)
        for bill in [500, 200, 100, 50, 20, 10, 5, 1]:
            num = riyals//bill
            if num > 0:
                money += str(bill) + ' * ' + str(num),
            riyals -= bill * num
        assert riyals == 0
        return money

    def MakeCurrency(self):
        riyals =int(self.amount)
        halalas = int(round((self.amount - float(riyals)) * 100))
        return self.MakeBills(riyals), self.MakeChange( halalas)



def Sar_to_Usd(x):
    if isinstance(x, Sar):
        file_object = open('currency_exchange_rates.py')
        exec file_object
        file_object.close()
        return Usd(x.amount * SAR_to_USD)
    else:
        raise TypeError

def Usd_to_Sar(x):
    if isinstance(x, Usd):
        file_object = open('currency_exchange_rates.py')
        exec file_object
        file_object.close()
        return Sar(x.amount * USD_to_SAR)
    else:
        raise TypeError

