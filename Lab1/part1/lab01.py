#!/usr/bin/env python3
#-*- coding: utf-8 -*-
def falling(n, k):


    """Рассчитать убывающий факториал от n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    fact = 1
    while (k != 0):
        fact = fact * n
        n = n - 1
        k = k - 1
    return fact


def sum_digits(y):

    """Сложить все цифры числа y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """
    k = 0
    while y > 0:
        k += y % 10
        y = y // 10
    return k



def double_eights(n):


    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    k = 0
    while (n > 0):
        if (n % 10 == 8):
            n = n // 10
            k += 1
            if (k == 2):
                break
        else:
            k = 0
            n = n // 10
    if (k == 2):
        return True
    else:
        return False
