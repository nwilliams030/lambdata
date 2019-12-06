"""
Assignment for unit 302

Execute the above code in a Python repl/environment
of your choice (a notebook can work too). Make multiple instances of the class,
inspect them, and try to use them interactively to perform basic mathematics
(arithmetic).

Rewrite the Complex class with a method add that takes a complex number as an
argument and returns the sum of it with the complex number it is being called
from (self).

"""

import math

class Complex(object):

    def __init__(self, a, b):
        '''Creates Complex Number'''
        self.a = a
        self.b = b

    def __str__(self):
        '''Returns complex number as a string'''
        return '(%s, %s)' % (self.a, self.b)

    def __add__(self, rhs):
        '''Adds complex numbers'''
        return Complex(self.a + rhs.a, self.b + rhs.b)

i = Complex(0, 1)
