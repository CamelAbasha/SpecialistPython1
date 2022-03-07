# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число:"))     # Первое число
second_number = int(input("Второе число:"))    # Второе число

# TODO: your code here

i,triple=first_number,[]

while i<=second_number:
    if i%3==0:
        triple.append(i)
    i+=1
print(triple)
