"""Обобщённо все части речи"""

from bs_lists.socket_bg import save_multi_root_words
from utils import (save_list_to_file, get_dicts_from_csv_file,
                   get_socket_word_form)


# Одиночки.txt
def get_loners(word_forms_bases, _) -> list:
    """
    Найти в БС строки с одиночками.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if not group.word_forms
    ]
    return word_forms


# Слова с дефисом.txt
def get_words_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками, в которых
    имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if '-' in group.title_word_form.name
    ]
    return word_forms


# Слова с латиницей.txt
def get_latin_words(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками, в которых
    имеется хотя бы 1 латинская буква.
    """

    from string import ascii_letters
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if any(map(lambda x: x in ascii_letters, group.title_word_form.name))
    ]
    return word_forms


# Слова с пояснительными примечаниями БС.txt
def get_words_with_exp_notes(word_forms_bases, _) -> list:
    """
    Найти в БС строки с пояснительными примечаниями, т.е. строки,
    в которых имеется комбинация символов .* (но не .* <)
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if '.*' in group.title_word_form.note
           and '.* <' not in group.title_word_form.note
    ]
    return word_forms


# Пояснительные примечания (без омонимов).txt
def get_words_with_exp_notes_no_homonyms(word_forms_bases, _) -> list:
    """
    Создать документы Слова с пояснительными примечаниями БС.txt
    и Омонимы БС (ЗС групп и одиночки).txt .
    Найти в документе Слова с пояснительными примечаниями БС.txt строки,
    отсутствующие в документе Омонимы БС (ЗС групп и одиночки).txt .
    """

    # Слова с пояснительными примечаниями БС
    words_with_exp_notes = get_words_with_exp_notes(word_forms_bases, _)
    save_list_to_file(sorted(words_with_exp_notes),
                      'Слова с пояснительными примечаниями БС.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с пояснительными примечаниями БС.txt')
    print(f'... сортировка ...')

    # Омонимы БС (ЗС групп и одиночки)
    homonyms = get_homonyms(word_forms_bases, _)
    save_list_to_file(sorted(homonyms),
                      'Омонимы БС (ЗС групп и одиночки).txt',
                      encoding='cp1251')
    print(f'Создан документ: Омонимы БС (ЗС групп и одиночки).txt')
    print(f'... сортировка ...')

    word_forms = [x for x in words_with_exp_notes if x not in homonyms]
    return word_forms


# Слова со специальными примечаниями.txt
def get_words_with_spec_notes(word_forms_bases, _) -> list:
    """
    Найти в БС строки со специальными примечаниями, т.е. строки,
    в которых имеется комбинация символов .* <
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if '.* <' in group.title_word_form.note
    ]
    return word_forms


# Многокорневые слова БС.txt
def get_multi_root_words(word_forms_bases, socket_group_list) -> list:
    """
    Создать документ Многокорневые слова БГ.csv .
    Учитывая пункты 1 и 2 Правил соотношения БГ и БС, найти в БС строки,
    соответствующие строкам из документа Многокорневые слова БГ.csv .
    """

    save_multi_root_words(word_forms_bases, socket_group_list)
    print(f'Создан документ: Многокорневые слова БГ.csv')
    print(f'... сортировка ...')

    multi_root_words = get_dicts_from_csv_file('Многокорневые слова БГ.csv')

    multi_root_bg_forms = []

    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word)[1:]:
            if multi_root_word[root_index_key]:
                socket_form = get_socket_word_form(
                    multi_root_word[root_index_key]
                )
                multi_root_bg_forms.append(
                    ' '.join(filter(
                        None,
                        [
                            socket_form.name,
                            socket_form.idf,
                            ' '.join(socket_form.info),
                            socket_form.note.replace('* ', ''),
                        ])))

    word_forms = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form
        src_title_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                (title_form.note.replace('.* ', '')
                 if '<' not in title_form.note else None),
            ]))
        if src_title_form in multi_root_bg_forms:
            word_forms.append(str(title_form))

    word_forms = sorted(
        word_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    )

    return word_forms


# ========================
# Омонимы БС (ЗС групп и одиночки).txt
def get_homonyms(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками,
    в которых имеются одинаковые слова.
    """

    from collections import Counter
    title_form_names = [group.title_word_form.name
                        for group in word_forms_bases]
    homonyms = [k for k, v in Counter(title_form_names).items() if v > 1]

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.name in homonyms
    ]
    return word_forms
