import sys
from pathlib import Path

from adjectives.comparative_forms import get_comparative_forms
from adjectives.full_forms import get_full_forms
from adjectives.short_forms import get_short_forms
from adjectives.superlative_forms import get_superlative_forms
from flexer_errors import get_error_message, InputDataError
from rem import reminder
from utils import (get_string_list_from_file,
                   save_bs_dicts_to_txt,
                   save_list_to_file, get_long_dicts_from_csv_file)
from word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    src_dict['name'] = src_dict['name'].replace('*', '')
    if any(list(src_dict.values())[1:-2]):
        info = list(filter(None, list(src_dict.values())[1:]))

        word_forms = []

        if src_dict['Inf_0']:
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

        if name.startswith('*'):
            title_word_form = TitleWordForm(name, '.ПмИ', info, '')
            return GroupWordForm(title_word_form, word_forms)
        else:
            title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
            return GroupWordForm(title_word_form, word_forms[1:])
    else:
        title_word_form = TitleWordForm(name, '', [], '')
        return GroupWordForm(title_word_form, [])


def check_input_data(src_dict: dict):
    in_data_string = ' '.join(list(filter(None, [
        src_dict['name'],
        src_dict['Inf_0'],
        src_dict['Inf_1'],
        src_dict['Inf_2'],
        src_dict['Inf_3'],
        src_dict['Inf_4'],
        src_dict['Inf_5'],
    ])))

    # Блокировка III
    if (
            (
                    src_dict['name'].startswith('*')
                    or src_dict['name'] in ('горазд', 'рад', 'полным-полон')
            )
            and src_dict['Inf_0']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка III.\n'
                   'Прилагательные ГОРАЗД, РАД, ПОЛНЫМ-ПОЛОН '
                   'и адъектированные причастия\n'
                   'НЕ образуют полную форму.')
        raise InputDataError(message)


def save_groups_to_bs():
    definitions = 'WordFormGen. Прилагательные.txt'
    print(f'Настройки:')
    print(f'{definitions}\n')

    *in_adjectives_list, out_adjectives = [
        x for x in list(
            get_string_list_from_file(definitions, encoding='cp1251')
        )
        if x
    ]

    print(f'Файлы с исходными данными:')
    for line in in_adjectives_list:
        print(line)
    print()

    print('Для продолжения нажмите Enter')
    input()
    print(f'{"* " * 38}*\n')

    count = 0
    add_groups_to_bs_list = []
    add_groups_to_bg_list = []

    error_list = []

    for in_adjectives in in_adjectives_list:
        src_groups = get_long_dicts_from_csv_file(in_adjectives, num_fields=7)
        for src_dict in src_groups:

            try:
                check_input_data(src_dict)
                group_word_form = get_group_word_form(src_dict)
                add_groups_to_bs_list.append(group_word_form)
                add_groups_to_bg_list.append(
                    group_word_form.title_word_form.bg_form)
                count += 1
            except InputDataError as e:
                error_list.append(get_error_message(e))
            except KeyError as e:
                error_list.append(
                    'В Н И М А Н И Е !\n'
                    'Аварийное завершение.\n'
                    f'Несуществующий шаблон: {str(e)[1:-1]}\n'
                    'Для продолжения нажмите Enter'
                )

    if error_list:
        for line in error_list:
            print(line)
            input()
        print(f'Количество ошибок: {len(error_list)}')
        print('Для выхода нажмите Enter')
        input()
        sys.exit()

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
