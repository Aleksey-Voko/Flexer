from bs_lists.nouns import get_nouns


def get_filtered_list(word_forms_bases, out_bs: str) -> list:
    filtered_tmpl = {
        'Существительные.txt': get_nouns,
    }

    return filtered_tmpl[out_bs](word_forms_bases)
