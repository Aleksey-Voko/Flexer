"""Числительные"""


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
