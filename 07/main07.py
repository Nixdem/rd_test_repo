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

# importing some necessary libs here
import os
import time
# lib import finished

phone_dic = {
    'entry0': None,
    'entry1': 10,
    'entry2': 20,
    'entry3': 30,
    'entry4': 40,
    'entry5': 50,
}

def dic_count_items(c_var_i):
    counter = 0
    for key0,value0 in c_var_i.items():
        counter += 1
    return counter


# decided to do it in cycle, omg here we go
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
        print('\n')
        for k, v in phone_dic.items():
            print(k, v)
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
              f'{dic_count_items(phone_dic)} entries\n'
              f'')
    # stats ---------------------------

    # show ---------------------------
    elif inp_l == 'show':
        os.system('cls')
        show_entry = input('\n'
                          'Type name of the entry to show: ')
        if show_entry in phone_dic.keys():
            print(f'\n'
                  f'Entry "{show_entry} : {phone_dic.get(show_entry)}" is present...')
            time.sleep(3)
        else:
            print(f'\n'
                  f'Entry "{show_entry}" was not found...')
            time.sleep(2)
    # show ---------------------------

    # delete ---------------------------
    elif inp_l == 'delete':
        os.system('cls')
        show_entry = input('\n'
                          'Type name of the entry to delete: ')
        if show_entry in phone_dic.keys():
            del phone_dic[show_entry]
            print(f'\n'
                  f'Entry "{show_entry}" with a value has been deleted...')
            time.sleep(2)
        else:
            print(f'\n'
                  f'Entry {show_entry} was not found...')
            time.sleep(2)
    # delete ---------------------------

    # add ---------------------------
    elif inp_l == 'add':
        os.system('cls')
        new_entry = input('\n'
                          'Type name for the new entry: ')
        if new_entry not in phone_dic:
            new_value = input('\n'
                              'Type name for the new value: ')
            phone_dic[new_entry] = new_value
            os.system('cls')
            print('\n'
                  'New entry with a value has been added...')
            time.sleep(2)
        else:
            os.system('cls')
            print(f'\n'
                  f'There is the "{new_entry}" already. '
                  f'You cannot overwrite it but you can delete it '
                  f'and then create it with a new value.')
            add_inp = input('\n'
                            'Enter anything to start over: ')
            if add_inp is not '':
                continue
            else:
                continue
    # add ---------------------------

    # no comm ---------------------------
    else:
        os.system('cls')
        print(f'\n'
              f'There is no such command as "{inp_l}"')
        while True:
            nocom_inp = input('\n'
                              'Type "yes" to start over.\n'
                              'Type "exit" to exit.\n'
                              '\n'
                              'Enter command: ')
            nocom_inp_l = str(nocom_inp.lower())
            if nocom_inp_l == 'yes':
                break
            elif nocom_inp_l == 'exit':
                os.system('cls')
                print('\n'
                      'I don\'t know how to break out of inner loops yet '
                      'so that I could exit this program at this point '
                      'without starting it over.')
                any_inp = input('\n'
                                'Enter anything to start over: ')
                if any_inp is not '':
                    break
                else:
                    break
            elif nocom_inp_l != 'yes' or 'exit':
                os.system('cls')
                print('\n'
                      'You have to type "yes" or "exit".')
                continue
            else:
                continue
    # no comm ---------------------------
