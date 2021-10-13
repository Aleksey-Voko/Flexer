"""Обобщённо все части речи"""


from bs_lists.socket_bg import (get_replays_in_socket_duplicate,
                                save_multi_root_words)
from utils import (save_list_to_file, get_socket_word_form,
                   get_bs_title_word_form)


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
    save_list_to_file(words_with_exp_notes,
                      'Слова с пояснительными примечаниями БС.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с пояснительными примечаниями БС.txt')
    print(f'... сортировка ...')

    # Омонимы БС (ЗС групп и одиночки)
    homonyms = get_homonyms(word_forms_bases, _)
    save_list_to_file(homonyms, 'Омонимы БС (ЗС групп и одиночки).txt',
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
    Найти в БГ и поместить в предварительный список строки
    с многокорневыми словами, т.е. словами, у которых есть
    корневой индекс (кроме невидимок) с соблюдением следующих правил:
        1. строки приводятся полностью;
        2. уже вставленная строка не должна вставляться второй (и более!) раз!
    Учитывая пункты 1 и 2 Правил соотношения БГ и БС, найти в БС строки,
    соответствующие строкам из предварительно созданного списка.

    В случае, когда найденная строка в БС снабжена специальным примечанием,
    необходимо убедиться в идентичности этого специального примечания
    строке с ЗС подгруппы, в которой в БГ находится строка,
    соответствующая строке, найденной в БС.
    При этом этимологическое примечание, которое может быть в строке
    с ЗС подгруппы в БГ ИГНОРИРУЕТСЯ.
    """

    save_multi_root_words(word_forms_bases, socket_group_list)
    print(f'Создан документ: Многокорневые слова БГ.csv')
    print(f'... сортировка ...')

    print('... ждите ...')

    multi_root_bg_forms = []
    multi_root_bg_forms_with_sub_title = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            sub_title_form = sub_group.title_word_form
            src_sub_title_form = ' '.join(filter(
                None,
                [
                    sub_title_form.invisible,
                    sub_title_form.name,
                    sub_title_form.root_index,
                    sub_title_form.idf,
                    ' '.join(sub_title_form.info),
                    sub_title_form.note,
                    sub_title_form.spec_note,
                ]
            ))
            for socket_form in sub_group.socket_word_forms:
                root_index = socket_form.root_index
                if root_index and not socket_form.invisible:
                    multi_root_bg_forms.append(
                        ' '.join(filter(
                            None,
                            [
                                socket_form.name,
                                socket_form.idf,
                                ' '.join(socket_form.info),
                                socket_form.note.replace('* ', ''),
                            ]
                        ))
                    )

                    multi_root_bg_forms_with_sub_title.append(
                        ' '.join(filter(
                            None,
                            [
                                socket_form.name,
                                socket_form.idf,
                                ' '.join(socket_form.info),
                                ' '.join(['<', src_sub_title_form]),
                            ]
                        ))
                    )

    word_forms = []

    for group_word_form in word_forms_bases:
        title_form = group_word_form.title_word_form
        src_title_form = ' '.join(filter(
            None,
            [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.* ', ''),
            ]))
        if '<' not in title_form.note.replace('.* ', ''):
            if src_title_form in multi_root_bg_forms:
                word_forms.append(str(title_form))
        else:
            if src_title_form in multi_root_bg_forms_with_sub_title:
                word_forms.append(str(title_form))

    word_forms = list(sorted(
        word_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    ))

    return word_forms


# Повторы в пределах гнезда. 1 раз в БС.txt
def get_repeats_w_socket_1_in_bs(word_forms_bases, socket_group_list) -> list:
    """
    Создать документы Повторы в гнезде. Повторяющиеся строки.txt

    Найти в БС строки, соответствующие строкам из документа
    Повторы в гнезде. Повторяющиеся строки.txt .

    Убедиться, что найденные строки отсутствуют в документе
    Омонимы БС (ЗС групп и одиночки).txt .

    Создать документ Повторы в пределах гнезда. 1 раз в БС.txt
    и вставить в него найденные строки.
    """

    # Повторы в гнезде. Повторяющиеся строки.txt
    socket_duplicate = get_replays_in_socket_duplicate(
        word_forms_bases, socket_group_list)

    save_list_to_file(
        socket_duplicate, 'Повторы в гнезде. Повторяющиеся строки.txt',
        encoding='cp1251')

    print(f'Создан документ: Повторы в гнезде. Повторяющиеся строки.txt')
    print(f'... сортировка ...')

    socket_word_forms = [get_socket_word_form(x) for x in socket_duplicate]
    socket_str_forms = [
        ' '.join(filter(
            None,
            [
                x.name,
                x.idf,
                ' '.join(x.info),
                x.note.replace('.*', '').strip()
            ]))
        for x in socket_word_forms
    ]

    # Омонимы БС (ЗС групп и одиночки).txt
    # homonyms = get_homonyms(word_forms_bases, socket_group_list)
    #
    # save_list_to_file(
    #     homonyms, 'Омонимы БС (ЗС групп и одиночки).txt', encoding='cp1251')
    #
    # print(f'Создан документ: Омонимы БС (ЗС групп и одиночки).txt')
    # print(f'... сортировка ...')
    #
    # homonyms_word_forms = [get_bs_title_word_form(x) for x in homonyms]
    # homonyms_str_forms = [
    #     ' '.join(filter(
    #         None,
    #         [
    #             x.name,
    #             x.idf,
    #             ' '.join(x.info),
    #             x.note.replace('.*', '').strip()
    #         ]))
    #     for x in homonyms_word_forms
    # ]

    # Повторы в пределах гнезда. 1 раз в БС.txt
    word_forms = []

    for group in word_forms_bases:
        title_form = group.title_word_form
        title_str_form = ' '.join(filter(
            None, [
                title_form.name,
                title_form.idf,
                ' '.join(title_form.info),
                title_form.note.replace('.*', '').strip()
            ]))

        if title_str_form in socket_str_forms:
            # if title_str_form in homonyms_str_forms:
            #     print(
            #         'В документе Омонимы БС (ЗС групп и одиночки).txt\n'
            #         f"обнаружена строка: '{title_str_form}'"
            #     )
            #     print('Для выхода нажмите Enter')
            #     input()
            #     sys.exit()
            # else:
            #     word_forms.append(str(title_form))
            word_forms.append(str(title_form))

    return word_forms


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


def is_all_root_indices(v_keys, index: dict) -> bool:
    # в каждой строке корневой индекс
    lst = [
        [
            x[1]
            for x in
            index[get_bs_title_word_form(y).name]
        ] for y in v_keys
    ]

    lst = [x for y in lst for x in y]

    return all(lst)


def is_in_one_socket_bg(v_keys, index: dict) -> bool:
    # в одном гнезде хотя бы 1 раз
    lst = [
        [x[0] for x in index[y]]
        for y in
        [get_bs_title_word_form(z).name for z in v_keys]
    ]

    lst = [x for y in lst for x in y]

    return len(set(lst)) < len(lst)


def is_all_in_one_socket_bg(v_keys, index: dict) -> bool:
    # ... соответствуют строки, находящиеся в одном гнезде
    lst = [
        [x[0] for x in index[y]]
        for y in
        [get_bs_title_word_form(z).name for z in v_keys]
    ]

    lst = [x for y in lst for x in y]

    return len(set(lst)) != 1


# Омонимичные формы БС.txt
def get_homonymous_forms(word_forms_bases, socket_group_list) -> list:
    """
    1. Найти в БС строки с омонимичными формами, т.е. одинаковыми словами,
    находящимися в разных группах.
    Создать документ и вставить в него найденные строки с омонимичными формами,
    указывая строки с ЗС группы, в которой находится каждая такая строка,
    и объединяя строки с одинаковыми омонимичными формами в "абзацы".

    Примечание 1. Омонимичной формой может быть любая словоформа, в том числе
        ЗС группы или одиночка.

    Примечание 2. Количество омонимичных форм не ограничено.

    Примечание 3. Перед строкой с ЗС группы ставится "!".

    Примечание 4. "Абзацы" со строками с омонимичными формами с указанием
        строк с ЗС групп, в которых они находятся, располагаются
        в соответствии с алфавитным порядком омонимичных форм.

    2. Удалить из созданного согласно п. 1 документа "абзацы",
    в которых все ЗС групп являются многокорневыми словами,
    т.е. "абзацы", в которых всем строкам с ЗС групп (из БС)
    в БГ соответствуют строки, находящиеся в одном гнезде хотя бы 1 раз
    и при этом в каждой такой (соответствующей) строке имеется корневой индекс.
    (При проверке на нахождение строк в БГ в одном гнезде учитывать
    пункты 1 - 4 Правил соотношения БГ и БС).

    3. Далее удалить "абзацы", в которых всем строкам с ЗС групп (из БС)
    в БГ соответствуют строки, находящиеся в одном гнезде.
    (При проверке на нахождение строк в БГ в одном гнезде учитывать
    пункты 1 - 4 Правил соотношения БГ и БС).
    """

    print('... ждите ...')

    bs_index = {}

    # Имена словоформ, находящиеся в строках из разных групп.
    # bs_index = {
    #     'title_form.name': {
    #         'str(title_form)': ['str(title_form)',...],
    #         'str(title_form)': ['str(title_form)',...],
    #     }
    #     'word_form.name': {
    #         'str(title_form)': ['str(word_form)',...],
    #         'str(title_form)': ['str(word_form)',...],
    #     }
    # }

    for group in word_forms_bases:
        title_form = group.title_word_form
        bs_index.setdefault(title_form.name, {})
        bs_index[title_form.name].setdefault(
            str(title_form), []).append(str(title_form))

        for word_form in group.word_forms:
            bs_index.setdefault(word_form.name, {})
            bs_index[word_form.name].setdefault(
                str(title_form), []).append(str(word_form))

    bs_index = {k: v for k, v in bs_index.items() if len(v) > 1}

    bg_index = {}

    # Имена словоформ, заглавные слова которых находяться в разных группах
    # bg_index = {
    #     'socket_form.name': [
    #         ('socket_title_form', 'socket_form.root_index'),
    #         ('socket_title_form', 'socket_form.root_index'),
    #     ],
    #     'socket_form.name': [
    #         ('socket_title_form', 'socket_form.root_index'),
    #         ('socket_title_form', 'socket_form.root_index'),
    #     ],
    # }

    for socket_group in socket_group_list:
        socket_title_form = socket_group.title_word_form
        for sub_group in socket_group.sub_groups:
            for socket_form in sub_group.socket_word_forms:
                bg_index.setdefault(socket_form.name, [])
                bg_index[socket_form.name].append(
                    (
                        str(socket_title_form),
                        socket_form.root_index,
                    )
                )

    bs_index = {
        k: v for k, v
        in bs_index.items()
        if not (
                is_all_root_indices(v.keys(), bg_index)
                and
                is_in_one_socket_bg(v.keys(), bg_index)
        )
    }

    bs_index = {
        k: v for k, v
        in bs_index.items()
        if is_all_in_one_socket_bg(v.keys(), bg_index)
    }

    word_forms = []

    for title_form_name in sorted(bs_index.keys()):
        for src_title_word, word_form_list in bs_index[title_form_name].items():
            word_forms.append(f'!{src_title_word}')
            for word_form in word_form_list:
                word_forms.append(word_form)
        word_forms.append('')

    return word_forms


# Обычные слова БС.txt
def get_common_words_bs(word_forms_bases, socket_group_list) -> list:
    """
    Создать документ Снимок БС.txt .
    Удалить из него строки из документов:
        Многокорневые слова БС.txt ;
        Повторы в пределах гнезда. 1 раз в БС.txt ;
        Омонимы БС (ЗС групп и одиночки).txt .

    Сохранить получившийся документ и переименовать его в Обычные слова БС.txt .
    Примечание. В 3 указанных документах могут быть одинаковые строки.
    """

    # Снимок БС.txt
    bs_snapshot = get_bs_snapshot(word_forms_bases, socket_group_list)

    save_list_to_file(
        bs_snapshot, 'Снимок БС.txt', encoding='cp1251')

    print(f'Создан документ: Снимок БС.txt')
    print(f'... сортировка ...')

    # Многокорневые слова БС.txt
    multi_root_words = get_multi_root_words(
        word_forms_bases, socket_group_list)

    save_list_to_file(
        multi_root_words, 'Многокорневые слова БС.txt', encoding='cp1251')

    print(f'Создан документ: Многокорневые слова БС.txt')
    print(f'... сортировка ...')

    # Повторы в пределах гнезда. 1 раз в БС.txt
    repeats_w_socket_1_in_bs = get_repeats_w_socket_1_in_bs(
        word_forms_bases, socket_group_list)

    save_list_to_file(
        repeats_w_socket_1_in_bs, 'Повторы в пределах гнезда. 1 раз в БС.txt',
        encoding='cp1251')

    print(f'Создан документ: Повторы в пределах гнезда. 1 раз в БС.txt')
    print(f'... сортировка ...')

    # Омонимы БС (ЗС групп и одиночки).txt
    homonyms = get_homonyms(word_forms_bases, socket_group_list)

    save_list_to_file(
        homonyms, 'Омонимы БС (ЗС групп и одиночки).txt', encoding='cp1251')

    print(f'Создан документ: Омонимы БС (ЗС групп и одиночки).txt')
    print(f'... сортировка ...')

    not_ordinary = multi_root_words + repeats_w_socket_1_in_bs + homonyms

    word_forms = list(sorted(
        list(set(bs_snapshot) - set(not_ordinary)),
        key=lambda x: x.replace('*', '').lower().strip()
    ))

    return word_forms


# Снимок БС.txt
def get_bs_snapshot(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками.
    Создать документ Снимок БС.txt и вставить в него найденные строки,
    располагая их друг за другом, без пробелов между строками.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
    ]
    return word_forms
