from pathlib import Path
from pprint import pprint

from rem import reminder
from utils import (get_string_list_from_file, save_bs_dicts_to_txt,
                   get_verbs_dicts_from_csv_file, save_list_to_file)
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

        title_word_form = TitleWordForm(name, '.ГИ', info, '')

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

        return GroupWordForm(title_word_form, word_forms)
    else:
        title_word_form = TitleWordForm(name, '', [], '')
        return GroupWordForm(title_word_form, [])


def save_groups_to_bs():
    definitions = 'WordFormGen. Глаголы.txt'
    print(f'Настройки:')
    print(f'"{definitions}"\n')

    *in_verbs_list, out_verbs = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_verbs_list = in_verbs_list[:-1]

    print(f'Файлы с исходными данными:')
    pprint(in_verbs_list)
    print()

    print('Для продолжения нажмите Enter')
    input()
    print(f'{"#" * 30}\n')

    count = 0
    add_groups_to_bs_list = []
    add_groups_to_bg_list = []

    for in_verbs in in_verbs_list:
        src_groups = get_verbs_dicts_from_csv_file(in_verbs)
        for src_dict in src_groups:
            group_word_form = get_group_word_form(src_dict)
            add_groups_to_bs_list.append(group_word_form)
            add_groups_to_bg_list.append(
                group_word_form.title_word_form.bg_form)
            count += 1

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
