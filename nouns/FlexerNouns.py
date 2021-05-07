from pathlib import Path
from pprint import pprint

from nouns.plural import get_plural_forms
from nouns.singular import get_singular_forms
from utils import (get_string_list_from_file, get_nouns_dicts_from_csv_file,
                   save_bs_dicts_to_txt)
from word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    info = [src_dict['Inf_0']]
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


def save_groups_to_bs():
    definitions = 'definitionsNouns.txt'

    print('*' * 3)
    print(f'Настройки:')
    print(definitions + '\n')

    *in_nouns_list, out_nouns = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_nouns_list = in_nouns_list[:-1]

    print('*' * 3)
    print(f'Файлы с исходными данными:')
    pprint(in_nouns_list)
    print()

    count = 0
    add_groups_to_bs_list = []

    for in_nouns in in_nouns_list:
        src_groups = get_nouns_dicts_from_csv_file(in_nouns)
        for src_dict in src_groups:
            add_groups_to_bs_list.append(get_group_word_form(src_dict))
            count += 1

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list), out_nouns)
    print('*' * 3)
    print(f'Создано {count} групп словоформ\n')

    print('*' * 3)
    print(f'Файл с результатами "{out_nouns}" сохранён в текущей директории:')
    print(Path().resolve())
    print()

    print('*' * 3)
    print('Для выхода нажмите любую Enter')
    input()


if __name__ == '__main__':
    save_groups_to_bs()

# compilation
# pyinstaller -F nouns/FlexerNouns.py
