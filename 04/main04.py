# task 01 — Створити програму, яка буде очікувати введення тексту від користувача і
# повідомляти — чи є введений текст “числом” чи “словом”.
#
# task 02 — Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
#
# task 03 — Якщо це “слово”, програма має вказати його довжину.
#
input_by_user = input('Enter here anything you want: ')
if input_by_user.isdigit():
    input_by_user = int(input_by_user)
    print(type(input_by_user))
    input_by_user = input_by_user % 2 == 0
    if not input_by_user:
        print(f'It is ODD because it\'s {input_by_user}')
    else:
        print(f'It is EVEN because it\'s {input_by_user}')
elif input_by_user.isalpha():
    print(type(input_by_user))
    print(f'It is {len(input_by_user)} character(s) long')
else:
    print(type(input_by_user))
    print('Looks like it\'s not a separate number and not a separate word')
