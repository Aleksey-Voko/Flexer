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
