from typing import *


def specialFilter(nums):

    count = 0
    for num in nums:
        print(f'[ITE][LOC]7[/LOC][VAR]num > 10[/VAR][VAL]{num > 10}[/VAL][/ITE]')
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            print(f'[ITE][LOC]10[/LOC][VAR]int(number_as_string[0]) in odd_digits and int(
                    number_as_string[-1]) in odd_digits[/VAR][VAL]{int(number_as_string[0]) in odd_digits and int(
                    number_as_string[-1]) in odd_digits}[/VAL][/ITE]')
            print(f'[ITE][LOC]10[/LOC][VAR]int(number_as_string[0]) in odd_digits[/VAR][VAL]{int(number_as_string[0]) in odd_digits}[/VAL][/ITE]')
            print(f'[ITE][LOC]10[/LOC][VAR]int(
                    number_as_string[-1]) in odd_digits[/VAR][VAL]{int(
                    number_as_string[-1]) in odd_digits}[/VAL][/ITE]')
            if int(number_as_string[0]) in odd_digits and int(
                    number_as_string[-1]) in odd_digits:
                count += 1

    return count

specialFilter([])