"""Все существительные"""


from collections import OrderedDict
from itertools import zip_longest

from utils import save_list_of_lists_to_csv_file, save_list_to_file


# Существительные.txt
def get_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С"""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
    ]
    return word_forms


# Существительные неод.txt
def get_inanimate_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указано неод ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and 'неод' in group.title_word_form.info
    ]
    return word_forms


# Существительные одуш.txt
def get_animate_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указано одуш ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and 'одуш' in group.title_word_form.info
    ]
    return word_forms


# Существительные ед. ч.txt
def get_singular_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп с идентификатором .СеИ-СмнИ / .СмнИ-СеИ ,
    а также строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется указатель рода м / ж / с
    или указатель рода с индикатором "!":  м! / ж! / с! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and any(map(
                lambda x: x.startswith(('м', 'ж', 'с'))
                          and not x.startswith('мн'),
                    group.title_word_form.info)))
           or group.title_word_form.idf in ('.СеИ-СмнИ', '.СмнИ-СеИ')
    ]
    return word_forms


# Существительные. Нет мн. ч.txt
def get_non_plural_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется указатель рода с индикатором "!":  м! / ж! / с! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith(('м!', 'ж!', 'с!')),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные мн. ч.txt
def get_plural_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп с идентификатором .СеИ-СмнИ / .СмнИ-СеИ ,
    а также строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется индикатор мн. ч. мн
    или индикатор мн. ч. с индикатором "!": мн! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and any(map(
                    lambda x: x.startswith('мн'),
                    group.title_word_form.info)))
           or group.title_word_form.idf in ('.СеИ-СмнИ', '.СмнИ-СеИ')
    ]
    return word_forms


# Существительные. Нет ед. ч.txt
def get_non_singular_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется индикатор мн. ч. с индикатором "!": мн! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith('мн!'),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные ед. и мн. ч.txt
def get_singular_and_plural_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп с идентификатором .СеИ-СмнИ / .СмнИ-СеИ ,
    а также строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется указатель рода м / ж / с
    и индикатор мн. ч. мн ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and any(map(
                    lambda x: (
                            x.startswith(('м', 'ж', 'с'))
                            and not x.startswith('мн')
                    ), group.title_word_form.info))
            and any(map(
                    lambda x: (
                            x.startswith('мн')
                            and not x.startswith('мн!')
                    ), group.title_word_form.info)))

           or group.title_word_form.idf in ('.СеИ-СмнИ', '.СмнИ-СеИ')
    ]
    return word_forms


# Существительные м. р.txt
def get_masculine_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и не содержит символ /
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель муж. рода м и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        б. указатель муж. рода м! и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        в. указатель муж. рода м и указатель муж. рода
        с предшествующим дефисом -м (м…-м…)
            или
        г. имеются указатель муж. рода с индикатором "!" м!
        и указатель муж. рода с индикатором "!"
        с предшествующим дефисом -м! (м!…-м!…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '/' not in group.title_word_form.idf
           and any(map(
            lambda x: (
                          x.startswith('м')
                          and '-' not in x
                          and not x.startswith('мн')
                      ) or (
                          x.startswith('м')
                          and group.title_word_form.idf == '.СеИ-'
                          and not x.startswith('мн')
                      ) or (
                          x.startswith('м')
                          and ('-м' in x and '-мн' not in x)
                          and not x.startswith('мн')
                      ) or (
                              x.startswith('м!')
                              and '-м!' in x
                      ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные ж. р.txt
def get_feminine_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и не содержит символ /
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель жен. рода ж и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        б. указатель жен. рода ж! и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        в. указатель жен. рода ж и указатель жен. рода
        с предшествующим дефисом -ж (ж…-ж…)
            или
        г. указатель жен. рода с индикатором "!" ж!
        и указатель жен. рода с индикатором "!"
        с предшествующим дефисом -ж! (ж!…-ж!…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '/' not in group.title_word_form.idf
           and any(map(
            lambda x: (
                              x.startswith('ж')
                              and '-' not in x
                      ) or (
                              x.startswith('ж')
                              and group.title_word_form.idf == '.СеИ-'
                      ) or (
                              x.startswith('ж')
                              and '-ж' in x
                      ) or (
                              x.startswith('ж!')
                              and '-ж!' in x
                      ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные с. р.txt
def get_neuter_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и не содержит символ /
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель ср. рода с и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        б. указатель ср. рода с! и отсутствует дефис
        (кроме ЗС групп с идентификатором .СеИ-)
            или
        в. указатель ср. рода с и указатель ср. рода
        с предшествующим дефисом -с (с…-с…)
            или
        г. указатель ср. рода с индикатором "!" с!
        и указатель ср. рода с индикатором "!"
        с предшествующим дефисом -с! (с!…-с!…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '/' not in group.title_word_form.idf
           and any(map(
            lambda x: (
                              x.startswith('с')
                              and '-' not in x
                      ) or (
                              x.startswith('с')
                              and group.title_word_form.idf == '.СеИ-'
                      ) or (
                              x.startswith('с')
                              and '-с' in x
                      ) or (
                              x.startswith('с!')
                              and '-с!' in x
                      ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные I скл.txt
def get_nouns_of_i_declension(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан шаблон ед. ч.,
    название которого содержит римскую цифру I
    (кроме шаблонов ед. ч. I5&II2* и I7&II4* и кроме существительных с дефисом,
    у которых изменяются обе части слова, т.е. кроме ЗС групп,
    идентификатор которых содержит .С , а также -С)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '-С' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн')
                      and 'I' in x
                      and 'II' not in x
                      and 'I5&II2*' not in x
                      and 'I7&II4*' not in x,
            group.title_word_form.info))
    ]
    return word_forms


# Существительные II скл.txt
def get_nouns_of_ii_declension(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан шаблон ед. ч.,
    название которого содержит римскую цифру II
    (кроме шаблонов ед. ч. I5&II2* и I7&II4* и кроме существительных с дефисом,
    у которых изменяются обе части слова, т.е. кроме ЗС групп,
    идентификатор которых содержит .С , а также -С)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '-С' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн')
                      and 'II' in x
                      and 'III' not in x
                      and 'I5&II2*' not in x
                      and 'I7&II4*' not in x,
            group.title_word_form.info))
    ]
    return word_forms


# Существительные III скл.txt
def get_nouns_of_iii_declension(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан шаблон ед. ч.,
    название которого содержит римскую цифру III
    (кроме существительных с дефисом, у которых изменяются обе части слова,
    т.е. кроме ЗС групп, идентификатор которых содержит .С , а также -С)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '-С' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн')
                      and 'III' in x,
            group.title_word_form.info))
    ]
    return word_forms


# Существительные смеш. скл.txt
def get_mixed_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан шаблон ед. ч. I5&II2* / I7&II4*
    (кроме существительных с дефисом, у которых изменяются обе части слова,
    т.е. кроме ЗС групп, идентификатор которых содержит .С , а также -С)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '-С' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн')
                      and (
                              'I5&II2*' in x
                              or 'I7&II4*' in x
                      ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные ПОЛ-.txt
def get_pol_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан шаблон ед. ч.,
    название которого содержит символ / ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн')
                      and '/' in x,
            group.title_word_form.info))
    ]
    return word_forms


# Поиск существительных с определённым шаблоном ед. ч.
# Напр. Существительные_ед_ч I1.txt
def get_singular_nouns_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан искомый шаблон ед. ч.
    Название этого шаблона вставляется в название документа
    после Существительные ед. ч.
    """

    idfs = task.split('.')[0]
    idfs = idfs.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.С')
                and any(map(
                    lambda x: x in group.title_word_form.info,
                    [f'{x}{idfs}' for x in ('м', 'м!', 'ж', 'ж!', 'с', 'с!')]
                ))
        )
    ]
    return word_forms


# Поиск существительных с определённым шаблоном мн. ч.
# Напр. Существительные_мн_ч I1.txt
def get_plural_nouns_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указан искомый шаблон мн. ч.
    Название этого шаблона вставляется в название документа
    после Существительные мн. ч.
    """

    idfs = task.split('.')[0]
    idfs = idfs.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.С')
                and any(map(
                    lambda x: x in group.title_word_form.info,
                    [f'{x}{idfs}' for x in ('мн', 'мн!')]
                ))
        )
    ]
    return word_forms


# Поиск существительных с определённым сочетанием идущих друг за другом
# элементов спец. информации
# Напр. Существительные мI1 мнI1.txt
def get_nouns_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации указано искомое сочетание
    идущих друг за другом элементов.
    Это сочетание элементов спец. информации вставляется в название
    документа после Существительные
    """

    idfs = task.split('.')[0]
    idfs = idfs.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.С')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms


# Существительные с дефисом.txt
def get_nouns_hyphenated(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в ЗС имеется хотя бы 1 дефис."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and '-' in group.title_word_form.name
    ]
    return word_forms


# Сущ-ные с дефисом. Изм. первая часть.txt
def get_nouns_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .С ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС
    и часть слова до первого дефиса в следующей
    после строки ЗС строке разные;
    часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and all(map(
                    lambda x: x == '-'.join(
                        group.title_word_form.name.split('-')[1:]
                    ),
                    [
                        '-'.join(x.name.split('-')[1:])
                        for x in group.word_forms
                    ]
                ))
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Сущ-ные с дефисом. Изм. последняя часть.txt
def get_nouns_hyphenated_ch_last_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .С ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова после последнего дефиса в строке ЗС и часть слова
    после последнего дефиса в следующей после строки ЗС строке разные;
    часть слова до последнего дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
                and all(map(
                    lambda x: x == '-'.join(
                        group.title_word_form.name.split('-')[:-1]
                    ),
                    [
                        '-'.join(x.name.split('-')[:-1])
                        for x in group.word_forms
                    ]
                ))
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Сущ-ные с дефисом. Изм. обе части.txt
def get_nouns_hyphenated_ch_both_parts(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .С ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова
    до первого дефиса в следующей после строки ЗС строке разные;
    часть слова после последнего дефиса в строке ЗС и часть слова
    после последнего дефиса в следующей после строки ЗС строке разные.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.С')
            and '-' in group.title_word_form.name
            and '-' in group.word_forms[0].name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Сущ-ные с дефисом. Разное число.txt
def get_nouns_hyphenated_singular_and_plural(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп
    с идентификатором .СеИ-СмнИ / .СмнИ-СеИ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf in ('.СеИ-СмнИ', '.СмнИ-СеИ')
    ]
    return word_forms


# Существительные. Несколько дефисов.txt
def get_nouns_multiple_hyphens(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С
    и в ЗС имеется более 1 дефиса."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and group.title_word_form.name.count('-') > 1
    ]
    return word_forms


# Существительные. Сочетания шаблонов.csv
def save_nouns_pattern_combinations(word_forms_bases, _):
    """Создать документы:
        Сущ-ные с дефисом. Изм. первая часть.txt ,
        Сущ-ные с дефисом. Изм. обе части.txt ,
        Сущ-ные с дефисом. Разное число.txt .
    Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и ЗС отсутствует в документах
        Сущ-ные с дефисом. Изм. первая часть.txt ,
        Сущ-ные с дефисом. Изм. обе части.txt ,
        Сущ-ные с дефисом. Разное число.txt .

    Выбрать из найденных строк строки с уникальным сочетанием
    элементов спец. информации
    (подробнее об элементах спец. информации - см. док-т Структура строки.xlsx,
    вкладка Структура спец. информации).

    Примечание. При наличии нескольких строк с одинаковым сочетанием
    элементов спец. информации выбирать первую (верхнюю) строку,
    т.е. строку, слово в которой идёт первым по алфавиту.

    Создать документ Существительные. Сочетания шаблонов.csv .
    Вставить в 8 столбцов этого документа выбранные строки
    (слово - в первый столбец, элементы спец. информации - в другие,
    соответствующие им по типу 7 столбцов),
    располагая строки в соответствии с алфавитным порядком
    элементов спец. информации."""

    # Сущ-ные с дефисом. Изм. первая часть.txt
    nouns_ch_first_part = get_nouns_hyphenated_ch_first_part(
        word_forms_bases, _)
    save_list_to_file(nouns_ch_first_part,
                      'Сущ-ные с дефисом. Изм. первая часть.txt',
                      encoding='cp1251')
    print(f'Создан документ: Сущ-ные с дефисом. Изм. первая часть.txt')
    print(f'... сортировка ...')

    # Сущ-ные с дефисом. Изм. обе части.txt
    nouns_ch_both_parts = get_nouns_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(nouns_ch_both_parts,
                      'Сущ-ные с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Сущ-ные с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    # Сущ-ные с дефисом. Разное число.txt
    nouns_singular_and_plural = get_nouns_hyphenated_singular_and_plural(
        word_forms_bases, _)
    save_list_to_file(nouns_singular_and_plural,
                      'Сущ-ные с дефисом. Разное число.txt',
                      encoding='cp1251')
    print(f'Создан документ: Сущ-ные с дефисом. Разное число.txt')
    print(f'... сортировка ...')

    unusual_words = (
            nouns_ch_first_part
            + nouns_ch_both_parts
            + nouns_singular_and_plural
    )

    word_forms = []
    unique_elements = []

    for group in word_forms_bases:
        if (
                group.title_word_form.idf.startswith('.С')
                and str(group.title_word_form) not in unusual_words
        ):
            elements = ' '.join(group.title_word_form.info)
            if elements not in unique_elements:
                unique_elements.append(elements)
                word_forms.append(group.title_word_form)

    in_form_of_list_1 = []
    in_form_of_list_2 = []
    in_form_of_list_3 = []

    for form in word_forms:
        indicators = OrderedDict({
            'name': form.name,
            'idf': form.idf,
            'animality': '',
            'род': '',
            'только ед. ч.': '',
            'шаблон ед. ч.': '',
            'мн': '',
            'только мн. ч.': '',
            'шаблон мн. ч.': '',
        })

        for indicator in form.info:
            if indicator in ('одуш', 'неод'):
                indicators['animality'] = indicator
            elif indicator.startswith('мн!'):
                indicators['мн'] = 'мн'
                indicators['только мн. ч.'] = '!'
                indicators['шаблон мн. ч.'] = indicator[3:]
            elif indicator.startswith('мн'):
                indicators['мн'] = 'мн'
                indicators['шаблон мн. ч.'] = indicator[2:]
            elif indicator.startswith(('м!', 'ж!', 'с!')):
                indicators['род'] = indicator[0]
                indicators['только ед. ч.'] = '!'
                indicators['шаблон ед. ч.'] = indicator[2:]
            elif indicator.startswith(('м', 'ж', 'с')):
                indicators['род'] = indicator[0]
                indicators['шаблон ед. ч.'] = indicator[1:]

        if indicators['только ед. ч.']:
            in_form_of_list_2.append(list(indicators.values()))
        elif indicators['только мн. ч.']:
            in_form_of_list_3.append(list(indicators.values()))
        else:
            in_form_of_list_1.append(list(indicators.values()))

    in_form_of_list_1 = sorted(
        in_form_of_list_1,
        key=lambda x: (x[5], x[8], x[2], x[3])
    )

    in_form_of_list_2 = sorted(
        in_form_of_list_2,
        key=lambda x: (x[5], x[2], x[3])
    )

    in_form_of_list_3 = sorted(
        in_form_of_list_3,
        key=lambda x: (x[8], x[2], x[3])
    )

    in_form_of_list = zip_longest(
            in_form_of_list_1,
            in_form_of_list_2,
            in_form_of_list_3,
            fillvalue=[''] * 9
    )

    in_form_of_list = [
        [x for y in lst for x in y]
        for lst in in_form_of_list
    ]

    save_list_of_lists_to_csv_file(
        in_form_of_list,
        'Существительные. Сочетания шаблонов.csv',
        encoding='cp1251',
        delimiter=';'
    )
