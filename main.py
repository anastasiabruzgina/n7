# -*- coding: utf-8 -*-
def merge(*arrs):
    arr_sum = []
    for i in arrs:
        arr_sum += i
    
    if len(arr_sum) < 2:
        return arr_sum
    
    else:
        const = arr_sum[0]
        less = [i for i in arr_sum[1:] if i <= const]
        greater = [i for i in arr_sum[1:] if i > const]
        
    return merge(less) + [const] + merge(greater)

def sort_sentence(sentence):
    import operator
    a = sentence.split(' ')
    unsorted = {i : len(i) for i in a}
    sorted_dict = sorted(unsorted.items(), key=operator.itemgetter(1))
    result = ''
    for key, i in sorted_dict:
        result += key + ' '
    return result
"""
Created on Sat Nov 13 05:22:42 2021

@author: anast
"""


