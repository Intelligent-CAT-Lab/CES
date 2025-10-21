from typing import *
def can_arrange(arr):
    ind=-1
    i=1
    while i<len(arr):
      print('[LINE]5[/LINE] may be hit')
      if arr[i]<arr[i-1]:
          print('[LINE]5[/LINE] is hit')
        ind=i
      i+=1
    return ind

can_arrange([1,2,4,3,5])