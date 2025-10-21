def can_arrange(arr):
    ind=-1
    i=1
    while i<len(arr):
      print(f'[ITE][LOC]4[/LOC][VAR]arr[i]<arr[i-1][/VAR][VAL]{arr[i]<arr[i-1]}[/VAL][/ITE]')
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
      ind-=1
    return ind

can_arrange([1, 2, 4, 5])
