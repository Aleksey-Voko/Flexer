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


# Двувидовые глаголы.txt
def get_two_species_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано 2в ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and '2в' in group.title_word_form.info
    ]
    return word_forms


# Переходные глаголы.txt
def get_transitive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано пер ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and 'пер' in group.title_word_form.info
    ]
    return word_forms


# Непереходные глаголы.txt
def get_intransitive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано неп ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and 'неп' in group.title_word_form.info
    ]
    return word_forms


# Безличные глаголы.txt
def get_impersonal_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации имеется индикатор безличности б ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and 'б' in group.title_word_form.info
    ]
    return word_forms


# Возвратные глаголы.txt
def get_reflexive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается на -СЯ / -СЬ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and group.title_word_form.name.endswith(('ся', 'сь'))
    ]
    return word_forms
