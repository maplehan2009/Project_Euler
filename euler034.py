# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 14:55:25 2017

@author: Jingtao
"""

def check_n(n, my_facto):
    m = n
    my_sum = 0
    while(m > 0):
        res = m % 10
        m /= 10
        my_sum += my_facto[res]
    if my_sum % n == 0:
        return True
    else:
        return False
        

if __name__=='__main__':
    my_facto = {0:1}
    for i in range(1, 10):
        my_facto[i] = my_facto[i-1] * i
     
    N = 20 
    ans = 0
    for i in range(10, N+1):
        if check_n(i, my_facto):
            ans += i
    print ans
    