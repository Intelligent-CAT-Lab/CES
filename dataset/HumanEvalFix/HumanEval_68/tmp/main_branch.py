def pluck(arr):
    print('[LINE]1[/LINE] may be hit')
    if(len(arr) == 0):
        print('[LINE]1[/LINE] is hit')
        return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    print('[LINE]3[/LINE] may be hit')
    if(evens == []): 
        print('[LINE]3[/LINE] is hit')
        return []
    return [arr.index(min(evens)), min(evens)]

pluck([4, 2, 3])