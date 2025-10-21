def any_int(x, y, z):
    
    print(f'[ITE][LOC]2[/LOC][VAR]isinstance(x,int) and isinstance(y,int) and isinstance(z,int)[/VAR][VAL]{isinstance(x,int) and isinstance(y,int) and isinstance(z,int)}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]isinstance(z,int)[/VAR][VAL]{isinstance(z,int)}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]isinstance(x,int)[/VAR][VAL]{isinstance(x,int)}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]isinstance(y,int)[/VAR][VAL]{isinstance(y,int)}[/VAL][/ITE]')
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        print(f'[ITE][LOC]3[/LOC][VAR](x+y==z) or (y+z==x)[/VAR][VAL]{(x+y==z) or (y+z==x)}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]x+y==z[/VAR][VAL]{x+y==z}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]y+z==x[/VAR][VAL]{y+z==x}[/VAL][/ITE]')
        if (x+y==z) or (y+z==x):
            return True
        return False
    return False

any_int(2, 3, 1)
