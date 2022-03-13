# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# TODO: your code here
def separate(s):                #эта функция вытягивает слагаемые из выражения
    b = s.find(' - ')
    if b == -1:
        b = s.find(' + ')
    return [s[:b], s[b + 3:]]


def oper(s):                    #эта функция определяет знак операции
    if s.find(' + ') == -1:
        return -1
    return 1


def int_part(s):                #эта функция определяет целую часть
    if ' ' in s:
        return s.split()[0].replace('-', '')
    elif '/' in s:
            return 0
    return s.replace('-', '')


def frac_part(s):               #эта функция определяет дробную часть
    if '/' in s:
        return s.split()[-1].replace('-', '')
    return 0


def koeff(s):                   #эта функция определяет знак числа
    if s[0] == '-':
        return -1
    return 1


def local_denom(s):             #эта функция определяет числитель дроби
    if s==0:
        return 1
    return int(s[s.find('/') + 1:])


def local_numerator(s):         #эта функция определяет знаменатель дроби
    if s==0:
        return 0
    return int(s[:s.find('/')].replace('-', ''))

def nod(a, b):                  #эта функция определяет наименьшее общее кратное 2 чисел
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a)

exp = '-2/3 - 2'
number1, number2 = separate(exp)[0], separate(exp)[1]

n1 = int(int_part(number1)) * koeff(number1)
x1 = local_numerator(frac_part(number1))
y1 = local_denom(frac_part(number1))

n2 = int(int_part(number2)) * oper(exp) * koeff(number2)
x2 = local_numerator(frac_part(number2))
y2 = local_denom(frac_part(number2))

full_part = int(n1) + int(n2)

frac_numer = x1 * koeff(number1) * y2 + x2 * oper(exp) * koeff(number2) * y1
y = y1 * y2
total_numer = full_part * y + frac_numer

if total_numer % y == 0:
    print(int(total_numer / y))
else:
    n = koeff(str(total_numer)) * (abs(total_numer) // y)
    if n == 0:
        if total_numer < 0:
            n = '-'
        else:
            n = ''

    x = abs(total_numer) % y
    nod_xy = nod(x, y)

    if n == '-' or n == '':
        print(n + str(int(x / nod_xy)) + '/' + str(int(y / nod_xy)))
    else:
        print(n, str(int(x / nod_xy)) + '/' + str(int(y / nod_xy)))
