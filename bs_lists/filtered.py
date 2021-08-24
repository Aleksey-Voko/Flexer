from bs_lists.nouns import get_nouns
from bs_lists.pronouns import (get_pronouns, get_pronouns_no_plural,
                               get_pronouns_no_singular)


def get_filtered_list(word_forms_bases, socket_group_list, out_bs: str) -> list:
    filtered_tmpl = {
        'Существительные.txt': get_nouns,

        'Местоимения.txt': get_pronouns,
        'Местоимения. Нет мн. ч.txt': get_pronouns_no_plural,
        'Местоимения. Нет ед. ч.txt': get_pronouns_no_singular,
    }

    # Explicit tasks:
    if out_bs in filtered_tmpl.keys():
        return filtered_tmpl[out_bs](word_forms_bases, socket_group_list)

    # Implicit tasks:
    elif out_bs.startswith(''):
        return []

    # Missing tasks:
    else:
        return []
