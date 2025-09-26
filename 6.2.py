try:
    usr_data = int(input("Enter a number: "))
    if usr_data >=0 and usr_data <= 8640000:
        usr_day = usr_data // 86400
        usr_hour = ((usr_data % 86400) // 3600)
        usr_data_min = (usr_data % 3600) // 60
        usr_data_sec = (usr_data % 3600) % 60
    else:
        print("Enter a valid number")
    decl_day = usr_day % 10
    decl_exept = usr_day % 100
    if decl_exept >= 11 and decl_exept <= 14:
        day = 'днів'
    else:
        if decl_day == 1:
            day = 'день'
        elif decl_day >= 2 and decl_day <= 4:
            day = 'дні'
        else:
            day = 'днів'
    print(f'{usr_day} {day}, {str(usr_hour).zfill(2)}:{str(usr_data_min).zfill(2)}:{str(usr_data_sec).zfill(2)}')
except ValueError:
    print("Enter a number")