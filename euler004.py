# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 22:19:05 2017

@author: Jingtao
"""

def is_palim(n):
    n_rev = 0
    m = n
    while(m > 0):
        res = m % 10
        n_rev = 10*n_rev + res
        m /= 10
    if n_rev == n:
        return True
    else:
        return False
    
def is_facto(n):
    for i in range(999, 99, -1):
        if n % i == 0 and n / i < 1000:
            print i, n/i
            return True
        elif n / i > 999:
            return False
        else:
            continue
    return False

def find_max_palim(N):
    i = N-1
    while(i > 10000):
        if is_palim(i) and is_facto(i):
            break
        i -= 1
    return i
    
if __name__=='__main__':
    N = 1000000
    print find_max_palim(N)