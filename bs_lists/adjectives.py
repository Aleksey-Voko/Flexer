"""Все прилагательные"""


# Прилагательные.txt
def get_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
    ]
    return word_forms


# Прилагательные одуш.txt
def get_animate_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется индикатор одушевлённости о ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and 'о' in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Нет мн. ч.txt
def get_non_plural_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется индикатор ед. ч. е ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and 'е' in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Нет ед. ч.txt
def get_non_singular_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит мн ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and any(map(
            lambda x: 'мн' in x,
            group.title_word_form.info))
    ]
    return word_forms
