from bs_lists.nouns import get_nouns
from bs_lists.numerals import (get_numerals, get_numerals_implicit_pattern,
                               get_numerals_hyphenated,
                               get_numerals_hyphenated_ch_first_part,
                               get_numerals_hyphenated_ch_last_part,
                               get_numerals_hyphenated_ch_both_parts)
from bs_lists.pronouns import (get_pronouns, get_pronouns_no_plural,
                               get_pronouns_no_singular,
                               get_pronouns_singular_and_plural,
                               get_pronouns_implicit_pattern,
                               get_pronouns_hyphenated,
                               get_pronouns_hyphenated_ch_first_part,
                               get_pronouns_hyphenated_ch_last_part,
                               get_pronouns_hyphenated_ch_both_parts)
from bs_lists.rest import get_loners, get_words_hyphenated

EXPLICIT_TASKS = {
    'Существительные.txt': get_nouns,

    'Местоимения.txt': get_pronouns,
    'Местоимения. Нет мн. ч.txt': get_pronouns_no_plural,
    'Местоимения. Нет ед. ч.txt': get_pronouns_no_singular,
    'Местоимения ед. и мн. ч.txt': get_pronouns_singular_and_plural,
    'Местоимения с дефисом.txt': get_pronouns_hyphenated,
    'Мест-ния с дефисом. Изм. первая часть.txt': get_pronouns_hyphenated_ch_first_part,
    'Мест-ния с дефисом. Изм. последняя часть.txt': get_pronouns_hyphenated_ch_last_part,
    'Мест-ния с дефисом. Изм. обе части.txt': get_pronouns_hyphenated_ch_both_parts,

    'Числительные.txt': get_numerals,
    'Числительные с дефисом.txt': get_numerals_hyphenated,
    'Числ-ные с дефисом. Изм. первая часть.txt': get_numerals_hyphenated_ch_first_part,
    'Числ-ные с дефисом. Изм. последняя часть.txt': get_numerals_hyphenated_ch_last_part,
    'Числ-ные с дефисом. Изм. обе части.txt': get_numerals_hyphenated_ch_both_parts,

    'Одиночки.txt': get_loners,
    'Слова с дефисом.txt': get_words_hyphenated,
}

IMPLICIT_TASK = {
    'Местоимения': get_pronouns_implicit_pattern,
    'Числительные': get_numerals_implicit_pattern,
}


def get_filtered_list(word_forms_bases, socket_group_list, task: str) -> list:
    # Explicit tasks:
    if task in EXPLICIT_TASKS.keys():
        return EXPLICIT_TASKS[task](word_forms_bases, socket_group_list)

    # Implicit tasks:
    elif task.startswith(tuple(IMPLICIT_TASK.keys())):
        return IMPLICIT_TASK[task.split()[0]](word_forms_bases,
                                              socket_group_list, task)

    # Missing tasks:
    else:
        return []
