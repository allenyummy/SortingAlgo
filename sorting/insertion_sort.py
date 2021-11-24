# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Insertion Sort

from __future__ import print_function
from typing import List


def insertion_sort_1(arr: List[int]) -> List[int]:
    
    if len(arr) <= 1:
        return

    for i in range(1, len(arr)):

        j = i
        while j > 0 and arr[j-1] > arr[j]:

            print (f"j={j}, {arr[j-1]} <-> {arr[j]}")

            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
            print (arr)
    

def insertion_sort_2(arr: List[int]) -> List[int]:
    
    if len(arr) <= 1:
        return
    
    for i in range(1, len(arr)):

        num = arr[i]

        j = i
        while j > 0 and arr[j-1] > num:
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = num




arr = [1, 5, 3, 2, 4]
print (arr)
arr_b = insertion_sort(arr)
print (arr_b)
