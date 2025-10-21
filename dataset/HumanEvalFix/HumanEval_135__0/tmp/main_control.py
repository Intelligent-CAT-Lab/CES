def can_arrange(arr):
    ind=-1
    i=1

    while i<len(arr):
      print(f'[ITE][LOC]4[/LOC][VAR](i < len(arr))[/VAR][VAL]{(i < len(arr))}[/VAL][/ITE]')
      print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
      print(f'[ITE][LOC]4[/LOC][VAR]len(arr)[/VAR][VAL]{len(arr)}[/VAL][/ITE]')
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
      ind-=1
    return ind

can_arrange([1, 2, 4, 5])
