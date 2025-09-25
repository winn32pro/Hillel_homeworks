import string

usr_input = input("Enter your letters: ").replace('-', '').replace(' ', '')
letter_list = []
for i in string.ascii_letters:
    letter_list.append(i)
if len(usr_input) == 2:
    first_letter = letter_list.index(usr_input[0])
    second_letter = letter_list.index(usr_input[1])
    letter_string = letter_list[first_letter:second_letter + 1]
    print(''.join(letter_string))
else:
    print(usr_input)