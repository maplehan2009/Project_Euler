# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:24:54 2016

@author: Jingtao
"""

import math

def is_square(x):
    # determine whether a number x is square
    if int(math.sqrt(x)) ** 2 == x:
        return True
    else:
        return False
        
def find_period(N):
    # find the pattern of the root of N
    # Here, we do research on the pattern (sqrt(N) - a1) / a2
    # When a1, a2 repeat, then we know there is a period.
    period = 0
    a1 = int(math.sqrt(N))
    a2 = 1
    while(True):
        a3 = (N - a1 ** 2) / a2
        div = int((math.sqrt(N) + a1) / a3)
        a1 = a3 * div - a1
        a2 = a3
        period += 1
        if a1 == int(math.sqrt(N)) and a2 == 1:
            break
    return period

if __name__=='__main__':
    #N = 13
    N = int(raw_input())
    count = 0
    for n in range(2, N+1):
        if is_square(n):
            continue
        else:
            p = find_period(n)
            if p % 2 == 1:
                count += 1
    print count