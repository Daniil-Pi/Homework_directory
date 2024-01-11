def Main():
    file_name = "contacts.txt"
    flag = True
    while flag:
        user_answer = input("Введите '1' -  для записи, '2' - для чтения, '3' - для поиска, '4' - редактировать контакт, '5' - скопировать контакт в другой файл, '0' - для выхода: ")
        if user_answer == "1":
            add_contact(file_name)
        elif user_answer == "2":
            show_all(file_name)
        elif user_answer == "3":
            print_contact(search_contacts(file_name))
        elif user_answer == "4":
            edit_contact(file_name)
        elif user_answer == "5":
            copy_contact(file_name)
        elif user_answer == "0":
            print("Спасибо, пока!")
            flag = False

def print_contact(contact_list):
    for contact in contact_list:
        print(' | '.join(contact))

def get_contacts_from_file(file):
    with open(file, 'r', encoding = 'utf-8') as data:
        contacts = data.readlines()
    result = []
    for i, c in enumerate(contacts):
        lst = [str(i)]
        lst.extend(c.rstrip().split(','))
        result.append(lst)
    return result

def add_contact(file):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    number = input("Введите номер телефона: ")
    with open(file, 'a', encoding = 'utf-8') as data:
        data.write(f'{last_name}, {first_name}, {patronymic}, {number}\n')

def show_all(file):
    contacts = get_contacts_from_file(file)
    print_contact(contacts)

def search_contacts(file):
    search_str = input('Введите фамилию для поиска: ').lower()
    contacts = get_contacts_from_file(file)
    search_res = []
    for contact in contacts:
        if search_str in contact[1].lower():
            search_res.append(contact)
    return search_res
    

def edit_contact(file):
    res = search_contacts(file)
    print_contact(res)
    select_contact = int(input('Выберите индекс контакта: '))
    all_contacts = get_contacts_from_file(file)
    last_name = input("Введите фамилию для изменения или Enter, чтобы оставить прежнюю: ")
    first_name = input("Введите имя для изменения или Enter, чтобы оставить прежнее: ")
    patronymic = input("Введите отчество для изменения или Enter, чтобы оставить прежнее: ")
    number = input("Введите номер телефона для изменения или Enter, чтобы оставить прежний: ")
    if len(last_name) > 0:
        all_contacts[select_contact][1] = last_name
    if len(first_name) > 0:
        all_contacts[select_contact][2] = first_name
    if len(patronymic) > 0:
        all_contacts[select_contact][3] = patronymic
    if len(number) > 0:
        all_contacts[select_contact][4] = number
    print_contact(all_contacts)
    result = []
    for i in all_contacts:
        result.append(f"{','.join(i[1:])}\n")
    with open(file, 'w', encoding='utf-8') as data:
        data.writelines(result)

def copy_contact(file):
    res = search_contacts(file)
    print_contact(res)
    select_contact = int(input('Выберите индекс контакта: '))
    all_contacts = get_contacts_from_file(file)
    old_data = all_contacts[select_contact]
    new_name = input('Введите название файла: ')
    new_name = new_name + '.txt'
    with open(new_name, 'a', encoding='utf-8') as new_data:
        new_data.write(f"{','.join(old_data[1:])}\n")

if __name__ == '__main__':
    Main()