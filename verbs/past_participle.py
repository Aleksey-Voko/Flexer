"""Деепричастие прошедшего времени"""

from verbs.past_tense import get_past_tense_forms
from verbs.present_future import get_present_future_forms
from verbs.present_participle import get_present_participle
from word_form import WordForm


def get_past_participle(src_dict) -> list:
    past_participle_tmpl = {
        'ДП1': past_participle_dp1,
        'ДП2': past_participle_dp2,
        'ДП2*': past_participle_dp2_prim,
        'ДП2!': past_participle_dp2_excl,
        'ДП3': past_participle_dp3,
        'ДП4': past_participle_dp4,
        'ДП5д': past_participle_dp5d,
        'ДП6': past_participle_dp6,
        'ДП7': past_participle_dp7,
        'ДП8': past_participle_dp8,
        'ДП9': past_participle_dp9,
        'ДП9&10': past_participle_dp9_and_10,
        'ДП9-&4': past_participle_dp9_dash_and_4,
        'ДП9-&6': past_participle_dp9_dash_and_6,
    }
    return past_participle_tmpl[src_dict['Inf_12']](src_dict)


# ДП1
def past_participle_dp1(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
        ]
    return word_forms


# ДП2
def past_participle_dp2(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП2*
def past_participle_dp2_prim(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e2 = list(filter(
        lambda x: x.idf == '.ГНБ2е2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(f'{gnb2e2[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(f'{gnb2e2[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП2!
def past_participle_dp2_excl(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    dn = list(filter(
        lambda x: x.idf == '.ДН',
        get_present_participle(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(dn, '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(dn, '.ДП!'),
        ]
    return word_forms


# ДП3
def past_participle_dp3(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}в', '.ДП'),
            WordForm(f'{gpm[:-1]}вши', '.ДП*'),
            WordForm(f'{gnb2e[:-3]}а', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}вшись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ась', '.ДП!'),
        ]
    return word_forms


# ДП4
def past_participle_dp4(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm}ши', '.ДП'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-2]}шись', '.ДП'),
        ]
    return word_forms


# ДП5д
def past_participle_dp5d(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm[:-1]}дши', '.ДП'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-3]}дшись', '.ДП'),
        ]
    return word_forms


# ДП6
def past_participle_dp6(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm}ши', '.ДП'),
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-2]}шись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП7
def past_participle_dp7(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gpm}ши', '.ДП'),
            WordForm(f'{gnb2e[:-3]}а', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gpm[:-2]}шись', '.ДП'),
            WordForm(f'{gnb2e[:-5]}ась', '.ДП!'),
        ]
    return word_forms


# ДП8
def past_participle_dp8(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb2e[:-3]}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb2e[:-5]}ясь', '.ДП!'),
        ]
    return word_forms


# ДП9
def past_participle_dp9(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}в', '.ДП'),
            WordForm(f'{name[:-2]}вши', '.ДП*'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-2]}вшись', '.ДП'),
        ]
    return word_forms


# ДП9&10
def past_participle_dp9_and_10(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}в', '.ДП1'),
            WordForm(f'{name[:-2]}вши', '.ДП1*'),
            WordForm(f'{name[:-4]}ши', '.ДП2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вшись', '.ДП1'),
            WordForm(f'{name[:-6]}шись', '.ДП2'),
        ]
    return word_forms


# ДП9-&4
def past_participle_dp9_dash_and_4(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}в', '.ДП1'),
            WordForm(f'{gpm}ши', '.ДП2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вшись', '.ДП1'),
            WordForm(f'{gpm[:-2]}шись', '.ДП2'),
        ]
    return word_forms


# ДП9-&6
def past_participle_dp9_dash_and_6(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}в', '.ДП1'),
            WordForm(f'{gpm}ши', '.ДП2'),
            WordForm(f'{gpm}я', '.ДП!'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вшись', '.ДП1'),
            WordForm(f'{gpm[:-2]}шись', '.ДП2'),
            WordForm(f'{gpm[:-2]}ясь', '.ДП!'),
        ]
    return word_forms
