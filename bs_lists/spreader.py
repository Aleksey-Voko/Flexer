from bs_lists.adjectives import (get_adjectives, get_animate_adjectives,
                                 get_non_plural_adjectives,
                                 get_non_singular_adjectives,
                                 get_singular_and_plural_adjectives,
                                 get_masculine_adjectives,
                                 get_feminine_adjectives,
                                 get_neuter_adjectives,
                                 get_non_neuter_adjectives,
                                 get_possessive_adjectives,
                                 get_russian_surnames,
                                 get_adjusted_participles,
                                 get_no_full_form_adjectives,
                                 get_short_adjectives,
                                 get_comparative_adjectives,
                                 get_superlative_adjectives)
from bs_lists.nouns import (get_nouns, get_inanimate_nouns, get_animate_nouns,
                            get_singular_nouns, get_non_plural_nouns,
                            get_plural_nouns, get_non_singular_nouns,
                            get_singular_and_plural_nouns, get_masculine_nouns,
                            get_feminine_nouns, get_neuter_nouns,
                            get_nouns_of_i_declension,
                            get_nouns_of_ii_declension,
                            get_nouns_of_iii_declension, get_mixed_nouns,
                            get_pol_nouns, get_singular_nouns_implicit_pattern,
                            get_plural_nouns_implicit_pattern,
                            get_nouns_implicit_pattern, get_nouns_hyphenated,
                            get_nouns_hyphenated_ch_first_part,
                            get_nouns_hyphenated_ch_last_part,
                            get_nouns_hyphenated_ch_both_parts,
                            get_nouns_hyphenated_singular_and_plural,
                            get_nouns_multiple_hyphens)
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
                                get_replays_in_socket,
                                get_replays_in_socket_duplicate,
                                get_invisible, get_socket_with_exp_notes,
                                get_socket_with_etml_notes,
                                get_unknown_etymology,
                                get_no_accepted_etymology, get_formed_from,
                                get_etymology_ignored, get_under_the_influence,
                                get_a_noteworthy_etymology,
                                get_multi_root_words_homonyms,
                                get_replays_in_groups,
                                get_replays_in_socket_unique,
                                get_homonyms_bg, get_homonymous_multi_rooted,
                                get_replays_in_socket_strings,
                                get_homonymous_replays_in_socket,
                                get_ordinary_words_bg, get_bg_snapshot)

EXPLICIT_TASKS = {
    # БС
    'Существительные.txt': get_nouns,
    'Существительные неод.txt': get_inanimate_nouns,
    'Существительные одуш.txt': get_animate_nouns,
    'Существительные ед. ч.txt': get_singular_nouns,
    'Существительные. Нет мн. ч.txt': get_non_plural_nouns,
    'Существительные мн. ч.txt': get_plural_nouns,
    'Существительные. Нет ед. ч.txt': get_non_singular_nouns,
    'Существительные ед. и мн. ч.txt': get_singular_and_plural_nouns,
    'Существительные м. р.txt': get_masculine_nouns,
    'Существительные ж. р.txt': get_feminine_nouns,
    'Существительные с. р.txt': get_neuter_nouns,
    'Существительные I скл.txt': get_nouns_of_i_declension,
    'Существительные II скл.txt': get_nouns_of_ii_declension,
    'Существительные III скл.txt': get_nouns_of_iii_declension,
    'Существительные смеш. скл.txt': get_mixed_nouns,
    'Существительные ПОЛ-.txt': get_pol_nouns,
    'Существительные с дефисом.txt': get_nouns_hyphenated,
    'Сущ-ные с дефисом. Изм. первая часть.txt': get_nouns_hyphenated_ch_first_part,
    'Сущ-ные с дефисом. Изм. последняя часть.txt': get_nouns_hyphenated_ch_last_part,
    'Сущ-ные с дефисом. Изм. обе части.txt': get_nouns_hyphenated_ch_both_parts,
    'Сущ-ные с дефисом. Разное число.txt': get_nouns_hyphenated_singular_and_plural,
    'Существительные. Несколько дефисов.txt': get_nouns_multiple_hyphens,

    'Прилагательные.txt': get_adjectives,
    'Прилагательные одуш.txt': get_animate_adjectives,
    'Прилагательные. Нет мн. ч.txt': get_non_plural_adjectives,
    'Прилагательные. Нет ед. ч.txt': get_non_singular_adjectives,
    'Прилагательные ед. и мн. ч.txt': get_singular_and_plural_adjectives,
    'Прилагательные. Только м. р.txt': get_masculine_adjectives,
    'Прилагательные. Только ж. р.txt': get_feminine_adjectives,
    'Прилагательные. Только с. р.txt': get_neuter_adjectives,
    'Прилагательные. Нет с. р.txt': get_non_neuter_adjectives,
    'Притяжательные прилагательные.txt': get_possessive_adjectives,
    'Русские фамилии.txt': get_russian_surnames,
    'Адъектированные причастия.txt': get_adjusted_participles,
    'Прилагательные. Нет полн. ф.txt': get_no_full_form_adjectives,
    'Прилагательные. Есть кр. ф.txt': get_short_adjectives,
    'Прилагательные. Есть срав. ст.txt': get_comparative_adjectives,
    'Прилагательные. Есть прев. ст.txt': get_superlative_adjectives,

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
    'Нет общепринятой этимологии.txt': get_no_accepted_etymology,
    'Образовано от.txt': get_formed_from,
    'Этимология игнорируется.txt': get_etymology_ignored,
    'Образовано под влиянием.txt': get_under_the_influence,
    'Этимология примечательна.txt': get_a_noteworthy_etymology,
    'Многокорневые слова БГ - омонимы.txt': get_multi_root_words_homonyms,
    'Повторы в пределах гнезда.txt': get_replays_in_socket,
    'Повторы в гнезде - многокорневые слова.txt': get_replays_in_groups,
    'Повторы в гнезде. Повторяющиеся строки.txt': get_replays_in_socket_duplicate,
    'Повторы в гнезде. Уникальные строки.txt': get_replays_in_socket_unique,
    'Повторы в пределах гнезда. Строки.txt': get_replays_in_socket_strings,
    'Омонимы БГ.txt': get_homonyms_bg,
    'Слова, омонимичные многокорневым словам.txt': get_homonymous_multi_rooted,
    'Слова, омонимичные повторам в гнезде.txt': get_homonymous_replays_in_socket,
    'Обычные слова БГ.txt': get_ordinary_words_bg,
    'Снимок БГ.txt': get_bg_snapshot,
}

IMPLICIT_TASK = {
    'Местоимения': get_pronouns_implicit_pattern,
    'Числительные': get_numerals_implicit_pattern,
    'Существительные_ед_ч': get_singular_nouns_implicit_pattern,
    'Существительные_мн_ч': get_plural_nouns_implicit_pattern,
    'Существительные': get_nouns_implicit_pattern,
}


def get_filtered_list(word_forms_bases, socket_group_list, task: str) -> list:
    # Explicit tasks:
    if task in EXPLICIT_TASKS.keys():
        return EXPLICIT_TASKS[task](word_forms_bases, socket_group_list)

    # Implicit tasks:
    elif task.startswith(tuple(IMPLICIT_TASK.keys())):
        return IMPLICIT_TASK[task.split()[0]](
            word_forms_bases, socket_group_list, task)

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
