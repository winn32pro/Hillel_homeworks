import keyword
import string

usr_input = str(input("Enter a string: "))
#print(usr_input.count("_"))

if usr_input in keyword.kwlist or any(i.isupper() for i in usr_input) or any(i in string.punctuation.replace("_", "") for i in usr_input) or not usr_input:
    print('False')
elif any(i.isspace() for i in usr_input) or usr_input[0].isdigit() or usr_input[:2].count("_") > 1:
    print('False')
else:
    print('True')