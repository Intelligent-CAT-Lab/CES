def is_happy(s):
    print('[LINE]1[/LINE] may be hit')
    if len(s) < 3:
      print('[LINE]1[/LINE] is hit')
      return False

    for i in range(len(s) - 2):
      
      print('[LINE]6[/LINE] may be hit')
      if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
        print('[LINE]6[/LINE] is hit')
        return False
    return True

is_happy('xyy')