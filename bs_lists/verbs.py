"""Все Глаголы"""


from word_form import TitleWordForm


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


# Невозвратные глаголы.txt
def get_non_reflexive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается не на -СЯ / -СЬ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and not group.title_word_form.name.endswith(('ся', 'сь'))
    ]
    return word_forms


# Глаголы -ШЕЛ(СЯ).txt
def get_walked_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается на -ШЕЛ(СЯ) ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and group.title_word_form.name.endswith(('шел', 'шелся'))
    ]
    return word_forms


# Глаголы I спр.txt
def get_verbs_of_first_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит римскую цифру I
    (кроме шаблонов НБ вр., название которого содержит
    сочетание римских цифр I-II ,
    а также шаблонов НБ вр. I3&II2 / I3&II2л / I8щ&II5щ ,
    и кроме глаголов с дефисом, т.е.
    кроме ЗС групп, идентификатор которых содержит .Г , а также -Г)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_first_conj(group.title_word_form)
    ]
    return word_forms


def is_first_conj(form: TitleWordForm):
    """
    Для 'Глаголы I спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')
            and '-' not in form.idf
            and 'I-II' not in form.idf
            and info_list[0].startswith('НБI')
            and not info_list[0].startswith((
                'НБII', 'НБI3&II2', 'НБI3&II2л', 'НБI8щ&II5щ'))
    ):
        return True
    else:
        return False


# Глаголы II спр.txt
def get_verbs_of_second_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит римскую цифру II
    (кроме шаблонов НБ вр., название которого содержит
    сочетание римских цифр I-II ,
    а также шаблонов НБ вр. I3&II2 / I3&II2л / I8щ&II5щ ,
    и кроме глаголов с дефисом, т.е. кроме ЗС групп,
    идентификатор которых содержит .Г , а также -Г)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_second_conj(group.title_word_form)
    ]
    return word_forms


def is_second_conj(form: TitleWordForm):
    """
    Для 'Глаголы II спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')
            and 'II' in info_list[0]
            and 'I-II' not in info_list[0]
            and '&' not in info_list[0]
    ):
        return True
    else:
        return False


# Глаголы смеш. спр.txt
def get_verbs_of_mixed_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит сочетание римских цифр I-II ,
    а также следующие шаблоны НБ вр.: I3&II2 / I3&II2л / I8щ&II5щ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_mixed_conj(group.title_word_form)
    ]
    return word_forms


def is_mixed_conj(form: TitleWordForm):
    """
    Для 'Глаголы смеш. спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')

            and (
                'I-II' in info_list[0]
                or
                ('II' in info_list[0] and '&' in info_list[0])
            )
    ):
        return True
    else:
        return False


# Глаголы с дефисом.txt
def get_verbs_hyphenated(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в ЗС имеется хотя бы 1 дефис."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
           and '-' in group.title_word_form.name
    ]
    return word_forms
