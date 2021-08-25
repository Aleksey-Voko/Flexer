"""Обобщённо все части речи"""


# Одиночки.txt
def get_loners(word_forms_bases, _) -> list:
    """
    Найти в БС строки с одиночками.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if not group.word_forms
    ]
    return word_forms
