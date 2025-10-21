from typing import *


def numerical_letter_grade(grades):

    letter_grade = []
    for gpa in grades:
        print('[LINE]7[/LINE] may be hit')
        print('[LINE]9[/LINE] may be hit')
        print('[LINE]11[/LINE] may be hit')
        print('[LINE]13[/LINE] may be hit')
        print('[LINE]15[/LINE] may be hit')
        print('[LINE]17[/LINE] may be hit')
        print('[LINE]19[/LINE] may be hit')
        print('[LINE]21[/LINE] may be hit')
        print('[LINE]23[/LINE] may be hit')
        print('[LINE]25[/LINE] may be hit')
        print('[LINE]27[/LINE] may be hit')
        print('[LINE]29[/LINE] may be hit')
        print('[LINE]31[/LINE] may be hit')
        if gpa == 4.0:
            print('[LINE]7[/LINE] is hit')
            letter_grade.append("A+")
        elif gpa > 3.7:
            print('[LINE]9[/LINE] is hit')
            letter_grade.append("A")
        elif gpa > 3.3:
            print('[LINE]11[/LINE] is hit')
            letter_grade.append("A-")
        elif gpa > 3.0:
            print('[LINE]13[/LINE] is hit')
            letter_grade.append("B+")
        elif gpa > 2.7:
            print('[LINE]15[/LINE] is hit')
            letter_grade.append("B")
        elif gpa > 2.3:
            print('[LINE]17[/LINE] is hit')
            letter_grade.append("B-")
        elif gpa > 2.0:
            print('[LINE]19[/LINE] is hit')
            letter_grade.append("C+")
        elif gpa > 1.7:
            print('[LINE]21[/LINE] is hit')
            letter_grade.append("C")
        elif gpa > 1.3:
            print('[LINE]23[/LINE] is hit')
            letter_grade.append("C-")
        elif gpa > 1.0:
            print('[LINE]25[/LINE] is hit')
            letter_grade.append("D+")
        elif gpa > 0.7:
            print('[LINE]27[/LINE] is hit')
            letter_grade.append("D")
        elif gpa > 0.0:
            print('[LINE]29[/LINE] is hit')
            letter_grade.append("D-")
        else:
            print('[LINE]31[/LINE] is hit')
            letter_grade.append("E")
    return letter_grade

numerical_letter_grade([0, 0.7])