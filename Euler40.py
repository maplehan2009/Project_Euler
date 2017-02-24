# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:35:11 2017

@author: Jingtao
"""

def tail(l):
    x = 0
    for i in range(l):
        x = x * 10 + 8
    x = x + 1 + (l-1) * 10 ** l
    return x
    
def func(n):
    length = 0
    m = n
    while(m > 0):
        m /= 10
        length += 1
    if length == 1:
        return n
    else:
        ll = length - 1
        
    if tail(ll) == n:
        return 9
    elif n > tail(ll):
        last_no = tail(ll)
        k = ll + 1
    else: 
        ll -= 1
        while(tail(ll) > n):
            ll -= 1
        k = ll + 1
        last_no = tail(ll)

    if (n - last_no) % k == 0:
        main_part = (n - last_no) / k  + 10 ** (k - 1) - 1
        return main_part % 10
    else:
        main_part = (n - last_no) / k  + 10 ** (k - 1)      
        remain = (n - last_no) % k
        return (main_part / 10 ** (k - remain)) % 10
    
if __name__=='__main__':
#    N = int(raw_input())
#    for i in range(N):
#        id_list = raw_input().split()
#        ans = 1
#        for j in id_list:
#            ans *= func(int(j))
#        print ans
    func(189)
