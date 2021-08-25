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


# Слова с дефисом.txt
def get_words_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками, в которых
    имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if '-' in group.title_word_form.name
    ]
    return word_forms


# Слова с латиницей.txt
def get_latin_words(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп / одиночками, в которых
    имеется хотя бы 1 латинская буква.
    """

    from string import ascii_letters
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if any(map(lambda x: x in ascii_letters, group.title_word_form.name))
    ]
    return word_forms
