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

phone_dic = {
    '111': 'name1',
    '222': 'name2',
    '333': 'name3',
    '444': 'name4',
    '555': 'name5',
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
        print('')
        for k, v in phone_dic.items():
            print(f'{k}: {v}')
        input('\n'
              'Press ENTER to continue... ')
        continue
    # list ---------------------------

    # stats ---------------------------
    elif inp_l == 'stats':
        print(f'\n'
              f'This phonebook has:\n'
              f'{len(phone_dic)} entries')
        input('\n'
              'Press ENTER to continue... ')
        continue
    # stats ---------------------------

    # show ---------------------------
    elif inp_l == 'show':
        show_name = input('\n'
                          'Enter name to show: ')
        found = False
        for k, v in phone_dic.items():
            if show_name == v:
                print(f'\n'
                      f'Item "{k}: {v}" is present.')
                input('\n'
                      'Press ENTER to continue... ')
                found = True
        if not found:
            print(f'\n'
                  f'Name "{show_name}" was not found.')
            input('\n'
                  'Press ENTER to continue... ')
            continue
    # show ---------------------------

    # delete ---------------------------
    elif inp_l == 'delete':
        del_entry = input('\n'
                          'Enter phone number to delete: ')
        if del_entry in phone_dic.keys():
            del phone_dic[del_entry]
            print(f'\n'
                  f'Phone number "{del_entry}" deleted.')
            input('\n'
                  'Press ENTER to continue... ')
            continue
        else:
            print(f'\n'
                  f'Phone number "{del_entry}" not found.')
            input('\n'
                  'Press ENTER to continue... ')
            continue
    # delete ---------------------------

    # add ---------------------------
    elif inp_l == 'add':
        new_key = input('\n'
                        'Enter new phone number: ')
        if new_key not in phone_dic.keys():
            new_name = input('\n'
                             'Enter new name: ')
            phone_dic[new_key] = new_name
            print('\n'
                  'New item has been added.')
            input('\n'
                  'Press ENTER to continue... ')
            continue
        else:
            print(f'\n'
                  f'Phone number "{new_key}" already exists. \n'
                  '\n'
                  f'You cannot overwrite it but you can delete it.')
            input('\n'
                  'Press ENTER to continue... ')
            continue
    # add ---------------------------

    # no such command ---------------------------
    else:
        print(f'\n'
              f'There is no such command as "{inp_l}"')
        input('\n'
              'Press ENTER to continue... ')
        continue
    # no such command ---------------------------
