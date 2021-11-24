# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Quick Sort

from __future__ import print_function
from typing import List


def quick_sort_1(arr: List[int], left, right):

    def partition() -> int: