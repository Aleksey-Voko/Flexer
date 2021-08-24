from bs_lists.nouns import get_nouns
from bs_lists.pronouns import get_pronouns, get_pronouns_no_plural


def get_filtered_list(word_forms_bases, out_bs: str) -> list:
    filtered_tmpl = {
        'Существительные.txt': get_nouns,

        'Местоимения.txt': get_pronouns,
        'Местоимения. Нет мн. ч.txt': get_pronouns_no_plural,
    }

    # Explicit tasks:
    if out_bs in filtered_tmpl.keys():
        return filtered_tmpl[out_bs](word_forms_bases)

    # Implicit tasks:
    elif out_bs.startswith(''):
        return []

    # Missing tasks:
    else:
        return []
