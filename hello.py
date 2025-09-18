lst_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
start_count = len(lst_1)
for i in lst_1:
    if i == 0:
        lst_1.remove(0)
        lst_1.append(0)
print(lst_1)