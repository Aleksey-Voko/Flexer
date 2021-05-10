"""Прилагательные превосходная степень"""

from word_form import WordForm


def get_superlative_forms(src_dict) -> list:
    superlative_tmpl = {
        'ПI1': get_superlative_pi1,
        'ПI2': get_superlative_pi2,
        'ПII1': get_superlative_pii1,
        'ПII2ж': get_superlative_pii2zh,
        'ПII3ж': get_superlative_pii3zh,
        'ПII4ч': get_superlative_pii4ch,
        'ПII5ч': get_superlative_pii5ch,
        'ПII6ч': get_superlative_pii6ch,
        'ПII7ч': get_superlative_pii7ch,
        'ПII8ш': get_superlative_pii8sh,
    }
    return superlative_tmpl[src_dict['Inf_3']](src_dict)


# ПI1
def get_superlative_pi1(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-2]}ейший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПI2
def get_superlative_pi2(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-3]}ейший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII1
def get_superlative_pii1(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-2]}айший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII2ж
def get_superlative_pii2zh(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-3]}жайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII3ж
def get_superlative_pii3zh(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-4]}жайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII4ч
def get_superlative_pii4ch(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-3]}чайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII5ч
def get_superlative_pii5ch(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-4]}чайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII6ч
def get_superlative_pii6ch(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-3]}ьчайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII7ч
def get_superlative_pii7ch(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-4]}гчайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms


# ПII8ш
def get_superlative_pii8sh(src_dict) -> list:
    pmi = src_dict['name']
    ppmi = f'{pmi[:-3]}шайший'
    word_forms = [
        WordForm(ppmi, '.ППмИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППмР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППмД'),
        WordForm(ppmi, '.ППмВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППмТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППмП'),
        WordForm(f'{ppmi[:-2]}ая', '.ППжИ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжР'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжД'),
        WordForm(f'{ppmi[:-2]}ую', '.ППжВ'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжТ1'),
        WordForm(f'{ppmi[:-2]}ею', '.ППжТ2'),
        WordForm(f'{ppmi[:-2]}ей', '.ППжП'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсИ'),
        WordForm(f'{ppmi[:-2]}его', '.ППсР'),
        WordForm(f'{ppmi[:-2]}ему', '.ППсД'),
        WordForm(f'{ppmi[:-2]}ее', '.ППсВ'),
        WordForm(f'{ppmi[:-2]}им', '.ППсТ'),
        WordForm(f'{ppmi[:-2]}ем', '.ППсП'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнИ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнР'),
        WordForm(f'{ppmi[:-2]}им', '.ППмнД'),
        WordForm(f'{ppmi[:-2]}ие', '.ППмнВ'),
        WordForm(f'{ppmi[:-2]}ими', '.ППмнТ'),
        WordForm(f'{ppmi[:-2]}их', '.ППмнП'),
    ]
    return word_forms
