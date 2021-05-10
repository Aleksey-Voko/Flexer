"""Прилагательные сравнительная степень"""

from word_form import WordForm


def get_comparative_forms(src_dict) -> list:
    comparative_tmpl = {
        'СI1': get_comparative_ci1,
        'СI1-': get_comparative_ci1_dash,
        'СII1': get_comparative_cii1,
        'СII2': get_comparative_cii2,
        'СII3ж': get_comparative_cii3zh,
        'СII4ж': get_comparative_cii4zh,
        'СII5ч': get_comparative_cii5ch,
        'СII6ч': get_comparative_cii6ch,
        'СII7ч': get_comparative_cii7ch,
        'СII8ш': get_comparative_cii8sh,
        'СII10ш': get_comparative_cii10sh,
        'СII11ш': get_comparative_cii11sh,
        'СII12ш': get_comparative_cii12sh,
        'СII13щ': get_comparative_cii13shch,
        'СI1&3о': get_comparative_ci1_3o,
        'СI1&II3ж': get_comparative_ci1_ii3zh,
        'СI1&II4ж': get_comparative_ci1_ii4zh,
        'СI1&II10ш': get_comparative_ci1_ii10sh,
        'СI1&II15л': get_comparative_ci1_ii15l,
        'СI2&II5ч': get_comparative_ci2_ii5ch,
        'СII5ч&7ч': get_comparative_cii5ch_7ch,
        'СII5ч&14щ': get_comparative_cii5ch_14shch,
        'СII6ч&9ш': get_comparative_cii6ch_9sh,
    }
    return comparative_tmpl[src_dict['Inf_2']](src_dict)


# СI1
def get_comparative_ci1(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
    ]
    return word_forms


# СI1-
def get_comparative_ci1_dash(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
    ]
    return word_forms


# СII1
def get_comparative_cii1(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}е', '.ПС'),
        WordForm(f'по{pmi[:-2]}е', '.ПС*'),
    ]
    return word_forms


# СII2
def get_comparative_cii2(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}е', '.ПС'),
        WordForm(f'по{pmi[:-4]}е', '.ПС*'),
    ]
    return word_forms


# СII3ж
def get_comparative_cii3zh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}же', '.ПС'),
        WordForm(f'по{pmi[:-3]}же', '.ПС*'),
    ]
    return word_forms


# СII4ж
def get_comparative_cii4zh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}же', '.ПС'),
        WordForm(f'по{pmi[:-4]}же', '.ПС*'),
    ]
    return word_forms


# СII5ч
def get_comparative_cii5ch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}че', '.ПС'),
        WordForm(f'по{pmi[:-3]}че', '.ПС*'),
    ]
    return word_forms


# СII6ч
def get_comparative_cii6ch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}че', '.ПС'),
        WordForm(f'по{pmi[:-4]}че', '.ПС*'),
    ]
    return word_forms


# СII7ч
def get_comparative_cii7ch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}ьче', '.ПС'),
        WordForm(f'по{pmi[:-3]}ьче', '.ПС*'),
    ]
    return word_forms


# СII8ш
def get_comparative_cii8sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}ше', '.ПС'),
        WordForm(f'по{pmi[:-3]}ше', '.ПС*'),
    ]
    return word_forms


# СII10ш
def get_comparative_cii10sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-5]}ше', '.ПС'),
        WordForm(f'по{pmi[:-5]}ше', '.ПС*'),
    ]
    return word_forms


# СII11ш
def get_comparative_cii11sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}ьше', '.ПС'),
        WordForm(f'по{pmi[:-3]}ьше', '.ПС*'),
    ]
    return word_forms


# СII12ш
def get_comparative_cii12sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}ьше', '.ПС'),
        WordForm(f'по{pmi[:-4]}ьше', '.ПС*'),
    ]
    return word_forms


# СII13щ
def get_comparative_cii13shch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}ще', '.ПС'),
        WordForm(f'по{pmi[:-4]}ще', '.ПС*'),
    ]
    return word_forms


# СI1&3о
def get_comparative_ci1_3o(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'{pmi[:-4]}онее', '.ПС3'),
        WordForm(f'{pmi[:-4]}оней', '.ПС4'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-4]}онее', '.ПС3*'),
        WordForm(f'по{pmi[:-4]}оней', '.ПС4*'),
    ]
    return word_forms


# СI1&II3ж
def get_comparative_ci1_ii3zh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'{pmi[:-3]}же', '.ПС3'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-3]}же', '.ПС3*'),
    ]
    return word_forms


# СI1&II4ж
def get_comparative_ci1_ii4zh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'{pmi[:-4]}же', '.ПС3'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-4]}же', '.ПС3*'),
    ]
    return word_forms


# СI1&II10ш
def get_comparative_ci1_ii10sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'{pmi[:-5]}ше', '.ПС3'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-5]}ше', '.ПС3*'),
    ]
    return word_forms


# СI1&II15л
def get_comparative_ci1_ii15l(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ее', '.ПС1'),
        WordForm(f'{pmi[:-2]}ей', '.ПС2'),
        WordForm(f'{pmi[:-2]}ле', '.ПС3'),
        WordForm(f'по{pmi[:-2]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-2]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-2]}ле', '.ПС3*'),
    ]
    return word_forms


# СI2&II5ч
def get_comparative_ci2_ii5ch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}ее', '.ПС1'),
        WordForm(f'{pmi[:-3]}ей', '.ПС2'),
        WordForm(f'{pmi[:-3]}е', '.ПС3'),
        WordForm(f'по{pmi[:-3]}ее', '.ПС1*'),
        WordForm(f'по{pmi[:-3]}ей', '.ПС2*'),
        WordForm(f'по{pmi[:-3]}е', '.ПС3*'),
    ]
    return word_forms


# СII5ч&7ч
def get_comparative_cii5ch_7ch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}че', '.ПС1'),
        WordForm(f'{pmi[:-3]}ьче', '.ПС2'),
        WordForm(f'по{pmi[:-3]}че', '.ПС1*'),
        WordForm(f'по{pmi[:-3]}ьче', '.ПС2*'),
    ]
    return word_forms


# СII5ч&14щ
def get_comparative_cii5ch_14shch(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}че', '.ПС1'),
        WordForm(f'{pmi[:-5]}ще', '.ПС2'),
        WordForm(f'по{pmi[:-3]}че', '.ПС1*'),
        WordForm(f'по{pmi[:-5]}ще', '.ПС2*'),
    ]
    return word_forms


# СII6ч&9ш
def get_comparative_cii6ch_9sh(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}че', '.ПС1'),
        WordForm(f'{pmi[:-4]}ше', '.ПС2'),
        WordForm(f'по{pmi[:-4]}че', '.ПС1*'),
        WordForm(f'по{pmi[:-4]}ше', '.ПС2*'),
    ]
    return word_forms
