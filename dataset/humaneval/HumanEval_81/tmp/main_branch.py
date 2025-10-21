from typing import *
def numerical_letter_grade(grades):

   
    letter_grade = []
    for gpa in grades:
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        print('[LINE]12[/LINE] may be hit')
        print('[LINE]14[/LINE] may be hit')
        print('[LINE]16[/LINE] may be hit')
        print('[LINE]18[/LINE] may be hit')
        print('[LINE]20[/LINE] may be hit')
        print('[LINE]22[/LINE] may be hit')
        print('[LINE]24[/LINE] may be hit')
        print('[LINE]26[/LINE] may be hit')
        print('[LINE]28[/LINE] may be hit')
        print('[LINE]30[/LINE] may be hit')
        if gpa == 4.0:
            print('[LINE]6[/LINE] is hit')
            letter_grade.append("A+")
        elif gpa > 3.7:
            print('[LINE]8[/LINE] is hit')
            letter_grade.append("A")
        elif gpa > 3.3:
            print('[LINE]10[/LINE] is hit')
            letter_grade.append("A-")
        elif gpa > 3.0:
            print('[LINE]12[/LINE] is hit')
            letter_grade.append("B+")
        elif gpa > 2.7:
            print('[LINE]14[/LINE] is hit')
            letter_grade.append("B")
        elif gpa > 2.3:
            print('[LINE]16[/LINE] is hit')
            letter_grade.append("B-")
        elif gpa > 2.0:
            print('[LINE]18[/LINE] is hit')
            letter_grade.append("C+")
        elif gpa > 1.7:
            print('[LINE]20[/LINE] is hit')
            letter_grade.append("C")
        elif gpa > 1.3:
            print('[LINE]22[/LINE] is hit')
            letter_grade.append("C-")
        elif gpa > 1.0:
            print('[LINE]24[/LINE] is hit')
            letter_grade.append("D+")
        elif gpa > 0.7:
            print('[LINE]26[/LINE] is hit')
            letter_grade.append("D")
        elif gpa > 0.0:
            print('[LINE]28[/LINE] is hit')
            letter_grade.append("D-")
        else:
            print('[LINE]30[/LINE] is hit')
            letter_grade.append("E")
    return letter_grade

numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) 