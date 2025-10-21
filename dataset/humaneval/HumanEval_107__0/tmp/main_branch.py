from typing import *


def even_odd_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        print('[LINE]11[/LINE] may be hit')
        print('[LINE]13[/LINE] may be hit')
        if i % 2 == 1 and is_palindrome(i):
            print('[LINE]11[/LINE] is hit')
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            print('[LINE]13[/LINE] is hit')
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

even_odd_palindrome(9)