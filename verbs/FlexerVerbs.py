from pathlib import Path
from pprint import pprint

from utils import (get_string_list_from_file, save_bs_dicts_to_txt,
                   get_verbs_dicts_from_csv_file)
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


def save_groups_to_bs():
    definitions = 'definitionsFlexer.txt'

    print('*' * 3)
    print(f'Настройки:')
    print(definitions + '\n')

    *in_verbs_list, out_verbs = get_string_list_from_file(
        definitions, encoding='cp1251')
    in_verbs_list = in_verbs_list[:-1]

    print('*' * 3)
    print(f'Файлы с исходными данными:')
    pprint(in_verbs_list)
    print()

    count = 0
    add_groups_to_bs_list = []

    for in_verbs in in_verbs_list:
        src_groups = get_verbs_dicts_from_csv_file(in_verbs)
        for src_dict in src_groups:
            add_groups_to_bs_list.append(get_group_word_form(src_dict))
            count += 1

    save_bs_dicts_to_txt(sorted(add_groups_to_bs_list), out_verbs)
    print('*' * 3)
    print(f'Создано {count} групп словоформ\n')

    print('*' * 3)
    print(f'Файл с результатами "{out_verbs}" сохранён в текущей директории:')
    print(Path().resolve())
    print()

    print('*' * 3)
    print('Для выхода нажмите любую Enter')
    input()


if __name__ == '__main__':
    save_groups_to_bs()

# compilation
# pyinstaller -F verbs/FlexerVerbs.py
