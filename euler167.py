# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 23:20:34 2016

@author: Jingtao
"""

def in_pattern(pattern_record, x):
    # Check if x is in the array of pattern_record
    for y in pattern_record:
        if x == y:
            return True
        elif y > x:
            return False
    return False

def add_pattern(pattern_record, x):
    # add new element x at the end of the array
    # then delete the first element of the array
    # In fact I should write a queue class but I am quite lazy...
    pattern_new = []
    n = len(pattern_record)
    for i in range(n-1):
        pattern_new.append(pattern_record[i+1])
    pattern_new.append(x)
    return pattern_new

def get_period_difference(u, v):
    # Calculate the period of the sequence
    u1 = u
    u2 = 2 * v + 2

    pattern_length = v + 1
    pattern_record = range(v, 3*v+1, 2)
    
    k_pattern = 0
    period = 0
    current = pattern_record[-1] + 2
    
    while(k_pattern != pattern_length):
        if in_pattern(pattern_record, current - u1) ^ in_pattern(pattern_record, current - u2):
            k_pattern += 1
            period += 1
            pattern_record = add_pattern(pattern_record, current)
        else:
            k_pattern = 0
        current += 2   
    
    difference = current - 2 - 3*v
    
    return period, difference   

def get_local_dif(u, v, n):
    # Calculate the difference between the n-th element and the first element
    # In this case we do not count the two even terms
    u1 = u
    u2 = 2 * v + 2
    
    if n <= v+1:
        return 2 * (n - 1)
    
    pattern_record = range(v, 3*v+1, 2)
    count = v+1
    current = pattern_record[-1] + 2    

    while(count < n):
        if in_pattern(pattern_record, current - u1) ^ in_pattern(pattern_record, current - u2):
            count += 1
            pattern_record = add_pattern(pattern_record, current)
        current += 2   
    return current - 2 - v
    
if __name__=='__main__':
    # read n, k from input file
    n, k = raw_input().strip().split(' ')
    n, k = [int(n),int(k)]
    
    # u is the first element of the Ulam sequence, v is the second
    # In this problem u = 2 and v = 2n+1
    u = 2
    v = 2 * n + 1

    # Very important conjecture : if u=2 and v is odd and v >= 5, then this 
    # sequence has exactly two even terms. The first even term is 2 at the position 1
    # the second even term is 2v+2 at the position (v+7)/2
    # Hence, the other odd number must be the sum of some odd number and one of the
    # two even numbers.

    even_position = (v + 7) / 2
    if k == 1:
        print 2
    elif k == even_position:
        print 2 * v + 2
    elif k < even_position:
        print v + 2 * (k - 2)
    elif k > even_position and k <= v+3:
        print v + 2 * (k - 3)
    else:
        Period, Dif = get_period_difference(u, v)
        N = (k - 2) / Period
        n = (k - 2) % Period
        
        if n == 0:
            N -= 1
            n = Period

        local_dif = get_local_dif(u, v, n)
        answer = v + N * Dif + local_dif
        print answer
