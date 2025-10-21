def specialFilter(nums):
    
    count = 0
    for num in nums:
        print('[LINE]4[/LINE] may be hit')
        if num > 10:
            print('[LINE]4[/LINE] is hit')
            odd_digits = (1, 2, 3, 5, 7, 9)
            number_as_string = str(num)
            print('[LINE]7[/LINE] may be hit')
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                print('[LINE]7[/LINE] is hit')
                count += 1
        
    return count 

specialFilter([33, (- 2), (- 3), 45, 21, 109])