"""Деепричастие настоящего времени"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_present_participle(src_dict) -> list:
    present_participle_tmpl = {
        'ДН1': present_participle_dn1,
        'ДН2': present_participle_dn2,
    }
    return present_participle_tmpl[src_dict['Inf_11']](src_dict)


# ДН1
def present_participle_dn1(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}я', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ясь', '.ДН'),
        ]
    return word_forms


# ДН2
def present_participle_dn2(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}а', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ась', '.ДН'),
        ]
    return word_forms
