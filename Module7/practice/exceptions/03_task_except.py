# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.

line="2 12 -45 7 10"
digits=line.split()
positive=[]

for d in digits:
    try:
        if int(d)>0:
            positive.append(int(d))
    except ValueError:
        print(d,'- это не число')

print(min(positive))
