from pathlib import Path

from flexer_errors import get_error_message, InputDataError
from rem import reminder, reminder_verbs
from utils import (get_string_list_from_file, save_bs_dicts_to_txt,
                   get_long_dicts_from_csv_file, save_list_to_file)
from verbs.imperative_mood import get_imperative_mood_forms
from verbs.joint_action import get_joint_action_forms
from verbs.passive_past_participle import get_passive_past_participle
from verbs.passive_present import get_passive_present_participle
from verbs.past_participle import get_past_participle
from verbs.past_participle_is_valid import get_past_participle_is_valid
from verbs.past_tense import get_past_tense_forms
from verbs.present_future import get_present_future_forms
from verbs.present_participle import get_present_participle
from verbs.present_participle_is_valid import get_present_participle_is_valid
from word_form import GroupWordForm, TitleWordForm


def get_group_word_form(src_dict: dict) -> GroupWordForm:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0:
        info = [src_dict['Inf_0'], src_dict['Inf_1']]
        info += list(filter(None, [
            src_dict['Inf_2'],
            src_dict['Inf_3'],
            src_dict['Inf_4'],
            src_dict['Inf_5'],
            src_dict['Inf_6'],
            src_dict['Inf_7'],
            src_dict['Inf_8'],
            src_dict['Inf_9'],
            src_dict['Inf_10'],
            src_dict['Inf_11'],
            src_dict['Inf_12'],
        ]))

        word_forms = []
        if src_dict['Inf_3']:
            present_future_forms = get_present_future_forms(src_dict)
            word_forms += present_future_forms

        if src_dict['Inf_4']:
            past_tense_forms = get_past_tense_forms(src_dict)
            word_forms += past_tense_forms

        if src_dict['Inf_5']:
            imperative_mood_forms = get_imperative_mood_forms(src_dict)
            word_forms += imperative_mood_forms

        if src_dict['Inf_6']:
            joint_action_forms = get_joint_action_forms(src_dict)
            word_forms += joint_action_forms

        if src_dict['Inf_7']:
            present_participle_is_valid_forms = get_present_participle_is_valid(src_dict)
            word_forms += present_participle_is_valid_forms

        if src_dict['Inf_8']:
            passive_present_participle_forms = get_passive_present_participle(src_dict)
            word_forms += passive_present_participle_forms

        if src_dict['Inf_9']:
            past_participle_is_valid_forms = get_past_participle_is_valid(src_dict)
            word_forms += past_participle_is_valid_forms

        if src_dict['Inf_10']:
            passive_past_participle_forms = get_passive_past_participle(src_dict)
            word_forms += passive_past_participle_forms

        if src_dict['Inf_11']:
            present_participle_forms = get_present_participle(src_dict)
            word_forms += present_participle_forms

        if src_dict['Inf_12']:
            past_participle_forms = get_past_participle(src_dict)
            word_forms += past_participle_forms

        if name.endswith(('шел', 'шелся')):
            title_word_form = TitleWordForm(name, word_forms[0].idf, info, '')
            return GroupWordForm(title_word_form, word_forms[1:])
        else:
            title_word_form = TitleWordForm(name, '.ГИ', info, '')
            return GroupWordForm(title_word_form, word_forms)
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
        src_dict['Inf_6'],
        src_dict['Inf_7'],
        src_dict['Inf_8'],
        src_dict['Inf_9'],
        src_dict['Inf_10'],
        src_dict['Inf_11'],
        src_dict['Inf_12'],
    ])))

    # Блокировка IV
    if src_dict['name'].endswith(('ся', 'сь')) and src_dict['Inf_1'] == 'пер':
        message = (f'{in_data_string}\n'
                   'Блокировка IV.\n'
                   'Возвратный глагол НЕ может быть переходным!')
        raise InputDataError(message)

    # Блокировка V
    if (
            src_dict['name'].endswith(('шел', 'шелся'))
            and any([
                src_dict['Inf_3'],
                src_dict['Inf_5'],
                src_dict['Inf_6'],
                src_dict['Inf_7'],
                src_dict['Inf_8'],
                src_dict['Inf_10'],
                src_dict['Inf_11'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка V.\n'
                   'Глаголы на -ШЕЛ(СЯ) НЕ образуют ничего, кроме форм:\n'
                   'прошедшего времени,\n'
                   'причастия прошедшего времени действительного,\n'
                   'деепричастия прошедшего времени.')
        raise InputDataError(message)

    # Блокировка VI
    if (
            (
                    src_dict['name'].endswith(('йти', 'йтись'))
                    or src_dict['name'] in ('грясти', 'идти', 'изыти')
            )
            and any([
                src_dict['Inf_4'],
                src_dict['Inf_9'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка VI.\n'
                   'Глаголы на -ЙТИ(СЬ) и глаголы ГРЯСТИ, ИДТИ, ИЗЫТИ '
                   'НЕ образуют формы:\n'
                   'прошедшего времени,\n'
                   'причастия прошедшего времени действительного.')
        raise InputDataError(message)

    # Блокировка VII
    if (
            src_dict['Inf_2'] == 'б'
            and any([
                src_dict['Inf_6'],
                src_dict['Inf_7'],
                src_dict['Inf_8'],
                src_dict['Inf_9'],
                src_dict['Inf_10'],
                src_dict['Inf_11'],
                src_dict['Inf_12'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка VII.\n'
                   'Безличные глаголы НЕ образуют ничего, кроме форм:\n'
                   'настоящего / будущего времени,\n'
                   'прошедшего времени,\n'
                   'повелительного наклонения.')
        raise InputDataError(message)

    # Блокировка VIII
    if (
            (
                    src_dict['Inf_0'] == 'нес'
                    or src_dict['name'] in ('заклать', 'попрать', 'услыхать')
            )
            and src_dict['Inf_6']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка VIII.\n'
                   'Глаголы несовершенного вида '
                   '(за исключением некоторых случаев) '
                   'и глаголы ЗАКЛАТЬ, ПОПРАТЬ, УСЛЫХАТЬ\n'
                   'НЕ образуют форму совместного действия.')
        raise InputDataError(message)

    # Блокировка IX
    if (
            src_dict['Inf_0'] == 'сов'
            and any([
                src_dict['Inf_7'],
                src_dict['Inf_8'],
                src_dict['Inf_11'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка IX.\n'
                   'Глаголы совершенного вида НЕ образуют формы:\n'
                   'причастия настоящего времени действительного,\n'
                   'причастия настоящего времени страдательного,\n'
                   'деепричастия настоящего времени.')
        raise InputDataError(message)

    # Блокировка X
    if (
            src_dict['name'].endswith(('ся', 'сь'))
            and any([
                src_dict['Inf_8'],
                src_dict['Inf_10'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка X.\n'
                   'Возвратные глаголы НЕ образуют страдательных причастий.')
        raise InputDataError(message)

    # Блокировка XI
    if (
            src_dict['Inf_1'] == 'неп'
            and any([
                src_dict['Inf_8'],
                src_dict['Inf_10'],
            ])
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка XI.\n'
                   'Непереходные глаголы НЕ образуют формы:\n'
                   'причастия настоящего времени страдательного '
                   '(за исключением некоторых случаев),\n'
                   'причастия прошедшего времени страдательного.')
        raise InputDataError(message)

    # Блокировка XII
    if (
            src_dict['Inf_0'] == 'нес'
            and any([
                src_dict['name'].endswith('оть'),

                src_dict['name'].endswith('сть')
                and not src_dict['name'].endswith('есть'),

                src_dict['name'].endswith('чь')
                and not src_dict['name'].endswith('влечь'),
            ])
            and src_dict['Inf_8']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка XII.\n'
                   'Причастие настоящего времени страдательное '
                   'НЕ образуют глаголы несовершенного вида на:\n'
                   '-ОТЬ,\n'
                   '-СТЬ (кроме ЕСТЬ),\n'
                   '-ЧЬ (кроме ВЛЕЧЬ).')
        raise InputDataError(message)

    # Блокировка XIII
    if (
            any([
                src_dict['name'].endswith('авать')
                and src_dict['name'] != 'исплавать'
                and src_dict['name'] != 'наплавать'
                and not src_dict['name'].endswith('хавать'),

                src_dict['name'].endswith('евать')
                and src_dict['name'][-6] in ('в', 'м', 'п', 'р', 'с', 'т', 'щ'),

                src_dict['name'].endswith((
                        'длевать',
                        'тлевать',
                        'одолевать',
                        'разевать',
                        'ивать',
                        'увать',
                        'ывать',
                )),

                src_dict['name'] == 'гневать',
            ])
            and src_dict['Inf_10']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка XIII.\n'
                   'Причастие прошедшего времени страдательное '
                   'НЕ образуют глаголы на\n'
                   '-АВАТЬ (кроме ИСПЛАВАТЬ, НАПЛАВАТЬ и на -ХАВАТЬ),\n'
                   '-ЕВАТЬ с предшествующей В, М, П, Р, С, Т, Щ,\n'
                   '-ДЛЕВАТЬ, -ТЛЕВАТЬ, -ОДОЛЕВАТЬ, -РАЗЕВАТЬ,\n'
                   '-ИВАТЬ,\n'
                   '-УВАТЬ,\n'
                   '-ЫВАТЬ\n'
                   'и глагол ГНЕВАТЬ.')
        raise InputDataError(message)

    # Блокировка XIV
    if (
            src_dict['Inf_0'] == 'нес'
            and any([
                src_dict['name'].endswith('водить')
                and src_dict['name'] != 'водить',

                src_dict['name'].endswith('возить')
                and src_dict['name'] != 'возить',

                src_dict['name'].endswith('носить')
                and src_dict['name'] != 'носить',

                src_dict['name'].endswith('ходить'),
            ])
            and src_dict['Inf_10']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка XIV.\n'
                   'Причастие прошедшего времени страдательное '
                   'НЕ образуют глаголы несовершенного вида на:\n'
                   '-ВОДИТЬ (кроме ВОДИТЬ),\n'
                   '-ВОЗИТЬ (кроме ВОЗИТЬ),\n'
                   '-НОСИТЬ (кроме НОСИТЬ),\n'
                   '-ХОДИТЬ.')
        raise InputDataError(message)

    # Блокировка XV
    if (
            any([
                src_dict['name'].endswith('нуть')
                and not src_dict['name'].endswith('тянуть'),

                src_dict['name'].endswith('нуться')
                and not src_dict['name'].endswith('тянуться'),
            ])
            and src_dict['Inf_11']
    ):
        message = (f'{in_data_string}\n'
                   'Блокировка XV.\n'
                   'Глаголы на -НУТЬ(СЯ) [кроме на -ТЯНУТЬ(СЯ)] '
                   'НЕ образуют деепричастие настоящего времени.')
        raise InputDataError(message)


def save_groups_to_bs():
    definitions = 'WordFormGen. Глаголы.txt'
    print(f'Настройки:')
    print(f'{definitions}\n')

    *in_verbs_list, out_verbs = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_verbs_list = in_verbs_list[:-1]

    print(f'Файлы с исходными данными:')
    for line in in_verbs_list:
        print(line)
    print()

    print('Для продолжения нажмите Enter')
    input()
    print(f'{"* " * 38}*\n')

    count = 0
    add_groups_to_bs_list = []
    add_groups_to_bg_list = []

    error_list = []

    for in_verbs in in_verbs_list:
        src_groups = get_long_dicts_from_csv_file(in_verbs)

        print(reminder_verbs)
        input()

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
        quit()

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list), out_verbs)
    print(f'Создано {count} групп словоформ')
    print(f'Создан файл "{out_verbs}"')

    add_to_bg = 'Добавить в БГ. Глаголы.txt'
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
# pyinstaller -F -i nouns/icon.ico verbs/FlexerVerbs.py
