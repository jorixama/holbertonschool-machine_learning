#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    result=[]
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
