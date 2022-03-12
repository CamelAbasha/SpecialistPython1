# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
tup1 = 5,-4, 7,-1, 0
tup2 = 5, 0, 6,-3, -1
tup3 = 5,-1, 2, 0, -2

elem_in_all=0
mega_tup = tup1 + tup2 + tup3

for elem in mega_tup:
    if (elem in tup1) and (elem in tup2) and (elem in tup3):
        elem_in_all+=1

print(int(elem_in_all/3))
