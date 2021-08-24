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

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
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
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в группе имеется словоформа с идентификатором .МР
    (кроме ЗС с шаблонами I3, I4, I7).
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and not any(map(lambda x: x in group.title_word_form.info,
                                ('I3', 'I4', 'I7')))
                and '.МР' in group.idf_list
        )
    ]
    return word_forms


# Местоимения. Нет ед. ч.txt
def get_pronouns_no_singular(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в спец. информации указан шаблон I3 / I4 / I7 .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and any(map(lambda x: x in group.title_word_form.info,
                            ('I3', 'I4', 'I7')))
        )
    ]
    return word_forms


# Местоимения ед. и мн. ч.txt
def get_pronouns_singular_and_plural(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в группе имеются словоформа с идентификатором .МмИ
    и словоформа с идентификатором .МмнИ .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and '.МмИ' in group.idf_list
                and '.МмнИ' in group.idf_list
        )
    ]
    return word_forms
