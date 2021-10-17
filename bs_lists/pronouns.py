"""Местоимения"""

from pathlib import Path


# Поиск местоимений с определённым шаблоном
# Напр. Местоимения II3ь.txt
def get_pronouns_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в спец. информации указан искомый шаблон.
    Название этого шаблона вставляется в название документа после Местоимения
    """

    idfs = Path(task).stem.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and idfs in group.title_word_form.info
        )
    ]
    return word_forms


# Местоимения.txt
def get_pronouns(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.М')
    ]
    return word_forms


# Местоимения. Нет мн. ч.txt
def get_pronouns_no_plural(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в группе имеется словоформа с идентификатором .МР / .МР-
    (кроме ЗС с шаблонами I3, I4, I7, I7-).
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and not any(map(lambda x: x in group.title_word_form.info,
                                ('I3', 'I4', 'I7', 'I7-')))
                and any(map(lambda x: x in group.idf_list, ('.МР', '.МР-')))
        )
    ]
    return word_forms


# Местоимения. Нет ед. ч.txt
def get_pronouns_no_singular(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в спец. информации указан шаблон I3 / I4 / I7 / I7- .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and any(map(lambda x: x in group.title_word_form.info,
                            ('I3', 'I4', 'I7', 'I7-')))
        )
    ]
    return word_forms


# Местоимения ед. и мн. ч.txt
def get_pronouns_singular_and_plural(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в группе имеются словоформа с идентификатором .МмИ / .МмИ- / .МмИ-МмИ
    и словоформа с идентификатором .МмнИ / .МмнИ- / .МмнИ-МмнИ .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and any(map(lambda x: x in group.idf_list,
                            ('.МмИ', '.МмИ-', '.МмИ-МмИ')))
                and any(map(lambda x: x in group.idf_list,
                            ('.МмнИ', '.МмнИ-', '.МмнИ-МмнИ')))
        )
    ]
    return word_forms


# Местоимения с дефисом.txt
def get_pronouns_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в ЗС имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and '-' in group.title_word_form.name
        )
    ]
    return word_forms


# Мест-ния с дефисом. Изм. первая часть.txt
def get_pronouns_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС
    и часть слова до первого дефиса в следующей после строки ЗС строке разные;
    часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[1:]
                        ),
                        [
                            '-'.join(x.name.split('-')[1:])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Мест-ния с дефисом. Изм. последняя часть.txt
def get_pronouns_hyphenated_ch_last_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова после последнего дефиса в строке ЗС и часть слова после
    последнего дефиса в следующей после строки ЗС строке разные;
    часть слова до последнего дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[:-1]
                        ),
                        [
                            '-'.join(x.name.split('-')[:-1])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Мест-ния с дефисом. Изм. обе части.txt
def get_pronouns_hyphenated_ch_both_parts(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова до первого дефиса
    в следующей после строки ЗС строке разные;
    часть слова после последнего дефиса в строке ЗС
    и часть слова после последнего дефиса в
    следующей после строки ЗС строке разные.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
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
