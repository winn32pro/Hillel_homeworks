while True:
        num_1 = int(input('write first number: '))
        num_2 = int(input('write second number: '))
        opr = input('write arithmetic operator: ')
        if opr == '+':
            print(num_1 + num_2)
        elif opr == '-':
            print(num_1 - num_2)
        elif opr == '*':
            print(num_1 * num_2)
        elif opr == '/' and num_2 != 0:
            print(num_1 / num_2)
        else:
            print('invalid operator')
        question = input("Do you want to continue? y or q: ")
        if question == 'y':
            print('Ok, let\'s continue')
        elif question == 'q':
            print('Ok, let\'s quit')
            break
        else:
            print('invalid command. Only y or q')
            break