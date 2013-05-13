
#!/usr/bin/env python
"""
RONALD INSELBERG
hw07.py

Implements USD (U.S. dollars) and Saudi riyals.
Testing is very sketchy at this point.

"""

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import HomeWork03Number02 as make_money_string


SAR_to_USD = 0.2665             # currency exchange rate
USD_to_SAR = 1 / SAR_to_USD     # reverse exchange rate


class Money(float):

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
        return make_money_string.MakeMoneyString(self.amount)

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
        if abs(Usd.__cmp__(self, other)) < 0.01:
            return True
        return False

    def MakeChange(self, cents):
        money = ()
        cents = abs(cents)
        for coin in [25, 10, 5, 1]:
            num = cents//coin
            money += (coin,) * num
            cents -= coin * num
        assert cents == 0
        return money

    def MakeBills(self, dollars):
        money = ()
        dollars = abs(dollars)
        for bill in [100, 50, 20, 10, 5, 1]:
            num = dollars//bill
            money += (bill,) * num
            dollars -= bill * num
        return money

    def MakeCurrency(self):
        dollars = int(self.amount)
        cents = int(round((self.amount - float(dollars)) * 100))
        return Usd.MakeBills(self, dollars), Usd.MakeChange(self, cents)


class SaudiRiyals(Money):

    def __init__(self, amount):
        Money.__init__(self, amount)
        self.__normalize()

    def __normalize(self):
        # unitize to 0.05 Riyals (value of smallest coin--the 5 halalas piece)
        self.amount = round(20 * self.amount) / 20

    def __str__(self):
        x = make_money_string.MakeMoneyString(self.amount)
        if x[0] == '-':
            return '-SAR' + x[2:]     # use 'SAR' instead of '$'
        else:
            return 'SAR' + x[1:]

    def __add__(self, other):
        if isinstance(other, SaudiRiyals):
            return SaudiRiyals(self.amount + other.amount)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, SaudiRiyals):
            return SaudiRiyals(self.amount - other.amount)
        else:
            raise TypeError

    def __cmp__(self, other):
        if isinstance(other, SaudiRiyals):
            return cmp(self.amount, other.amount)
        else:
            raise TypeError

    def __eq__(self, other):
        if abs(SaudiRiyals.__cmp__(self, other)) < 0.01:
            return True
        return False

    def MakeChange(self, halalas):
        money = ()
        halalas = abs(halalas)
        for coin in [50, 25, 10, 5]:
            num = halalas//coin
            money += (coin,) * num
            halalas -= coin * num
        assert halalas == 0
        return money

    def MakeBills(self, riyals):
        money = ()
        riyals = abs(riyals)
        for bill in [500, 200, 100, 50, 20, 10, 5, 1]:
            num = riyals//bill
            money += (bill,) * num
            riyals -= bill * num
        return money

    def MakeCurrency(self):
        riyals =int(self.amount)
        halalas = int(round((self.amount - float(riyals)) * 100))
        return SaudiRiyals.MakeBills(self, riyals), SaudiRiyals.MakeChange(self, halalas)



def SaudiRiyals_to_Usd(x):
    if isinstance(x, SaudiRiyals):
        return Usd(x.amount * SAR_to_USD)
    else:
        raise TypeError

def Usd_to_SaudiRiyals(x):
    if isinstance(x, Usd):
        return SaudiRiyals(x.amount * USD_to_SAR)
    else:
        raise TypeError


print Usd_to_SaudiRiyals(Usd(1.0))
print SaudiRiyals_to_Usd(SaudiRiyals(1.0))
x = SaudiRiyals(-12.04)
y = SaudiRiyals(0.89)
print x.MakeCurrency()
print y.MakeCurrency()
print x, y
print x + y

print x == y
print x <> y
print x < y, x <= y
print y > x, y >= x

a, b, c = SaudiRiyals(36.71), Usd(36.71), Usd(36.71)
print b == c
print a == b


"""Copy and paste of program tests
steven-inselbergs-computer:HW07 Steve$ python hw07.py
SAR3.75
$0.27
((10, 1, 1), (5,))
((), (50, 25, 10, 5))
-SAR12.05 SAR0.90
-SAR11.15
False
True
True True
True True
True
Traceback (most recent call last):
  File "money.py", line 181, in <module>
    print a == b
  File "money.py", line 122, in __eq__
    if abs(SaudiRiyals.__cmp__(self, other)) < 0.01:
  File "money.py", line 119, in __cmp__
    raise TypeError
TypeError
steven-inselbergs-computer:HW07 Steve$
"""
