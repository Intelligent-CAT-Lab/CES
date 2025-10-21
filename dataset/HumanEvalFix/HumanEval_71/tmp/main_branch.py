def triangle_area(a, b, c):
    print('[LINE]1[/LINE] may be hit')
    if a + b <= c or a + c <= b or b + c <= a:
        print('[LINE]1[/LINE] is hit')
        return -1 
    s = (a + b + c)    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

triangle_area(3, 4, 5)