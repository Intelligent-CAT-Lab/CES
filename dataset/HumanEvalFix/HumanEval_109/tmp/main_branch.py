def move_one_ball(arr):
    print('[LINE]1[/LINE] may be hit')
    if len(arr)==0:
      print('[LINE]1[/LINE] is hit')
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=sorted_array.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      print('[LINE]10[/LINE] may be hit')
      if my_arr[i]!=sorted_array[i]:
        print('[LINE]10[/LINE] is hit')
        return False
    return True

move_one_ball([3, 4, 5, 1, 2])