from pathlib import Path
from pprint import pprint

from adjectives.comparative_forms import get_comparative_forms
from adjectives.full_forms import get_full_forms
from adjectives.short_forms import get_short_forms
from adjectives.superlative_forms import get_superlative_forms
from rem import reminder
from utils import (get_string_list_from_file,
                   get_adjectives_dicts_from_csv_file, save_bs_dicts_to_txt,
                   save_list_to_file)
from word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0:
        info = [src_dict['Inf_0'], ' '.join(list(filter(None, [
            src_dict['Inf_1'],
            src_dict['Inf_2'],
            src_dict['Inf_3'],
            src_dict['Inf_4'],
            src_dict['Inf_5'],
        ])))]

        word_forms = []
        adjectives_full_forms = get_full_forms(src_dict)
        word_forms += adjectives_full_forms

        if src_dict['Inf_1']:
            adjectives_short_forms = get_short_forms(src_dict)
            word_forms += adjectives_short_forms

        if src_dict['Inf_2']:
            adjectives_comparative_forms = get_comparative_forms(src_dict)
            word_forms += adjectives_comparative_forms

        if src_dict['Inf_3']:
            adjectives_superlative_forms = get_superlative_forms(src_dict)
            word_forms += adjectives_superlative_forms

        title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
        return GroupWordForm(title_word_form, word_forms[1:])
    else:
        title_word_form = TitleWordForm(name, '', [], '')
        return GroupWordForm(title_word_form, [])


def save_groups_to_bs():
    definitions = 'WordFormGen. Прилагательные.txt'
    print(f'Настройки:')
    print(f'"{definitions}"\n')

    *in_adjectives_list, out_adjectives = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_adjectives_list = in_adjectives_list[:-1]

    print(f'Файлы с исходными данными:')
    pprint(in_adjectives_list)
    print()

    print('Для продолжения нажмите Enter')
    input()
    print(f'{"#" * 30}\n')

    count = 0
    add_groups_to_bs_list = []
    add_groups_to_bg_list = []

    for in_adjectives in in_adjectives_list:
        src_groups = get_adjectives_dicts_from_csv_file(in_adjectives)
        for src_dict in src_groups:
            group_word_form = get_group_word_form(src_dict)
            add_groups_to_bs_list.append(group_word_form)
            add_groups_to_bg_list.append(
                group_word_form.title_word_form.bg_form)
            count += 1

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list), out_adjectives)
    print(f'Создано {count} групп словоформ')
    print(f'Создан файл "{out_adjectives}"')

    add_to_bg = 'Добавить в БГ. Прилагательные.txt'
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
# pyinstaller -F -i adjectives/icon.ico adjectives/FlexerAdjectives.py
