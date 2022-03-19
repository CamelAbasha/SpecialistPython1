# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

import math
def palindrome(number):
     return str(number)==str(number)[::-1]

print(palindrome(12321))

def palindrome_no_strings(number):
    i = 0
    while number != 0:
        length = math.log10(number) // 1 + 1
        last_digit = number % 10
        first_digit = number // (10 ** (length - i-1))
        number = number % (first_digit * 10 ** (length - i-1))//10
        if first_digit != last_digit:
            return False
    return True


print(palindrome_no_strings(123321))
print(palindrome_no_strings(124321))
print(palindrome_no_strings(12431))
