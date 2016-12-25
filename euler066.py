# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 19:34:29 2016

@author: Jingtao
"""

import math

def is_square(x):
    # determine whether a number x is square
    if int(math.sqrt(x)) ** 2 == x:
        return True
    else:
        return False
    
def naive_method(D):
    # a naive method trying all the possible value for x from 1 to infinity
    # It does not work for the case where D = 16 since the minimal x is quite large
    x = 1
    flag = True
    while(flag):
        x += 1
        if (x ** 2 - 1) % D == 0 and is_square((x ** 2 - 1) / D):
            flag = False
    return x

def continued_fraction(N):
    # In the Wiki page Pell's equation. I found a very clever method using
    # the continued fraction of a square root. Magically, the minimal solution x
    # is one of the numerator in the expansion sequence of the square root of D
    a0 = int(math.sqrt(N))
    a1 = a0
    a2 = 1
    a_list = []
    while(True):
        a3 = (N - a1 ** 2) / a2
        div = int((math.sqrt(N) + a1) / a3)
        a1 = a3 * div - a1
        a2 = a3
        a_list.append(div)
        if a1 == int(math.sqrt(N)) and a2 == 1:
            break
    return a0, a_list 

def solve_pell_equation(D):
    a0, a = continued_fraction(D)
    h0 = 1
    h1 = a0
    k0 = 0
    k1 = 1
    h2 = a0
    k2 = 1
    n = 0
    while (h2 ** 2 - D * k2 ** 2 != 1):
        an = a[n]
        h2 = an * h1 + h0
        k2 = an * k1 + k0
        h0 = h1
        k0 = k1
        h1 = h2
        k1 = k2
        n = (n + 1) % len(a)
    return h2

if __name__=='__main__':
    N = int(raw_input())
    #N = 7
    max_x = 0
    max_D = 0
    for i in range(2, N+1):
        if is_square(i):
            continue
        else:
            xi = solve_pell_equation(i)
            if  xi > max_x:
                max_D = i
                max_x = xi
            
    print max_D
