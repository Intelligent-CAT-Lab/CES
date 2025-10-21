from typing import *
def move_one_ball(arr):
    print('[LINE]2[/LINE] may be hit')
    if len(arr)==0:
        print('[LINE]2[/LINE] is hit')
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      print('[LINE]11[/LINE] may be hit')
      if my_arr[i]!=sorted_array[i]:
          print('[LINE]11[/LINE] is hit')
        return False
    return True

move_one_ball([3, 4, 5, 1, 2])