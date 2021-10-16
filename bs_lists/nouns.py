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
