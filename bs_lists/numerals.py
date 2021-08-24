"""Числительные"""

from pathlib import Path


# Поиск числительных с определённым шаблоном
# Напр. Числительные II10.txt
def get_numerals_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч,
    и в спец. информации указан искомый шаблон.
    Название этого шаблона вставляется в название документа после Числительные
    """

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.Ч')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms


# Числительные.txt
def get_numerals(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Ч')
    ]
    return word_forms


# Числительные с дефисом.txt
def get_numerals_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч ,
    и в ЗС имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.Ч')
                and '-' in group.title_word_form.name
        )
    ]
    return word_forms


# Числ-ные с дефисом. Изм. первая часть.txt
def get_numerals_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .Ч ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова до первого дефиса
    в следующей после строки ЗС строке разные;
    часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Ч')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[1:]),
                        [
                            '-'.join(x.name.split('-')[1:])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms
