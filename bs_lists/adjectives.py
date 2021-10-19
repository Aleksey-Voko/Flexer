"""Все прилагательные"""

from pathlib import Path


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
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('мн')
    ]
    return word_forms


# Прилагательные ед. и мн. ч.txt
def get_singular_and_plural_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    в спец. информации указан шаблон полной формы,
    название которого не содержит мн ,
    и отсутствует индикатор ед. ч. е ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and not group.title_word_form.info[0].endswith('мн')
           and 'е' not in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Только м. р.txt
def get_masculine_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит м (но не мн) / фм ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('м')
           and not group.title_word_form.info[0].endswith('фм')
    ]
    return word_forms


# Прилагательные. Только ж. р.txt
def get_feminine_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит ж ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('ж')
    ]
    return word_forms


# Прилагательные. Только с. р.txt
def get_neuter_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит с (но не -с)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('с')
           and not group.title_word_form.info[0].endswith('-с')
    ]
    return word_forms


# Прилагательные. Нет с. р.txt
def get_non_neuter_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит -с ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('-с')
    ]
    return word_forms


# Притяжательные прилагательные.txt
def get_possessive_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит римскую цифру III
    (кроме шаблонов полной формы IIIф и IIIфм)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].startswith('III')
           and not group.title_word_form.info[0].startswith('IIIф')
    ]
    return word_forms


# Русские фамилии.txt
def get_russian_surnames(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы IIIф (но не IIIфм)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].startswith('IIIф')
           and not group.title_word_form.info[0].startswith('IIIфм')
    ]
    return word_forms


# Адъектированные причастия.txt
def get_adjusted_participles(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и перед ЗС имеется поставленный(-ые) без пробела символ(ы) * / ** ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and group.title_word_form.name.startswith('*')
    ]
    return word_forms


# Прилагательные. Нет полн. ф.txt
def get_no_full_form_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации отсутствует шаблон полной формы
    (кроме адъектированных причастий, т.е. ЗС,
    перед которыми имеется поставленный(-ые) без пробела символ(ы) * / ** )."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and not group.title_word_form.name.startswith('*')
    ]
    return word_forms


# Прилагательные. Есть кр. ф.txt
def get_short_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон краткой формы."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and any(map(
               lambda x: x.startswith('К'),
               group.title_word_form.info
           ))
    ]
    return word_forms


# Прилагательные. Есть срав. ст.txt
def get_comparative_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон сравнительной степени."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and any(map(
            lambda x: x.startswith('С'),
            group.title_word_form.info
            ))
    ]
    return word_forms


# Прилагательные. Есть прев. ст.txt
def get_superlative_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон превосходной степени."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and any(map(
            lambda x: x.startswith('П'),
            group.title_word_form.info
            ))
    ]
    return word_forms


# Поиск прилагательных с определённым элементом спец. информации /
# определённым сочетанием идущих друг за другом
# элементов спец. информации
# Напр. Прилагательные К2о СII5ч.txt
def get_adjectives_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан искомый элемент / указано искомое сочетание
    идущих друг за другом элементов.                                                                                                                                          Этот элемент спец. информации / сочетание элементов спец. информации вставляется в название документа после Прилагательные
    """

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.П')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms


# Прилагательные с дефисом.txt
def get_adjectives_hyphenated(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в ЗС имеется хотя бы 1 дефис."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and '-' in group.title_word_form.name
    ]
    return word_forms


# Прил-ные с дефисом. Изм. первая часть.txt
def get_adjectives_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
        идентификатор ЗС группы содержит .П ;
        в ЗС имеется хотя бы 1 дефис;
        часть слова до первого дефиса в строке ЗС
        и часть слова до первого дефиса в следующей после строки ЗС
        строке разные;                                                                                                                                                                 часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.П')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms
