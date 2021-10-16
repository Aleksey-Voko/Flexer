"""Все существительные"""


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
    и в спец. информации имеется указатель рода м / ж / с
    и индикатор мн. ч. мн ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith(('м', 'ж', 'с')),
            group.title_word_form.info))
           and any(map(
            lambda x: x.startswith('мн'),
            group.title_word_form.info))
    ]
    return word_forms


# Существительные м. р.txt
def get_masculine_nouns(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .С ,
    и в спец. информации в составе шаблона ед. ч. имеется указатель муж. рода м
    или указатель муж. рода м! ,
    или указатель муж. рода с предшествующим дефисом -м (м…-м…)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.С')
           and any(map(
            lambda x: x.startswith(('м', '-м'))
                      and not x.startswith('мн'),
            group.title_word_form.info))
    ]
    return word_forms
