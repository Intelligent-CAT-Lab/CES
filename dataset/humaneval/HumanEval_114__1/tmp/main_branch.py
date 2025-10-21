from typing import *


def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        print('[LINE]8[/LINE] may be hit')
        if (s < 0):
            print('[LINE]8[/LINE] is hit')
            s = 0
        max_sum = max(s, max_sum)
    print('[LINE]11[/LINE] may be hit')
    if max_sum == 0:
        print('[LINE]11[/LINE] is hit')
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

minSubArraySum([0, 10, 20, 1000000])