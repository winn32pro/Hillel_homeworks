import random
#v1
list_new = []
lst_1 = [random.randint(1,100) for i in range(random.randint(3, 10))]
print(lst_1)
list_new.append(lst_1[0])
list_new.append(lst_1[2])
list_new.append(lst_1[-2])
print(list_new)

#v2
#lst_1 = [random.randint(1,100) for i in range(random.randint(3, 10))]
#print(lst_1)
#list_new = [lst_1[i] for i in range(0, 3) if i % 2 == 0] + [lst_1[-2]]
#print(list_new)
