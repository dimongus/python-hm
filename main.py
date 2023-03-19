def all_contacts():
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)


def find_contact(contact):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if contact in line:
                print(line)


def add_contact(new_contact):
    with open('phone_number.txt', 'a', encoding='utf8') as data:
        data.writelines('\n')
        data.writelines(new_contact)


def delete_contact(contact):
    with open('phone_number.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
    with open('phone_number.txt', 'w', encoding='utf8') as f:
        for line in lines:
            if contact not in line:
                f.write(line)


def edit_contact(old_contact, new_contact):
    with open('phone_number.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
    with open('phone_number.txt', 'w', encoding='utf8') as f:
        for line in lines:
            if old_contact in line:
                f.write(new_contact + '\n')
            else:
                f.write(line)

while True:
    numb = int(input('Введите значение:'
                     '\n 1 - вывод справочника, '
                     '\n 2 - поиска по имени, фамилии, номеру телефона, '
                     '\n 3 - добавления контакта в справочник'
                     '\n 4 - удаления контакта из справочника'
                     '\n 5 - изменения контакта в справочнике'
                     '\n 6 - для выхода из справочника  '
                     '\n --->>>> '))

    if numb == 6:
        break
    if numb == 1:
        all_contacts()
    elif numb == 2:
         contact = input('Введите значение для поиска -->> ')
         find_contact(contact)
    elif numb == 3:
         new_contact = input('Введите ИМЯ ФАМИЛИЯ НОМЕР ТЕЛЕФОНА нового контакта -->> ')
         add_contact(new_contact)
    elif numb == 4:
         contact = input('Введите контакт для удаления -->> ')
         delete_contact(contact)
    elif numb == 5:
         old_contact = input('Введите контакт для изменения -->> ')
         new_contact = input('Введите новый контакт -->> ')
         edit_contact(old_contact, new_contact)
else:
    print('Неправильный ввод. Попробуйте еще раз.')
