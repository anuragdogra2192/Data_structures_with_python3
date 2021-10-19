"""
String to integer

The function used in the following code:


1) reduce() in Python
    The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements 
    mentioned in the sequence passed along.This function is defined in “functools” module.
    Working : 
    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and 
    the number just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.

    More detailed description: ref: https://docs.python.org/3/library/functools.html#functools.reduce

    functools.reduce(function, iterable[, initializer])
    Apply function of two arguments cumulatively to the items of iterable, from left to right, 
    so as to reduce the iterable to a single value. 
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
    The left argument, x, is the accumulated value and the right argument, 
    y, is the update value from the iterable. 
    If the optional initializer is present, 
    it is placed before the items of the iterable in the calculation, 
    and serves as a default when the iterable is empty. 
    If initializer is not given and iterable contains only one item, the first item is returned.

    Roughly equivalent to:

    def reduce(function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            value = next(it)
         else:
            value = initializer
        for element in it:
            value = function(value, element)
        return value

2) string.digit()
    In Python3, string.digits is a pre-initialized string used as string constant. 
    In Python, string.digits will give the lowercase letters ‘0123456789’.

    Syntax : string.digits

    Parameters : Doesn’t take any parameter, since it’s not a function.

    Returns : Return all digit letters.
"""

import functools, string

def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
    s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

s = input("Enter the number as string: ")

i = string_to_int(s)
print("The converted number to integer: ", i ,"and its type", type(i))