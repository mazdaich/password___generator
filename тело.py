import random


def generate_password():
    for _ in range(number_pas):
        total_pas = []
        total_pas += random.sample(chars, length_pas)
        print(*total_pas, sep="")


digit = "1234567890"
lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
punctuation = '!#$%&*+-=?@^_'
ignor = 'il1Lo0O'

chars = ''

print("Сколько паролей нужно сгенерировать?")
number_pas = int(input())
print("Какой длины должны быть пароли?")
length_pas = int(input())
print("Включать цифры в пароль? (да, нет)")
yes_digit = input()
if yes_digit == "да":
    chars += digit
print("Включать заглавные буквы? (да, нет)")
yes_up = input()
if yes_up == "да":
    chars += uppercase_letters
print("Включать строчные буквы? (да, нет)")
yes_low = input()
if yes_low == "да":
    chars += lowercase_letters
print("Включать другие символы? (да, нет)")
yes_pun = input()
if yes_pun == "да":
    chars += punctuation
print("Исключать ли неоднозначные символы il1Lo0O ? (да, нет)")
yes_ignor = input()
if yes_ignor == "да":
    for c in chars:
        if c in ignor:
            chars = chars.replace(c, "")

generate_password()
