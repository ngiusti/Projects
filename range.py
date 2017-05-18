my_list1 = [67,45,2,13,1,998]
my_list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

for i in range(len(my_list1)):
    for j in range(len(my_list1) - 1):
        if my_list1[j] > my_list1[j+1]:
            my_list1[j+1], my_list1[j] = my_list1[j], my_list1[j+1]

print my_list1


for i in range(len(my_list2)):
    for j in range(len(my_list2) - 1):
        if my_list2[j] > my_list2[j+1]:
            my_list2[j+1], my_list2[j] = my_list2[j], my_list2[j+1]

print my_list2
