lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_count = 0
if len(lst_1) == 0:
    lst_1.append(0)
    print(lst_1)
else:
    for i in lst_1:
        if (lst_1.index(i) % 2) == 0:
            lst_count = lst_count + i
    print(lst_count * lst_1[len(lst_1) - 1])