"""Прилагательные превосходная степень"""

from word_form import WordForm


def get_superlative_forms(src_dict) -> list:
    superlative_tmpl = {
        'ПI1': get_superlative_pi1,
    }
    return superlative_tmpl[src_dict['Inf_3']](src_dict)


# ПI1
def get_superlative_pi1(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}ейший', '.ППмИ'),
        WordForm(f'{name[:-2]}ейшего', '.ППмР'),
        WordForm(f'{name[:-2]}ейшему', '.ППмД'),
        WordForm(f'{name[:-2]}ейший', '.ППмВ'),
        WordForm(f'{name[:-2]}ейшим', '.ППмТ'),
        WordForm(f'{name[:-2]}ейшем', '.ППмП'),
        WordForm(f'{name[:-2]}ейшая', '.ППжИ'),
        WordForm(f'{name[:-2]}ейшей', '.ППжР'),
        WordForm(f'{name[:-2]}ейшей', '.ППжД'),
        WordForm(f'{name[:-2]}ейшую', '.ППжВ'),
        WordForm(f'{name[:-2]}ейшей', '.ППжТ1'),
        WordForm(f'{name[:-2]}ейшею', '.ППжТ2'),
        WordForm(f'{name[:-2]}ейшей', '.ППжП'),
        WordForm(f'{name[:-2]}ейшее', '.ППсИ'),
        WordForm(f'{name[:-2]}ейшего', '.ППсР'),
        WordForm(f'{name[:-2]}ейшему', '.ППсД'),
        WordForm(f'{name[:-2]}ейшее', '.ППсВ'),
        WordForm(f'{name[:-2]}ейшим', '.ППсТ'),
        WordForm(f'{name[:-2]}ейшем', '.ППсП'),
        WordForm(f'{name[:-2]}ейшие', '.ППмнИ'),
        WordForm(f'{name[:-2]}ейших', '.ППмнР'),
        WordForm(f'{name[:-2]}ейшим', '.ППмнД'),
        WordForm(f'{name[:-2]}ейшие', '.ППмнВ'),
        WordForm(f'{name[:-2]}ейшими', '.ППмнТ'),
        WordForm(f'{name[:-2]}ейших', '.ППмнП'),
    ]
    return word_forms
