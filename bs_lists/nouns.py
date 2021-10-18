"""Все существительные"""

from pathlib import Path


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
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется указатель рода м / ж / с
    или указатель рода с индикатором "!":  м! / ж! / с! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с'))
                      and not x.startswith('мн'),
            group.title_word_form.info))
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
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется индикатор мн. ч. мн
    или индикатор мн. ч. с индикатором "!": мн! ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith('мн'),
            group.title_word_form.info))
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
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации имеется указатель рода м / ж / с и индикатор мн. ч. мн ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: (
                    x.startswith(('м', 'ж', 'с'))
                    and not x.startswith('мн')
            ),
            group.title_word_form.info))

           and any(map(
            lambda x: (
                    x.startswith('мн')
                    and not x.startswith('мн!')
            ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные м. р.txt
def get_masculine_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель муж. рода м
            или
        б. указатель муж. рода м!
            или
        в. указатель муж. рода м и указатель муж. рода
        с предшествующим дефисом -м (м…-м…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: (
                          x.startswith('м')
                          and '-' not in x
                          and not x.startswith('мн')
                      ) or (
                            x.startswith('м')
                            and '-м' in x
                            and not x.startswith('мн')
            ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные ж. р.txt
def get_feminine_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель жен. рода ж
            или
        б. указатель жен. рода ж!
            или
        в. указатель жен. рода ж и указатель жен. рода
        с предшествующим дефисом -ж (ж…-ж…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: (
                              x.startswith('ж')
                              and '-' not in x
                      ) or (
                              x.startswith('ж')
                              and '-ж' in x
                      ),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные с. р.txt
def get_neuter_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации в составе шаблона ед. ч. имеется:
        а. указатель ср. рода с
            или
        б. указатель ср. рода с!
            или
        в. указатель ср. рода с и указатель ср. рода
        с предшествующим дефисом -с (с…-с…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: (
                              x.startswith('с')
                              and '-' not in x
                      ) or (
                              x.startswith('с')
                              and '-с' in x
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

    idfs = Path(task).stem.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.С')
                and any(map(
                    lambda x: x in group.title_word_form.info,
                    [f'{x}{idfs}' for x in 'мжс']
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

    idfs = Path(task).stem.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.С')
                and f'мн{idfs}' in group.title_word_form.info
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

    idfs = Path(task).stem.split()[1:]
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
            and '-' in group.title_word_form.name)
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
