from typing import *
def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        print(f'[ITE][LOC]6[/LOC][VAR]s < 0[/VAR][VAL]{s < 0}[/VAL][/ITE]')
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    print(f'[ITE][LOC]9[/LOC][VAR]max_sum == 0[/VAR][VAL]{max_sum == 0}[/VAL][/ITE]')
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

minSubArraySum([2, 3, 4, 1, 2, 4]) 