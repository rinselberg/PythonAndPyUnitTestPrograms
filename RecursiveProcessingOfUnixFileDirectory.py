#!/usr/bin/env python
"""
RONALD INSELBERG
hw10_2.py
This program accepts a directory name.
The program uses the os.walk function to walk the given directory recursively
(processing any/all nested directories). For each non-directory file that is encountered,
the program reads the file and scans for words that are palindromes. At the end, a report
is generated, listing each palindrome and the number of files in which it occurs.
"""

import sys
import os
import string

if __name__ == '__main__':
    sys.path.insert(0, "..")
else:
    sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import utils.hw10_1 as utils

def CountWords(text, counts_d=None):
    """Generates the directory that contains each palindrome and the number
    of files in which it ooccurs.
    """
    if counts_d == None:    # None given on call, start with empty                                                                                 
        counts_d = {}       # {}, a mutable default is a pitfall!
    list_of_palindromes_in_current_text = []
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        word = utils.Palindrome(word)
        if not word:
            continue

        elif word in counts_d:
            if word not in list_of_palindromes_in_current_text:
                counts_d[word] += 1
                list_of_palindromes_in_current_text.append(word)
        else:
            counts_d[word] = 1
            list_of_palindromes_in_current_text.append(word)
    return counts_d

def GetText(file_name):
    """Puts the whole file into memory and returns it."""
    try:
        file_obj = open(file_name)
        try:
            text = file_obj.read()
        finally:
            file_obj.close()
    except IOError, info:
        print >> sys.stderr, "Can't read", file_name, ':', info
        sys.exit(1)
    return text

def Process(this_dir, dir_names, file_names, words_count):
    print os.path.abspath(this_dir)
    for file_name in sorted(dir_names + file_names):
        whole_name = os.path.join(this_dir, file_name)
        if os.path.isdir(whole_name):
            print 'directory:', file_name
        else:
            print file_name
            text = GetText(whole_name)
            words_count = CountWords(text, words_count)

def main():
    def ValueKey(i):
        return word_count[i]

    def PrintReport(word_count):
        for word in reversed(sorted(word_count, key=ValueKey)):
            print "%s in %d files" % (word, word_count[word])

    word_count = {}
    directory_name = raw_input('Enter directory name: ')
    for (this_dir, dir_names, file_names) in os.walk(directory_name):
        Process(this_dir, dir_names, file_names, word_count)
    PrintReport(word_count)

if __name__ == '__main__':
    main()

"""Copy and paste of program tests
steven-inselbergs-computer:driver Steve$ python hw10_2.py
Enter directory name: palindromes
/Users/Steve/PythonClass/application/driver/palindromes
empty.txt
one.txt
directory: palindromes
two.txt
/Users/Steve/PythonClass/application/driver/palindromes/palindromes
three.txt
murderforajarofredrum in 3 files
3443 in 2 files
onacloverifaliveeruptsavastpureevilafirevolcano in 2 files
asantaatnasa in 1 files
nzy33yzn in 1 files
123454321 in 1 files
steven-inselbergs-computer:driver Steve$
"""

"""Copy and paste of directory tree
steven-inselbergs-computer:PythonClass Steve$ python lab09_3.py
Tree to start at which directory? application
 /application
 |-- /driver
 |   |-- hw10_2.py
 |   |-- hw10_2.py~
 |   |-- /palindromes
 |  |   |-- empty.txt
 |  |   |-- one.txt
 |  |   |-- /palindromes
 |  |  |   |-- three.txt
 |  |   |-- two.txt
 |-- /utils
 |   |-- __init__.py
 |   |-- __init__.pyc
 |   |-- hw10_1.py
 |   |-- hw10_1.pyc
 |   |-- hw10_1.py~

5 directories, 11 files
steven-inselbergs-computer:PythonClass Steve$ 
"""
