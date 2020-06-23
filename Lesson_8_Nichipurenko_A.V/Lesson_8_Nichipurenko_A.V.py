my_list = []
print (my_list)


my_list1 = ['a', 'd', 'g', 12]
print(my_list1)


my_list2 = [10, "anna", "Fedir", "298", ["hello hjgsdfjhf"]]
print(my_list2)
print(len(my_list2))
del my_list2 [-1]
print(my_list2)

my_list2.append("Test") # додати елемент
print(my_list2)

del my_list2 [-1]
print(my_list2)

my_list2.insert(2, "help jngj") # вставити елемент
print(my_list2)

lst = []
for i in range(5):
    #lst.append()
    lst.insert(0,i)
    print(lst)

print()

ist_1 = [1,2,3,4,5]
price = 0
for i in range(len(lst)):
    price +=lst[i]
    print(price)


lst_2 = [1,2,3,4,5,12]
price = 0
for i in lst_2:
    price +=i
    print(price)


print()

lst_3 = [8, 10, 6, 2, 4]

for i in range(len(lst_3)+1):
    if lst_3[i+1]> lst_3[i]:
        print(True)
    else:
        print(False)


asd = [10, 6, 2, 4, 8, 20]
swapped = True
while swapped:
        swapped = False

        for i in range(len(asd) - 1):
            if asd[i] > asd[i+1]
            swapped = True
            print() 