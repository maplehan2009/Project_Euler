#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 23:09:43 2016

@author: jingtao
"""
import sys

def change2b(x, b):
    '''x is a 10 based number, b is a new base. Change x based on b'''
    x_new = ''
    while(x > 0):
        res = str(x % b)
        x_new = res + x_new
        x /= b
    return x_new

def d_number(x, d):
    '''x is a string based on b. d is the number that we search for. Return the number of d in the string x'''
    return x.count(d)

def b2ten(x, b):
    length = len(x)
    s = 0
    if length > 0:
        for i in range(length):
            s += int(x[i]) * b ** (length - 1 - i)
    return s

def f(n, d, b):
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

def find_root(d, b):
    N = 100
    root = []
    for n in range(N+1):
        if f(n, d, b) == n:
            root = root + [n]
    return root
    
def find_root_quick(d, b):
    N = b ** (b ** 2) - 1
    root = []
    f = 0
    n = 1
    while(n <= N):
        f += d_number(change2b(n, b), str(d))
        if f == n:
            root = root + [n]
        n += 1
        
    return root

def find_root_superquick(d, b):
    N = b ** (b ** 2)
    f_node = [x * b ** (x-1) for x in range(1, b ** 2 + 1)]
    n_node = [b ** x - 1 for x in range(1, b ** 2 + 1)]
    root = []
    f = 0
    n = 1
    node = 0
    count = 0
    while(n <= N and node < b ** 2):
        count += 1
        f += d_number(change2b(n, b), str(d))
        if f == n:
            root = root + [n]
        if n < f_node[node] and n < n_node[node]:
            n += 1
        else:
            n = n_node[node] + 1
            f = f_node[node]
            node += 1
    print 'count is ' + str(count)
    return root

def s(d, b):
    root = find_root_superquick(d, b)
    return sum(root)

def read_input():
    file = open('input', 'rb')
    b, _ = file.readline().split(' ')
    b = int(b)
    d = file.readline().split(' ')
    d_int = [int(x) for x in d]
    return d_int, b

def read_input_web():
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