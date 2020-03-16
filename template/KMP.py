# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:14:18 2019

@author: WuliVe
"""

import numpy as np

#  python to vist the string data :   var1[0]: ", var1[0]

def normal_solving(ts, ps):
    i = 0
    j = 0
    
    while (i <= len(ts)-1 and j <= len(ps)-1):
        if ts[i] == ps[j]:
            i += 1
            j += 1
        else:  # i should return and for next match
            i = i-j+1
            j = 0
  
    if j == len(ps):  #means end the match, we get it
        return i-j  # the position of the start of matching
    else: return -1  #fails to match



def get_next(ps):
      
    next_a = np.zeros(len(ps), dtype = "int_")
    next_a[0] = -1
    j = 0
    k = -1
    
    while (j < len(ps)-1):
        if j == -1 or ps[j] == ps[k]:
            j += 1
            k += 1
            if ps[j] == ps[k]:
                next_a[j] = next_a[k]
            else:  next_a[j] = k
        else: k = next_a[k]
    
    return next_a


def KMP_solving(ts, ps):
    i = 0
    j = 0
    next_a= get_next(ps)
    while (i <= len(ts)-1 and j <= len(ps)-1):
        if ts[i] == ps[j] or j == -1: #when j = -1 we should move i and j should be 0
            i += 1
            j += 1
        else:  # i should return and for next match
            # i = i-j+1 i should not be return
            j = next_a[j]
  
    if j == len(ps):  #means end the match, we get it
        return i-j  # the position of the start of matching
    else: return -1  #fails to match
    
    return



""" test main """
ts = "abcdedebdscabd"   #main string  
ps = "abd"   #pattern string
next_a = get_next(ps)
result = normal_solving(ts, ps)
result2 = KMP_solving(ts, ps)