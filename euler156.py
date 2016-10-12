#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 23:09:43 2016

@author: jingtao
"""

def change2b(x, b):
    '''x is a 10 based number, b is a new base. Change x based on b'''
    x_new = ''
    while(x > 0):
        res = str(x % b)
        x_new = res + x_new
        x /= b
    return x_new

def b2ten(x, b):
    '''x is a number based on b. Change x to the number based on 10'''
    length = len(x)
    s = 0
    if length > 0:
        for i in range(length):
            s += int(x[i]) * b ** (length - 1 - i)
    return s

def f(n, d, b):
    '''Calculate the f(n) value'''
    if n == 0:
        return 0
    
    nb = change2b(n, b)
    count = 0
    head = int(nb[0])
    tail = nb[1:]
    tail10 = b2ten(tail, b)
    l = len(nb)
    while(l > 0):
        count += (n / b ** l) * b ** (l-1)
        if head == d:
            count += (tail10 + 1)
        if head > d:
            count += (b ** (l-1))
 
        l = len(tail)
        if l > 0:
            head = int(tail[0])
            tail = tail[1:]
            tail10 = b2ten(tail, b)
    return count
    
def binary_search(left, right, d, b):
    '''The binary search method to find all the roots in a certain range'''
    s = 0
    if right - left == 0:
        if f(left, d, b) == left:
            return left
        else:
            return 0
            
    if right - left == 1:
        if f(left, d, b) == left:
            s += left
        if f(right, d, b) == right:
            s += right
        return s
        
    if right - left == 2:
        if f(left, d, b) == left:
            s += left
        if f(left + 1, d, b) == left+1:
            s += (left+1)
        if f(right, d, b) == right:
            s += right
        return s       
  

    middle = (left + right) / 2
    if (f(right, d, b) >= middle+1) and (f(middle+1, d, b) <= right):
        s += binary_search(middle+1, right, d, b)
    if (f(middle, d, b) >= left) and (f(left, d, b) <= middle):
        s += binary_search(left, middle, d, b)
    
    return s

def read_input():
    '''read a local test file'''
    file = open('input', 'rb')
    b, _ = file.readline().split(' ')
    b = int(b)
    d = file.readline().split(' ')
    d_int = [int(x) for x in d]
    return d_int, b

def read_input_web():
    '''read the on-line test file provided by Hackranker'''
    b,M = raw_input().strip().split(' ')
    b,M = [int(b),int(M)]
    arr = map(int,raw_input().strip().split(' '))
    return arr, b
    
if __name__=='__main__':
    d_list, b = read_input()
    ans = 0
    left = 1
    right = b ** (b + 1)
    for d in d_list:
        ans += binary_search(left, right, d, b)
    print ans
