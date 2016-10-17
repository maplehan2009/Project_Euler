# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:34:32 2016

@author: Jingtao
"""

import sys

def gauss(n):
    return (1+n) * n / 2    
    
def my_func(N):
    n3 = (N-1) / 3
    n5 = (N-1) / 5
    n15 = (N-1) / 15
    return gauss(n3) * 3 + gauss(n5) * 5 - gauss(n15) * 15
    
if __name__=='__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print my_func(n)