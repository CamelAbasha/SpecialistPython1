# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    
    a = ticket_number // 100000
    b = ticket_number // 10000 % 10
    c = ticket_number // 1000 % 10
    d = ticket_number // 100 % 10
    e = ticket_number // 10 % 10
    f = ticket_number % 10
    return a + b + c == d + e + f


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
