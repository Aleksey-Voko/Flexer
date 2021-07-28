from pathlib import Path

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

    print('Файлы с добавляемыми группами словоформ:')
    for line in add_groups_list:
        print(line)
    print()

    count = 0

    capital_letters = []
    invalid_characters = []

    added_homonyms = []
    existing_homonyms = []

    for add_groups in add_groups_list:
        verbs = list(read_src_bs(add_groups))

        for group_word_form in verbs:
            title_form = group_word_form.title_word_form
            name_title = title_form.name

            if not name_title.islower():
                capital_letters.append(title_form.bg_form)

            if 'ё' in name_title.lower():
                invalid_characters.append(title_form.bg_form)

            if name_title in word_form_names:
                added_homonyms.append(title_form.bg_form)
                existing_homonyms += [
                    x.title_word_form.bg_form for x in word_forms_bases
                    if name_title == x.title_word_form.name
                ]

        word_forms_bases += verbs
        count += len(verbs)

    print(f'{"* " * 38}*\n')

    if capital_letters:
        print('В Н И М А Н И Е !')
        print('В добавляемых ЗС групп и одиночках найдены заглавные буквы:\n')
        for line in capital_letters:
            print(line)
        print('\nДля продолжения нажмите Enter')
        input()
    else:
        print('В Н И М А Н И Е !')
        print('В добавляемых ЗС групп и одиночках НЕТ заглавных букв.')
        print('Для продолжения нажмите Enter')
        input()

    if invalid_characters:
        print('В Н И М А Н И Е !')
        print('В добавляемых ЗС групп и одиночках найдена буква Ёё:\n')
        for line in invalid_characters:
            print(line)
        print('\nДля продолжения нажмите Enter')
        input()
    else:
        print('В Н И М А Н И Е !')
        print('В добавляемых ЗС групп и одиночках НЕТ буквы Ёё.')
        print('Для продолжения нажмите Enter')
        input()

    if added_homonyms:
        print('В Н И М А Н И Е !')
        print('Новые случаи омонимии!!!')
        print('В БС среди ЗС групп и одиночек ОБНАРУЖЕНЫ слова, омонимичные добавляемым ЗС групп и одиночкам.')
        print('Добавляемые:')
        for line in sorted(list(set(added_homonyms))):
            print(line)
        print('Уже имеющиеся в БС:')
        for line in sorted(list(set(existing_homonyms))):
            print(line)
        print('Для продолжения нажмите Enter')
        input()
    else:
        print('В Н И М А Н И Е !')
        print('Новых случаев омонимии НЕТ.')
        print('В БС среди ЗС групп и одиночек НЕ обнаружено слов, омонимичных добавляемым ЗС групп и одиночкам.')
        print('Для продолжения нажмите Enter')
        input()

    print(f'{"* " * 38}*\n')

    print('Добавлены данные из файлов:')
    for line in add_groups_list:
        print(line)
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
