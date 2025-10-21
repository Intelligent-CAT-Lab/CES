from typing import *


def minSubArraySum(nums):
    max_sum = 0
    s = 0
    print(f'[ITE][LOC]7[/LOC][VAR]nums[/VAR][VAL]{nums}[/VAL][/ITE]')
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

minSubArraySum([0, 10, 20, 1000000])