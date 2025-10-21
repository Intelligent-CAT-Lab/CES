def unique_digits(x):
    odd_digit_elements = []
    for j, i in enumerate(x):
        print('[LINE]3[/LINE] may be hit')
        if all (int(c) % 2 == 1 for c in str(i)):
            print('[LINE]3[/LINE] is hit')
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)

unique_digits([15, 33, 1422, 1])