# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = 5, -4, 7, -1, 5
tup2 = 5, 0, 6, -3, -1
tup3 = 5, -1, 2, 0, -2

all_elem = tup1 + tup2 + tup3              #общий список всех элементов кортежей

without_duplicates=[]                      #список всех элементов кортежей без дублей
for elem in all_elem:
    if elem not in without_duplicates:     #если элемента из большого списка нет в списке без дублей,
        without_duplicates.append(elem)    #...то вносим его в список без дублей

elem_in_all=0
for elem in without_duplicates:
    if (elem in tup1) and (elem in tup2) and (elem in tup3):
        elem_in_all+=1
print(elem_in_all)
