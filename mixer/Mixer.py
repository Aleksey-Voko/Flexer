from pathlib import Path
from pprint import pprint

from utils import get_string_list_from_file, read_src_bs, save_bs_dicts_to_txt


def add_groups_to_bs():
    definitions = 'insertion.txt'
    print('Настройки:')
    print(f'"{definitions}"\n')

    in_bs, *add_groups_list, out_bs = get_string_list_from_file(
        definitions, encoding='cp1251')
    add_groups_list = add_groups_list[1:-1]

    print('База словоформ:')
    print(f'"{in_bs}"\n')
    print(f'... чтение "{in_bs}" ...\n')
    word_forms_bases = list(read_src_bs(in_bs))
    word_form_names = [x.title_word_form.name for x in word_forms_bases]

    print('Файлы с группами:')
    pprint(add_groups_list)
    print()

    count = 0

    for add_groups in add_groups_list:
        verbs = list(read_src_bs(add_groups))

        for group_word_form in verbs:
            title_form = group_word_form.title_word_form
            name_title = title_form.name

            if not name_title.islower():
                print('В Н И М А Н И Е !')
                print('В добавляемых ЗС групп или одиночках найдены заглавные буквы:')
                print(title_form)
                print('Для продолжения нажмите Enter')
                input()

            if 'ё' in name_title:
                print('В Н И М А Н И Е !')
                print('В добавляемых ЗС групп или одиночках найдены буквы "Ёё":')
                print(title_form)
                print('Для продолжения нажмите Enter')
                input()

            if name_title in word_form_names:
                print('В Н И М А Н И Е !')
                print('Новые случаи омонимии!!!')
                print(title_form)
                print('Для продолжения нажмите Enter')
                input()

        word_forms_bases += verbs
        print(f'Дабавлены данные из файла "{add_groups}"')
        count += len(verbs)
    print()

    print('... сортировка ...\n')
    save_bs_dicts_to_txt(sorted(word_forms_bases), out_bs)

    print(f'В БС добавлено {count} групп словоформ')
    print(f'Создан файл "{out_bs}"\n')
    print(f'Файлы с результатами сохранены в текущей директории:')
    print(Path().resolve())
    print()

    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    add_groups_to_bs()

# compilation
# pyinstaller -F -i mixer/icon.ico mixer/Mixer.py
