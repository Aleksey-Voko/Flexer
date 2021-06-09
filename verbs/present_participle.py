"""Деепричастие настоящего времени"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_present_participle(src_dict) -> list:
    present_participle_tmpl = {
        'ДН1': present_participle_dn1,
        'ДН2': present_participle_dn2,
        'ДН3': present_participle_dn3,
        'ДН4': present_participle_dn4,
        'ДН5': present_participle_dn5,
        'ДН1|1': present_participle_dn1_1,
        'ДН1|2': present_participle_dn1_2,
        'ДН2|1': present_participle_dn2_1,
        'ДН1|1|1': present_participle_dn1_1_1,
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


# ДН3
def present_participle_dn3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}я', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}ясь', '.ДН'),
        ]
    return word_forms


# ДН4
def present_participle_dn4(src_dict) -> list:
    name = src_dict['name']
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn[:-2]}я', '.ДН'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn[:-4]}ясь', '.ДН'),
        ]
    return word_forms


# ДН5
def present_participle_dn5(src_dict) -> list:
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name

    word_forms = [
        WordForm(f'{gnb2e[:-3]}учи', '.ДН'),
    ]

    return word_forms


# ДН1|1
def present_participle_dn1_1(src_dict) -> list:
    name = src_dict['name']
    gnb2e1 = list(filter(
        lambda x: x.idf == '.ГНБ2е1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2e2 = list(filter(
        lambda x: x.idf == '.ГНБ2е2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e1[:-3]}я', '.ДН1'),
            WordForm(f'{gnb2e2[:-3]}я', '.ДН2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e1[:-5]}ясь', '.ДН1'),
            WordForm(f'{gnb2e2[:-5]}ясь', '.ДН2'),
        ]
    return word_forms


# ДН1|2
def present_participle_dn1_2(src_dict) -> list:
    name = src_dict['name']
    gnb2e1 = list(filter(
        lambda x: x.idf == '.ГНБ2е1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2e2 = list(filter(
        lambda x: x.idf == '.ГНБ2е2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e1[:-3]}я', '.ДН1'),
            WordForm(f'{gnb2e2[:-3]}а', '.ДН2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e1[:-5]}ясь', '.ДН1'),
            WordForm(f'{gnb2e2[:-5]}ась', '.ДН2'),
        ]
    return word_forms


# ДН2|1
def present_participle_dn2_1(src_dict) -> list:
    name = src_dict['name']
    gnb2e1 = list(filter(
        lambda x: x.idf == '.ГНБ2е1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2e2 = list(filter(
        lambda x: x.idf == '.ГНБ2е2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e1[:-3]}а', '.ДН1'),
            WordForm(f'{gnb2e2[:-3]}я', '.ДН2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e1[:-5]}ась', '.ДН1'),
            WordForm(f'{gnb2e2[:-5]}ясь', '.ДН2'),
        ]
    return word_forms


# ДН1|1|1
def present_participle_dn1_1_1(src_dict) -> list:
    name = src_dict['name']
    gnb2e1 = list(filter(
        lambda x: x.idf == '.ГНБ2е1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2e2 = list(filter(
        lambda x: x.idf == '.ГНБ2е2',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2e3 = list(filter(
        lambda x: x.idf == '.ГНБ2е3',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e1[:-3]}я', '.ДН1'),
            WordForm(f'{gnb2e2[:-3]}я', '.ДН2'),
            WordForm(f'{gnb2e3[:-3]}я', '.ДН3'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e1[:-5]}ясь', '.ДН1'),
            WordForm(f'{gnb2e2[:-5]}ясь', '.ДН2'),
            WordForm(f'{gnb2e3[:-5]}ясь', '.ДН3'),
        ]
    return word_forms
