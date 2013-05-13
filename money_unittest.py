#!/usr/bin/env python
"""
RONALD INSELBERG
money_unittest.py

Homework Assignment #8

Unit test of  USD (U.S. dollars), SAR (Saudi riyals) and GBR (U.K. pounds sterling).
"""
import unittest
import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

from usd import Money, Usd
from saudi_riyals import Sar, Sar_to_Usd, Usd_to_Sar
from pounds_sterling import Gbr, Gbr_to_Usd, Usd_to_Gbr

class TestMoney(unittest.TestCase):

    def testFormat(self):
        self.assertEqual(str(Usd(-123.21)), '-$123.21')
        self.assertEqual(str(Sar(-123.22)), '-SAR123.20')   # rounding down to nearest 0.05 Riyals
        self.assertEqual(str(Sar(-123.23)), '-SAR123.25')   # rounding up to nearest 0.05 Riyals
        self.assertEqual(str(Gbr(-123.21)), '-GBR123.21')
        self.assertEqual(str(Usd(123456789.999)), '$123,456,790.00')
        self.assertEqual(str(Sar(123456789.999)), 'SAR123,456,790.00')
        self.assertEqual(str(Gbr(123456789.999)), 'GBR123,456,790.00')

    def testAdd(self):
        self.assertEqual(Usd(10.37) + Usd(20.94), Usd(10.37 + 20.94))
        self.assertEqual(Sar(10.37) + Sar(20.94), Sar(10.35 + 20.95))   # rounding to nearest 0.05 Riyals
        self.assertEqual(Gbr(10.37) + Gbr(20.94), Gbr(10.37 + 20.94))
    
    def testSub(self):
        self.assertEqual(Usd(10.37) - Usd(20.94), Usd(10.37 - 20.94))
        self.assertEqual(Sar(10.37) - Sar(20.94), Sar(10.35 - 20.95))   # rounding to nearest 0.05 Riyals
        self.assertEqual(Gbr(10.37) - Gbr(20.94), Gbr(10.37 - 20.94))
        
    def testRepr(self):
        self.assertEqual(eval(repr(Usd(-34981.07))), Usd(-34981.07))
        self.assertEqual(eval(repr(Sar(-34981.07))), Sar(-34981.07))
        self.assertEqual(eval(repr(Gbr(-34981.07))), Gbr(-34981.07))

    def testNeg(self):
        self.assertEqual(-Usd(1003379.94), Usd(-1003379.94))
        self.assertEqual(-Sar(1003379.94), Sar(-1003379.94))
        self.assertEqual(-Gbr(1003379.94), Gbr(-1003379.94))

    def testMult(self):
        self.assertEqual(10.91 * Usd(-44.37), Usd(10.91 * -44.37))
        self.assertEqual(10.91 * Sar(-44.37), Sar(10.91 * -44.35))   # rounding to nearest 0.05 Riyals
        self.assertEqual(10.91 * Gbr(-44.37), Gbr(10.91 * -44.37))

    def testRMult(self):
        self.assertEqual(Usd(-44.37) * 10.91, Usd(10.91 * -44.37))
        self.assertEqual(Sar(-44.37) * 10.91, Sar(10.91 * -44.35))   # rounding to nearest 0.05 Riyals
        self.assertEqual(Gbr(-44.37) * 10.91, Gbr(10.91 * -44.37))

    def testDiv(self):
        self.assertEqual(Usd(3245736.04) / -217.06, Usd(3245736.04 / -217.06))
        self.assertEqual(Sar(3245736.04) / -217.06, Sar(3245736.05 / -217.06))   # rounding to nearest 0.05 Riyals
        self.assertEqual(Gbr(3245736.04) / -217.06, Gbr(3245736.04 / -217.06))

    def testConversions(self):
        self.assertEqual(Gbr_to_Usd(Usd_to_Gbr(Usd(1.0))), Usd(1.0))
        self.assertEqual(Sar_to_Usd(Usd_to_Sar(Usd(1.0))), Usd(1.0))

if __name__ == '__main__':
    unittest.main()

"""Copy and paste of output
steven-inselbergs-computer:unittest Steve$ python money_unittest.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK
steven-inselbergs-computer:unittest Steve$ 
"""
