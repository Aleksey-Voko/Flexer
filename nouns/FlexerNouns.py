from pathlib import Path

from flexer_errors import get_error_message, InputDataError
from nouns.plural import get_plural_forms
from nouns.singular import get_singular_forms
from rem import reminder
from utils import (get_string_list_from_file, save_bs_dicts_to_txt,
                   save_list_to_file, get_word_dicts_from_csv_file)
from word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0:
        in_data_list = [name, inf_0]
        if src_dict['Inf_1']:
            in_data_list.append(''.join(list(filter(None, [
                src_dict['Inf_1'],
                src_dict['Inf_2'],
                src_dict['Inf_3'],
            ]))))
        if src_dict['Inf_4']:
            in_data_list.append(''.join(list(filter(None, [
                src_dict['Inf_4'],
                src_dict['Inf_5'],
                src_dict['Inf_6'],
            ]))))
        in_data_string = ' '.join(in_data_list)

        # Блокировка I
        if not src_dict['Inf_4'] and src_dict['Inf_2'] != '!':
            message = (f'{in_data_string}\n'
                       'Блокировка I.\n'
                       'Отсутствие индикатора "!"\n'
                       'Нет форм мн. ч., однако индикатор "!" '
                       'после указателя рода отсутствует.')
            raise InputDataError(message)

        # Блокировка I
        if not src_dict['Inf_1'] and src_dict['Inf_5'] != '!':
            message = (f'{in_data_string}\n'
                       'Блокировка I.\n'
                       'Отсутствие индикатора "!"\n'
                       'Нет форм ед. ч., однако индикатор "!" '
                       'после индикатора мн. ч. отсутствует.')
            raise InputDataError(message)

        # Блокировка II.
        if (
                src_dict['Inf_1'] and src_dict['Inf_4']
                and
                (
                        src_dict['Inf_2'] == '!'
                        or src_dict['Inf_5'] == '!'
                )
        ):
            message = (f'{in_data_string}\n'
                       'Блокировка II.\n'
                       'Необоснованное применение индикатора "!"\n'
                       'Есть формы и ед. ч., и мн. ч., поэтому применение '
                       'хотя бы одного индикатора "!" необоснованно.')
            raise InputDataError(message)

        info = [inf_0]
        if src_dict['Inf_1']:
            info.append(''.join(list(filter(None, [
                src_dict['Inf_1'],
                src_dict['Inf_2'],
                src_dict['Inf_3']]))))
        if src_dict['Inf_4']:
            info.append(''.join(list(filter(None, [
                src_dict['Inf_4'],
                src_dict['Inf_5'],
                src_dict['Inf_6']]))))

        word_forms = []
        if src_dict['Inf_1']:
            singular_word_forms = get_singular_forms(src_dict)
            word_forms += singular_word_forms
            if src_dict['Inf_4']:
                plural_word_forms = get_plural_forms(
                    src_dict, singular_word_forms)
                word_forms += plural_word_forms
        elif src_dict['Inf_4']:
            plural_word_forms = get_plural_forms(src_dict, [])
            word_forms += plural_word_forms

        title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
        return GroupWordForm(title_word_form, word_forms[1:])
    else:
        title_word_form = TitleWordForm(name, '', [], '')
        return GroupWordForm(title_word_form, [])


def save_groups_to_bs():
    definitions = 'WordFormGen. Существительные.txt'
    print(f'Настройки:')
    print(f'"{definitions}"\n')

    *in_nouns_list, out_nouns = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_nouns_list = in_nouns_list[:-1]

    print(f'Файлы с исходными данными:')
    for line in in_nouns_list:
        print(line)
    print()

    print('Для продолжения нажмите Enter')
    input()
    print(f'{"* " * 38}*\n')

    count = 0
    add_groups_to_bs_list = []
    add_groups_to_bg_list = []

    error_list = []

    for in_nouns in in_nouns_list:
        src_groups = get_word_dicts_from_csv_file(in_nouns, num_fields=8)
        for src_dict in src_groups:

            try:
                group_word_form = get_group_word_form(src_dict)
                add_groups_to_bs_list.append(group_word_form)
                add_groups_to_bg_list.append(
                    group_word_form.title_word_form.bg_form)
                count += 1
            except KeyError as e:
                error_list.append(
                    'В Н И М А Н И Е !\n'
                    'Аварийное завершение.\n'
                    f'Несуществующий шаблон: {str(e)[1:-1]}\n'
                    'Для продолжения нажмите Enter'
                )
            except InputDataError as e:
                error_list.append(get_error_message(e))

    if error_list:
        for line in error_list:
            print(line)
            input()
        print(f'Количество ошибок: {len(error_list)}')
        print('Для выхода нажмите Enter')
        input()
        quit()

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list), out_nouns)
    print(f'Создано {count} групп словоформ')
    print(f'Создан файл "{out_nouns}"')

    add_to_bg = 'Добавить в БГ. Существительные.txt'
    save_list_to_file(sorted(add_groups_to_bg_list,
                             key=lambda x: x.replace('*', '').lower()),
                      add_to_bg, encoding='cp1251')
    print(f'Создан файл "{add_to_bg}"\n')

    print(f'Файлы с результатами сохранены в текущей директории:')
    print(Path().resolve())
    print()

    print('Для продолжения нажмите Enter')
    input()

    print(f'{reminder}\n')

    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    save_groups_to_bs()

# compilation
# pyinstaller -F -i nouns/icon.ico nouns/FlexerNouns.py
