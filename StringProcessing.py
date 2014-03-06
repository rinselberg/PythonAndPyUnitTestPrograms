#!/usr/bin/env python
"""
RONALD INSELBERG
hw10_1.py
"""

def Palindrome(word):
    """
    If the string passed via 'word' is a palindrome (and is at least three characters long)
    return the processed string; otherwise return None. All whitespace and punctuations are
    removed. Numbers are treated like letters. Letters are converted to lower case.
    """
    list_of_chars = [char for char in word.lower() if char.isalnum()]
    #print list_of_chars
    if len(list_of_chars) >= 3 and list_of_chars == list_of_chars[::-1]:
        return ''.join(list_of_chars)
    else:
        return None

def main():
    DATA = ('Murder for a jar of red rum', 12321, 'nope', 'abcbA', 3443, 'what', 'Never odd or even', 'Rats live on no evil star')
    for word in DATA:
        print word
        print Palindrome(str(word))
        print
    
if __name__ == '__main__':
    main()


"""Copy and paste of program tests
steven-inselbergs-computer:utils Steve$ python hw10_1.py
Murder for a jar of red rum
murderforajarofredrum

12321
12321

nope
None

abcbA
abcba

3443
3443

what
None

Never odd or even
neveroddoreven

Rats live on no evil star
ratsliveonnoevilstar

steven-inselbergs-computer:utils Steve$
"""

"""
python -i hw10_1.py
>>> import hw10_1
>>> help(Palindrome)
Help on function Palindrome in module __main__:

Palindrome(word)
    If the string passed via 'word' is a palindrome (and is at least three characters long)
    return the processed string; otherwise return None. All whitespace and punctuations are
    removed. Numbers are treated like letters. Letters are converted to lower case.
"""
