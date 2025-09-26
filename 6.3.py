usr_number = int(input("Enter your number: "))
while usr_number >= 9:
    num_r = 1
    for i in str(usr_number):
        num_r *= int(i)
    usr_number = num_r
print(usr_number)