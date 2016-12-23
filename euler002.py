# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:47:24 2016

@author: Jingtao
"""

import sys

if __name__=='__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        T = long(raw_input().strip())
        
        a1 = 1
        a2 = 2
        summ = 0
        
        while(a2 <= T):
            summ += a2
            temp1 = a1 + a2
            temp2 = temp1 + a2
            a2 = temp1 + temp2
            a1 = temp2
        
        print summ