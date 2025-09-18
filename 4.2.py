lst_1 = [6]
lst_count = 0
if len(lst_1) == 0:
    print(lst_1)
else:
    for i in lst_1:
        if (lst_1.index(i) % 2) == 0:
            lst_count = lst_count + i
    print(lst_count * lst_1[len(lst_1) - 1])