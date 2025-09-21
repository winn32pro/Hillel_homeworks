import sys

usr_input = str(input("Enter a string: "))
print(usr_input)
key_list = ['False', 'None', 'True', 'and', 'or', 'not', 'as', 'assert'
            'break', 'continue', 'def', 'del', 'elif', 'else', 'class',
            'except', 'finally', 'finally', 'for', 'from', 'global',
            'exec', 'if', 'import', 'in', 'is', 'lambda','nonlocal',
            'pass', 'print', 'raise', 'return', 'try', 'while', 'with',
            'yield']
punctuation_list = ['(', ')', '[', ']', '{', '}' ',', ':', '.', ';', '@',
                    '=', '->', '+=', '-=', '*=', '/=', '//=', '%=', '@=',
                    '&=', '|=', '^=', '>>=', '<<=', '**=', ' ', '/', '!']
for i in punctuation_list:
    if usr_input.find(i) != -1:
       print('False')
    break
else:
    if usr_input in key_list or usr_input.islower() is False or usr_input.isdigit() is True:
        print('False')
    else:
        print('True')
