"""База гнёзд БГ"""


from collections import Counter

import pandas as pd
import numpy as np

from utils import (save_list_to_file, get_dicts_from_csv_file,
                   get_socket_word_form)


# Невидимки.txt
def get_invisible(_, socket_group_list) -> list:
    """
    Найти в БГ строки с невидимками, т.е. строки, начинающиеся с символа * ,
    после которого ЧЕРЕЗ ПРОБЕЛ указано слово.
    Напр.
    * аван
    * arm
    * 5 * <= five
    """

    word_forms = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if word_form.invisible:
                    word_forms.append(str(word_form))

    return word_forms


# Слова с пояснительными примечаниями БГ.txt
def get_socket_with_exp_notes(_, socket_group_list) -> list:
    """
    Найти в БГ строки с пояснительными примечаниями, т.е. строки, в которых
    после спец. информации (если это не строка с одиночкой или невидимкой) или
    после слова (если это строка с одиночкой или невидимкой) или
    после корневого индекса (если это строка с одиночкой, являющимся
    многокорневым словом, или невидимкой, являющимся многокорневым словом)
    указан символ * , после которого идут буквы
    (непосредственно само пояснительное примечание).
    Примечание. Строки с многокорневыми словами
    (т.е. слово имеет корневой индекс) вставляются в документ 1 раз.
    """

    word_forms = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if word_form.note and str(word_form) not in word_forms:
                    word_forms.append(str(word_form))

    return word_forms


# Слова с этимологическими примечаниями.txt
def get_socket_with_etml_notes(_, socket_group_list) -> list:
    """
    Найти в БГ строки с этимологическими примечаниями, т.е. строки,
    в которых имеются следующие комбинации символов: <= / *? ,
    а также строки, оканчивающиеся комбинацией символов *!
    Примечание. Одинаковые строки с многокорневыми словами
    (т.е. в строке имеется также корневой индекс),
    в которых имеются следующие комбинации символов: <= / *? ,
    а также одинаковые строки с многокорневыми словами,
    оканчивающиеся комбинацией символов *! , вставляются в документ 1 раз.
    """

    word_forms = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if word_form.etml_note and str(word_form) not in word_forms:
                    word_forms.append(str(word_form))

    return word_forms


# Этимология неизвестна.txt
def get_unknown_etymology(_, socket_group_list) -> list:
    """
    Создать документ Слова с этимологическими примечаниями.txt
    и найти в нём строки, оканчивающиеся комбинацией символов *?
    """

    # Слова с этимологическими примечаниями.txt
    socket_with_etml_notes = get_socket_with_etml_notes(_, socket_group_list)
    save_list_to_file(socket_with_etml_notes,
                      'Слова с этимологическими примечаниями.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с этимологическими примечаниями.txt')
    print(f'... сортировка ...')

    word_forms = [
        x for x in socket_with_etml_notes
        if x.endswith('*?')
    ]

    return word_forms


# Нет общепринятой этимологии.txt
def get_no_accepted_etymology(_, socket_group_list) -> list:
    """
    Создать документ Слова с этимологическими примечаниями.txt
    и найти в нём строки, оканчивающиеся комбинацией символов *??
    """

    # Слова с этимологическими примечаниями.txt
    socket_with_etml_notes = get_socket_with_etml_notes(_, socket_group_list)
    save_list_to_file(socket_with_etml_notes,
                      'Слова с этимологическими примечаниями.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с этимологическими примечаниями.txt')
    print(f'... сортировка ...')

    word_forms = [
        x for x in socket_with_etml_notes
        if x.endswith('*??')
    ]

    return word_forms


# Образовано от.txt
def get_formed_from(_, socket_group_list) -> list:
    """
    Создать документ Слова с этимологическими примечаниями.txt
    и найти в нём строки, в которых имеется символ * ,
    после которого через пробел указана комбинация символов <= (* <=)
    """

    # Слова с этимологическими примечаниями.txt
    socket_with_etml_notes = get_socket_with_etml_notes(_, socket_group_list)
    save_list_to_file(socket_with_etml_notes,
                      'Слова с этимологическими примечаниями.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с этимологическими примечаниями.txt')
    print(f'... сортировка ...')

    word_forms = [
        x for x in socket_with_etml_notes
        if x.find('* <=') != -1
    ]

    return word_forms


# Этимология игнорируется.txt
def get_etymology_ignored(_, socket_group_list) -> list:
    """
    Создать документ Слова с этимологическими примечаниями.txt
    и найти в нём строки, в которых имеется комбинация символов |<=
    """

    # Слова с этимологическими примечаниями.txt
    socket_with_etml_notes = get_socket_with_etml_notes(_, socket_group_list)
    save_list_to_file(socket_with_etml_notes,
                      'Слова с этимологическими примечаниями.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с этимологическими примечаниями.txt')
    print(f'... сортировка ...')

    word_forms = [
        x for x in socket_with_etml_notes
        if x.find('|<=') != -1
    ]

    return word_forms


# Образовано под влиянием.txt
def get_under_the_influence(_, socket_group_list) -> list:
    """
    Создать документ Слова с этимологическими примечаниями.txt
    и найти в нём строки, в которых имеется комбинация символов ++
    """

    # Слова с этимологическими примечаниями.txt
    socket_with_etml_notes = get_socket_with_etml_notes(_, socket_group_list)
    save_list_to_file(socket_with_etml_notes,
                      'Слова с этимологическими примечаниями.txt',
                      encoding='cp1251')
    print(f'Создан документ: Слова с этимологическими примечаниями.txt')
    print(f'... сортировка ...')

    word_forms = [
        x for x in socket_with_etml_notes
        if x.find('++') != -1
    ]

    return word_forms


# Этимология примечательна.txt
def get_a_noteworthy_etymology(_, socket_group_list) -> list:
    """
    Найти в БГ строки, оканчивающиеся комбинацией символов *!
    Создать документ Этимология примечательна.txt и вставить в него найденные
    строки с указанием строк с ЗС группы, в которой находится такая строка,
    и с соблюдением алфавитного порядка ЗС групп.
    Напр.

        блуза .СеИ неод жII1 мнII6
        луза .СеИ неод жII1 мнII6 *!

        вино .СеИ неод сI5 мнIV6
        винил .СеИ неод мI1 мнII1 *!
    """

    index = {}

    for socket_group in socket_group_list:
        title_word_form = socket_group.title_word_form
        for word_form in socket_group.socket_word_forms:
            if str(word_form).endswith('*!'):
                index.setdefault(str(title_word_form), [])
                index[str(title_word_form)].append(str(word_form))

    word_forms = []

    for key in sorted(index.keys()):
        word_forms.append(key)
        for word_form in index[key]:
            word_forms.append(word_form)
        word_forms.append('')

    return word_forms


# Многокорневые слова БГ.csv
def save_multi_root_words(_, socket_group_list):
    """
    Найти в БГ строки с многокорневыми словами, т.е. словами, у которых есть
    корневой индекс (кроме невидимок).

    Создать документ Многокорневые слова БГ.csv и заполнить его строками
    с найденными многокорневыми словами с соблюдением следующих правил:
        1. строки приводятся полностью;
        2. строки вставляются в тот или иной столбец в зависимости
            от корневого индекса;
        3. уже вставленная строка не должна вставляться второй (и более!) раз!
            Другими словами, в документе Многокорневые слова БГ.csv не должно
            быть повторов одинаковых строк (напр. строка:
                автобус 3* .СеИ неод мI1 мнII1 * auto(mobile) (omni)bus
            вставляется 1 раз несмотря на то, что в базе она
            встречается 2 раза, или напр. строка:
                ЮНЕСКО 6
            вставляется 1 раз несмотря на то, что в базе
            она встречается 6 раз).

    По завершении заполнения документа Многокорневые слова БГ.csv
    вставленные строки в столбцах расположить в соответствии
    с алфавитным порядком слов,
    а сами столбцы - в следующем порядке:
    2 2! 2* 3 3! 3* 3** 4 4! 4* 4** 5 5! 5* 5** 6 6! 6* 6** 7 7! 7* 7**
    """
    root_index_ds = {
        '2': [],
        '2!': [],
        '2*': [],
        '3': [],
        '3!': [],
        '3*': [],
        '3**': [],
        '4': [],
        '4!': [],
        '4*': [],
        '4**': [],
        '5': [],
        '5!': [],
        '5*': [],
        '5**': [],
        '6': [],
        '6!': [],
        '6*': [],
        '6**': [],
        '7': [],
        '7!': [],
        '7*': [],
        '7**': [],
    }

    for socket_group in socket_group_list:
        for socket_word_form in socket_group.socket_word_forms:
            root_index = socket_word_form.root_index
            if root_index and not socket_word_form.invisible:
                root_index_ds[root_index].append(str(socket_word_form))

    for k in root_index_ds:
        # noinspection PyUnresolvedReferences
        root_index_ds[k] = sorted(list(
            set(root_index_ds[k])),
            key=lambda x: x.replace('*', '').lower().strip()
        )

    ds = []
    for k in root_index_ds:
        for word_form in root_index_ds[k]:
            ds.append({
                'root_index': k,
                'word_form': word_form,
            })

    df = pd.DataFrame(ds)
    res_df = (df
              .assign(idx=df.groupby("root_index").cumcount())
              .pivot_table(index="idx", columns="root_index",
                           values="word_form", aggfunc="first"))

    for col in res_df.columns:
        res_df[col] = res_df[col].replace(np.nan, '\uFFFC')
        res_df[col] = sorted(res_df[col],
                             key=lambda x: x.replace('*', '').lower())
        res_df[col] = res_df[col].replace('\uFFFC', np.nan)

    # noinspection PyTypeChecker
    res_df.to_csv('Многокорневые слова БГ.csv', index=False, sep=';',
                  encoding='cp1251')


# Многокорневые слова БГ - омонимы.txt
def get_multi_root_words_homonyms(word_forms_bases, socket_group_list) -> list:
    """
    Создать документ Многокорневые слова БГ.csv
    и найти в нём строки с одинаковыми словами.
    """

    save_multi_root_words(word_forms_bases, socket_group_list)
    print(f'Создан документ: Многокорневые слова БГ.csv')
    print(f'... сортировка ...')

    multi_root_words = get_dicts_from_csv_file('Многокорневые слова БГ.csv')

    index = {}

    for multi_root_word in multi_root_words:
        for root_index_key in multi_root_word:
            if multi_root_word[root_index_key]:
                socket_form = get_socket_word_form(
                    multi_root_word[root_index_key]
                )
                index.setdefault(socket_form.name, [])
                index[socket_form.name].append(str(socket_form))

    index = {k: v for k, v in index.items() if len(v) > 1}

    word_forms = []

    for key in sorted(index.keys()):
        for socket_form in index[key]:
            word_forms.append(socket_form)

    word_forms = sorted(
        word_forms,
        key=lambda x: x.replace('*', '').lower().strip()
    )

    return word_forms


# Повторы в пределах гнезда.txt
def get_repeats_within_a_socket(_, socket_group_list) -> list:
    """
    Найти строки со словами, повторяющимися в пределах одной и той же
    группы (кроме невидимок).
    Создать документ Повторы в пределах гнезда.txt
    и вставить в него строки (полностью),
    в которых обнаружились повторяющиеся слова, указывая строки
    с ЗС группы и ЗС подгруппы и соблюдая следующие правила:
        1. Перед строкой с ЗС подгруппы ставится "!".
    2. Строка с ЗС подгруппы и строка с ЗС группы могут совпадать.
        Строка с повторяющимся словом и строка с ЗС подгруппы могут совпадать.
        Строка с повторяющимся словом, строка с ЗС подгруппы и строка
        с ЗС группы могут совпадать.
    3. ЗС групп располагаются в алфавитном порядке,
        ЗС подгрупп - в том порядке, в котором они находятся в базе.
    """

    replays_in_groups = []

    for socket_group in socket_group_list:
        socket_word_forms = socket_group.socket_word_forms
        socket_word_forms = [x for x in socket_word_forms if not x.invisible]
        socket_names = [x.name for x in socket_word_forms]
        replays_names = sorted(list(set(
            [x for x in socket_names if socket_names.count(x) > 1]
        )))

        if replays_names:
            replays_in_groups.append(str(socket_group.socket_word_forms[0]))
            for sub_group in socket_group.sub_groups:
                flag = True
                for word_form in sub_group.socket_word_forms:
                    if word_form.name in replays_names:
                        if flag:
                            replays_in_groups.append(' '.join([
                                '!',
                                str(sub_group.title_word_form),
                            ]))
                            flag = False
                        replays_in_groups.append(str(word_form))

            replays_in_groups.append('')

    return replays_in_groups


# Повторы в гнезде - многокорневые слова.txt
def get_replays_in_groups(_, socket_group_list) -> list:
    """
    Найти в БГ строки со словами, имеющими корневой индекс и повторяющимися
    в пределах одной и той же группы (кроме невидимок).
    Создать документ Повторы в гнезде - многокорневые слова.txt
    и вставить в него строки (полностью), в которых обнаружились повторяющиеся
    слова, указывая строки с ЗС группы и ЗС подгруппы и
    соблюдая следующие правила:
        1. Перед строкой с ЗС подгруппы ставится "!".
        2. Строка с ЗС подгруппы и строка с ЗС группы могут совпадать.
            Строка с повторяющимся словом и строка с ЗС подгруппы
            могут совпадать.
            Строка с повторяющимся словом, строка с ЗС подгруппы и
            строка с ЗС группы могут совпадать.
        3. ЗС групп располагаются в алфавитном порядке,
            ЗС подгрупп - в том порядке, в котором они находятся в базе.
    """

    replays_in_groups = []

    for socket_group in socket_group_list:
        socket_word_forms = socket_group.socket_word_forms
        socket_word_forms = [
            x for x in socket_word_forms
            if not x.invisible and x.root_index
        ]
        socket_names = [x.name for x in socket_word_forms]

        replays_names = sorted(list(set(
            [x for x in socket_names if socket_names.count(x) > 1]
        )))

        if replays_names:
            replays_in_groups.append(str(socket_group.socket_word_forms[0]))
            for sub_group in socket_group.sub_groups:
                flag = True
                for word_form in sub_group.socket_word_forms:
                    if word_form.name in replays_names:
                        if flag:
                            replays_in_groups.append(' '.join([
                                '!',
                                str(sub_group.title_word_form),
                            ]))
                            flag = False
                        replays_in_groups.append(str(word_form))

            replays_in_groups.append('')

    return replays_in_groups


# Повторы в гнезде. Повторяющиеся строки.txt
def get_repeats_within_a_socket_duplicate(_, socket_group_list) -> list:
    """
    Создать документ Повторы в пределах гнезда.txt .
    Удалить из него строки с ЗС групп, с ЗС подгрупп
    и с многокорневыми словами.
    Найти среди оставшихся строк одинаковые строки.
    Создать документ Повторы в гнезде. Повторяющиеся строки.txt ,
    вставить в него найденные одинаковые строки
    с соблюдением алфавитного порядка слов.
    Удалить повторы строк.
    Сохранить документ Повторы в гнезде. Повторяющиеся строки.txt .
    """

    # Повторы в пределах гнезда.txt
    replays_in_socket = get_repeats_within_a_socket(_, socket_group_list)
    save_list_to_file(replays_in_socket, 'Повторы в пределах гнезда.txt',
                      encoding='cp1251')
    print(f'Создан документ: Повторы в пределах гнезда.txt')
    print(f'... сортировка ...')

    socket_duplicate = [
        x for x, count in Counter(replays_in_socket).items()
        if (
                count > 1
                and x
                and not x.startswith(('*', '!'))
                and not get_socket_word_form(x).root_index
        )
    ]

    socket_duplicate = sorted(
        list(set(socket_duplicate)),
        key=lambda x: x.replace('*', '').lower().strip()
    )

    return socket_duplicate


# Повторы в гнезде. Уникальные строки.txt
def get_repeats_within_a_socket_unique(_, socket_group_list) -> list:
    """
    Создать документ Повторы в пределах гнезда.txt .
    Удалить из него строки с ЗС групп и строки с ЗС подгрупп.
    Найти среди оставшихся строк уникальные строки.
    Расположить их в соответствии с алфавитным порядком слов.
    """

    replays_in_groups = []
    replays_in_groups_unique = []

    for socket_group in socket_group_list:
        socket_word_forms = socket_group.socket_word_forms
        socket_word_forms = [x for x in socket_word_forms if not x.invisible]
        socket_names = [x.name for x in socket_word_forms]
        replays_names = sorted(list(set(
            [x for x in socket_names if socket_names.count(x) > 1]
        )))

        if replays_names:
            replays_in_groups.append(str(socket_group.socket_word_forms[0]))
            for sub_group in socket_group.sub_groups:
                flag = True
                for word_form in sub_group.socket_word_forms:
                    if word_form.name in replays_names:
                        if flag:
                            replays_in_groups.append(' '.join([
                                '!',
                                str(sub_group.title_word_form),
                            ]))
                            flag = False
                        replays_in_groups.append(str(word_form))
                        replays_in_groups_unique.append(str(word_form))

            replays_in_groups.append('')

    save_list_to_file(replays_in_groups, 'Повторы в пределах гнезда.txt',
                      encoding='cp1251')
    print(f'Создан документ: Повторы в пределах гнезда.txt')
    print(f'... сортировка ...')

    replays_in_groups_unique = sorted(
        list(set(replays_in_groups_unique)),
        key=lambda x: x.replace('*', '').lower()
    )

    return replays_in_groups_unique


# Повторы в пределах гнезда. Строки.txt


# Омонимы БГ.txt
def get_homonyms_bg(_, socket_group_list) -> list:
    """
    Найти в БГ строки с омонимами, т.е. с одинаковыми словами,
    находящимися в разных группах (кроме невидимок и кроме многокорневых слов).
    Создать документ Омонимы БГ.txt и вставить в него найденные строки с
    соблюдением алфавитного порядка слов и с соблюдением следующего правила:
        если омоним является ЗС подгруппы, то просто полностью указывается
            строка с омонимом;
        если же омоним не является ЗС подгруппы, то после строки с омонимом
            ставится символ < и затем указывается строка с ЗС подгруппы,
            в которой находится данный омоним.
    """

    socket_names = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    socket_names.append(
                        word_form.name.replace('*', '').strip()
                    )

    socket_names = [x for x, y in Counter(socket_names).items() if y > 1]
    socket_names = sorted(list(set(socket_names)))

    homonyms = []

    for socket_group in socket_group_list:
        group_names = [
            x.name.replace('*', '').strip()
            for x in socket_group.socket_word_forms if not x.invisible
        ]

        for sub_group in socket_group.sub_groups:
            title_word_form = sub_group.title_word_form
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    raw_name = word_form.name.replace('*', '').strip()
                    if (
                            group_names.count(raw_name) == 1
                            and raw_name in socket_names):
                        if str(word_form) == str(title_word_form):
                            homonyms.append(str(word_form))
                        else:
                            homonyms.append(' < '.join([
                                str(word_form),
                                str(title_word_form),
                            ]))

    sort_homonyms = sorted(
        homonyms,
        key=lambda x: x.replace('*', '').strip().lower()
    )

    return sort_homonyms


# Слова, омонимичные многокорневым словам.txt
def get_homonymous_multi_rooted(word_forms_bases, socket_group_list) -> list:
    """
    Создать документ Многокорневые слова БГ.csv .
    Найти в БГ строки с НЕ многокорневыми словами (кроме невидимок),
    совпадающими по написанию с многокорневыми словами из документа
    Многокорневые слова.csv .
    Создать документ Слова, омонимичные многокорневым словам.txt
    и вставить в него найденные строки с соблюдением алфавитного порядка слов
    и с соблюдением следующего правила:
        если омоним является ЗС подгруппы, то просто полностью указывается
            строка с омонимом;
        если же омоним не является ЗС подгруппы, то после строки с омонимом
            ставится символ < и затем указывается строка с ЗС подгруппы,
            в которой находится данный омоним.
    """

    save_multi_root_words(word_forms_bases, socket_group_list)
    print(f'Создан документ: Многокорневые слова БГ.csv')
    print(f'... сортировка ...')

    multi_root_words = get_dicts_from_csv_file('Многокорневые слова БГ.csv')

    multi_root_names = []
    for multi_root_word in multi_root_words:
        for root_index_key in list(multi_root_word):
            if multi_root_word[root_index_key]:
                multi_root_names.append(
                    get_socket_word_form(multi_root_word[root_index_key]).name
                )

    homonymous_multi_rooted = []

    for socket_group in socket_group_list:
        for sub_group in socket_group.sub_groups:
            title_word_form = sub_group.title_word_form
            for word_form in sub_group.socket_word_forms:
                if (
                        not word_form.invisible
                        and not word_form.root_index
                ):
                    if word_form.name in multi_root_names:
                        if str(word_form) == str(title_word_form):
                            homonymous_multi_rooted.append(str(word_form))
                        else:
                            homonymous_multi_rooted.append(' < '.join([
                                str(word_form),
                                str(title_word_form),
                            ]))

    homonymous_multi_rooted = sorted(
        homonymous_multi_rooted,
        key=lambda x: x.replace('*', '').strip().lower()
    )

    return homonymous_multi_rooted
