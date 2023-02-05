import time

sel = input('Select prog (1 or 2): ')

# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію
# по кожному надрукованому символу:
#
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”
#

if sel == '1':
    value = input('Enter any text here: ')
    for item in value:
        if item.isdigit():
            item = int(item)
            item_bool = item % 2 == 0
            if not item_bool:
                print(f'This "{item}" is a "{type(item)}", and it\'s "ODD"'
                      f' cuz it returned "{item_bool}".')
            else:
                print(f'This "{item}" is a "{type(item)}", and it\'s "EVEN"'
                      f' cuz it returned "{item_bool}".')
        elif item.isalpha():
            item_bool = item.isupper()
            if not item.isupper():
                print(f'This "{item}" is a "{type(item)}", and it\'s "LOWER"'
                      f' cuz it returned "{item_bool}".')
            else:
                print(f'This "{item}" is a "{type(item)}", and it\'s "UPPER"'
                      f' cuz it returned "{item_bool}".')
        elif not item.isalnum():
            item_bool = not item.isalnum()
            print(f'This "{item}" is not a "DIGIT" nor a "LETTER"'
                  f', but maybe it\'s a "SYMBOL" cuz it returned "{item_bool}".')

# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, поки її виконання
# не буде перервано вручну.
#
# Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати бібліотеку
# time (import time), а саме функцію sleep().
# (time.sleep(second), де second, це кількість секунд, які програма має чекати).
#

elif sel == '2':
    while True:
        print('I love Python')
        time.sleep(4.2)

else:
    print('bye')




