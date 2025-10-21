def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        print('[LINE]5[/LINE] may be hit')
        if int_digit%2 == 1:
            print('[LINE]5[/LINE] is hit')
            product*= product*int_digit
            odd_count+=1
    print('[LINE]8[/LINE] may be hit')
    print('[LINE]10[/LINE] may be hit')
    if odd_count ==0:
        print('[LINE]8[/LINE] is hit')
        return 0
    else:
        print('[LINE]10[/LINE] is hit')
        return product

digits(5576543)