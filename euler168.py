# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:47:45 2016

@author: Jingtao
"""

def check_order(m):
    # check the numbers in the range of [10^m, 10^m+1)
    # return the sum of the rotation numbers in this range
    summ = 0
    for p in range(1, 10):
        for d in range(1, 10):
            if ((10 ** m - p) * d) % (10 * p - 1) == 0:
                n = ((10 ** m - p) * d) / (10 * p - 1)
                if n / (10 ** (m-1)) != 0:
                    summ = (summ + 10 * n + d) % 100000
    return summ

if __name__=='__main__':
    #m = int(raw_input())
    # Find the sum in the range of (10, 10^m)    
    m = 100
    summ = 0
    for order in range(1, m):
        summ = (summ + check_order(order)) % 100000
    print summ