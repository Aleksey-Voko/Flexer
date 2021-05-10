"""Прилагательные сравнительная степень"""

from word_form import WordForm


def get_comparative_forms(src_dict) -> list:
    comparative_tmpl = {
        'СI1': get_comparative_ci1,
    }
    return comparative_tmpl[src_dict['Inf_2']](src_dict)


# СI1
def get_comparative_ci1(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}ее', '.ПС1'),
        WordForm(f'{name[:-2]}ей', '.ПС2'),
        WordForm(f'по{name[:-2]}ее', '.ПС1*'),
        WordForm(f'по{name[:-2]}ей', '.ПС2*'),
    ]
    return word_forms
