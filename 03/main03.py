# task 01 — Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
#
phrase = 'I love Python '
occasions = 42
result01 = phrase * occasions
print('ANSWER 01:', result01.count(phrase))

# task 02 — Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
#
age = 34
months_in_a_year = 12
age_in_month = age * months_in_a_year
result02 = age_in_month
print('ANSWER 02:', result02)

# task 03 — Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
# Підказка: використовуючи арифметичні оператори та/або приведення типів).
#
age_in_years = age_in_month
age_in_years /= months_in_a_year
result03 = int(age_in_years)
print('ANSWER 03:', result03)

# task 04 — Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”,
# де на замість пропусків буде підставлятись ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years.
#
first_name = 'Dmytro'
my_age = 'Му name is ' + first_name + '.' + ' I\'m ' + str(int(age_in_years)) + ' years old.'
result04 = my_age
print('ANSWER 04:', result04)

# task 05 — Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її із будь-якими іншими
# значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
#
my_var = 1
compare1 = my_var == occasions
compare2 = my_var != age
compare3 = my_var < months_in_a_year
compare4 = my_var > age_in_month
compare5 = my_var <= int(age_in_years)
result05 = compare1,compare2,compare3,compare4,compare5
print('ANSWER 05:', result05)

# task 06 — Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”.
#
a = 2
b = 5
c = 6
d = int(str(a)+str(b)+str(c))
result06 = d
print('ANSWER 06:', result06)
