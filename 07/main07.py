# 1. Створити телефонну книгу, яка матиме наступні команди:
#
# stats: кількість записів
#
# add: додати запис
#
# delete <name>: видалити запис за іменем (ключем)
#
# list: список всіх імен в книзі
#
# show <name>: детальна інформація по імені
#
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.
#

import os
import time

phone_dic = {
    'entry0': None,
    'entry1': '10',
    'entry2': '20',
    'entry3': '30',
    'entry4': '40',
    'entry5': '50',
}

while True:
    os.system('cls')
    inp = input('\n'
                'Welcome to the test phonebook.\n'
                'Here is the list of available commands:\n'
                'stats      - shows you the number of entries stored\n'
                'add        - adds a new entry\n'
                'delete     - deletes an entry\n'
                'list       - shows you all entries in the phonebook\n'
                'show       - tells you details about entry\n'
                '\n'
                'Enter command: ')

    inp_l = str(inp.lower())

    # list ---------------------------
    if inp_l == 'list':
        os.system('cls')
        print('')
        for k, v in phone_dic.items():
            print(f'{k}: {v}')
        list_inp = input('\n'
                         'Enter anything to start over: ')
        if list_inp is not '':
            continue
        else:
            continue
    # list ---------------------------

    # stats ---------------------------
    elif inp_l == 'stats':
        print(f'\n'
              f'This phonebook has:\n'
              f'{len(phone_dic)} entries\n'
              f'')
        time.sleep(2)
    # stats ---------------------------

    # show ---------------------------
    elif inp_l == 'show':
        os.system('cls')
        show_name = input('\n'
                          'Enter name to show: ')
        if show_name in phone_dic.keys():
            print(f'\n'
                  f'Item "{show_name}: {phone_dic.get(show_name)}" is present...')
            time.sleep(2)
        else:
            print(f'\n'
                  f'Name "{show_name}" was not found...')
            time.sleep(2)
    # show ---------------------------

    # delete ---------------------------
    elif inp_l == 'delete':
        os.system('cls')
        del_entry = input('\n'
                          'Enter name to delete: ')
        if del_entry in phone_dic.keys():
            del phone_dic[del_entry]
            print(f'\n'
                  f'Entry "{del_entry}" has been deleted...')
            time.sleep(2)
        else:
            print(f'\n'
                  f'Entry "{del_entry}" was not found...')
            time.sleep(2)
    # delete ---------------------------

    # add ---------------------------
    elif inp_l == 'add':
        os.system('cls')

        new_value = input('\n'
                          'Enter the new value (phone number): ')
        if new_value not in phone_dic.values():
            new_entry = input('\n'
                              'Type name for the new entry: ')
            phone_dic[new_entry] = new_value
            os.system('cls')
            print('\n'
                  'New entry with a value has been added...')
            time.sleep(2)
        else:
            os.system('cls')
            print(f'\n'
                  f'Value (phone number) "{new_value}" already exists. \n'
                  '\n'
                  f'You cannot overwrite it but you can delete it, \n'
                  f'and then create it with a new entry name.')
            add_inp = input('\n'
                            'Enter anything to start over: ')

            if add_inp == '':
                continue
            else:
                continue
    # add ---------------------------

    # no such command ---------------------------
    else:
        os.system('cls')
        print(f'\n'
              f'There is no such command as "{inp_l}"')
        any_inp = input('\n'
                        'Type "exit" to terminate program \n'
                        'or enter anything to start over: ')
        any_inp_l = str(any_inp.lower())
        if any_inp_l == 'exit':
            break
        else:
            continue
    # no such command ---------------------------
