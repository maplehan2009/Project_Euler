# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:04:07 2016

@author: Jingtao
"""
import math

def is_prime(n):
    # Determine whether n is a prime
    if n == 1 or n == 2:
        return True
        
    for i in range(2, int(math.sqrt(n))+2):
        if n % i == 0:
            return False
    return True
    
def largest_prime(N):
    # Find the largest prime factor of N
    target = 0
    for i in range(1, int(math.sqrt(N)) + 2):
        if N % i == 0:
            if is_prime(N / i):
                return N / i
            elif is_prime(i):
                target = i
    return target

if __name__=='__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = long(raw_input().strip())
        print largest_prime(n)