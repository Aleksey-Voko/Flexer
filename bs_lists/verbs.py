"""Все Глаголы"""


# Глаголы.txt
def get_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
    ]
    return word_forms


# Глаголы нес. вида.txt
def get_imperfective_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано нес ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and 'нес' in group.title_word_form.info
    ]
    return word_forms


# Глаголы сов. вида.txt
def get_perfect_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано сов ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and 'сов' in group.title_word_form.info
    ]
    return word_forms
