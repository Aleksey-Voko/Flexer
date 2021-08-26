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
from bs_lists.rest import (get_loners, get_words_hyphenated, get_latin_words,
                           get_words_with_exp_notes, get_homonyms,
                           get_words_with_exp_notes_no_homonyms,
                           get_words_with_spec_notes, get_multi_root_words,
                           get_repeats_w_socket_1_in_bs, get_homonymous_forms,
                           get_bs_snapshot, get_common_words_bs)
from bs_lists.socket_bg import (save_multi_root_words,
                                get_repeats_within_a_socket,
                                get_repeats_within_a_socket_duplicate,
                                get_invisible, get_socket_with_exp_notes,
                                get_socket_with_etml_notes,
                                get_unknown_etymology)

EXPLICIT_TASKS = {
    # БС
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
    'Слова с латиницей.txt': get_latin_words,
    'Слова с пояснительными примечаниями БС.txt': get_words_with_exp_notes,
    'Пояснительные примечания (без омонимов).txt': get_words_with_exp_notes_no_homonyms,
    'Слова со специальными примечаниями.txt': get_words_with_spec_notes,
    'Многокорневые слова БС.txt': get_multi_root_words,
    'Повторы в пределах гнезда. 1 раз в БС.txt': get_repeats_w_socket_1_in_bs,
    'Омонимы БС (ЗС групп и одиночки).txt': get_homonyms,
    'Омонимичные формы БС.txt': get_homonymous_forms,
    'Обычные слова БС.txt': get_common_words_bs,
    'Снимок БС.txt': get_bs_snapshot,

    # БГ
    'Невидимки.txt': get_invisible,
    'Слова с пояснительными примечаниями БГ.txt': get_socket_with_exp_notes,
    'Слова с этимологическими примечаниями.txt': get_socket_with_etml_notes,
    'Этимология неизвестна.txt': get_unknown_etymology,

    'Повторы в пределах гнезда.txt': get_repeats_within_a_socket,
    'Повторы в гнезде. Повторяющиеся строки.txt': get_repeats_within_a_socket_duplicate,
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


SCV_TASK = {
    'Многокорневые слова БГ.csv': save_multi_root_words,
}


def run_csv_task(word_forms_bases, socket_group_list, task: str):
    if task in SCV_TASK.keys():
        SCV_TASK[task](word_forms_bases, socket_group_list)
        return True

    else:
        return False
