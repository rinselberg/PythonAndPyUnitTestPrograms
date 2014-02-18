#!/usr/bin/env python
"""
RONALD INSELBERG
money_test.py

Homework Assignment #7

Implements USD (U.S. dollars), SAR (Saudi riyals) and GBR (U.K. pounds sterling).

Testing is very sketchy at this point.

The currency exchange rates are coded as Python assignment statements in a separate file
"currency_exchange_rates.py" that is executed (via an 'exec' command) every time
that one of the currency conversion methods is called.

Obviously this wouldn't be very fast if the program were doing a very large number of
currency conversions. I did it this way because it provides an easy way to update the
currency exchange rates without changing any of the (other) Python code, and because it
gave me a chance to use the 'exec' command.

So in theory, every currency conversion uses the most up-to-date exchange rates, which could
even be changed in the middle of a program run, by someone independently updating the file
"currency_exchange_rates.py".

Of course I would implement it differently if there were a requirement for a very large number
of currency conversions.

You will see some duplicate code, but I thought that was a good tradeoff, vs. making the
code more complicated. The code that updates the currency exchange rates, for example.
"""

from usd import Money, Usd
from saudi_riyals import Sar, Sar_to_Usd, Usd_to_Sar
from pounds_sterling import Gbr, Gbr_to_Usd, Usd_to_Gbr

print Usd_to_Gbr(Usd(1.0))
print Gbr_to_Usd(Gbr(1.0))
z = Gbr(-24.37)
print z.MakeCurrency()

print Usd_to_Sar(Usd(1.0))
print Sar_to_Usd(Sar(1.0))
x = Sar(-12.04)
y = Sar(0.89)
print x.MakeCurrency()
print y.MakeCurrency()
print x, y
print x + y

print x == y
print x <> y
print x < y, x <= y
print y > x, y >= x

f = Usd(99.41)
print f.MakeCurrency()
print f == f

a, b, c = Sar(36.71), Usd(36.71), Usd(36.71)
print b == c
print a == b

"""Copy and paste of program tests
steven-inselbergs-computer:HW07 Steve$ python money_test.py
GBR0.64
$1.57
(('20 * 1',), ('200 * 2', '20 * 1', '10 * 1', '5 * 1', '2 * 1'))
SAR3.75
$0.27
(('10 * 1', '1 * 2'), ('5 * 1',))
((), ('50 * 1', '25 * 1', '10 * 1', '5 * 1'))
-SAR12.05 SAR0.90
-SAR11.15
False
True
True True
True True
(('50 * 1', '20 * 2', '5 * 1', '1 * 4'), ('25 * 1', '10 * 1', '5 * 1', '1 * 1'))
True
True
Traceback (most recent call last):
  File "money_test.py", line 40, in <module>
    print a == b
  File "/Users/Steve/PythonClass/HW07/saudi_riyals.py", line 47, in __eq__
    if abs(SaudiRiyals.__cmp__(self, other)) < 0.01:
  File "/Users/Steve/PythonClass/HW07/saudi_riyals.py", line 44, in __cmp__
    raise TypeError
TypeError
steven-inselbergs-computer:HW07 Steve$ 
"""
