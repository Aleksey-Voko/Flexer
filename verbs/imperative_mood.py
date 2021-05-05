"""Глаголы повелительное наклонение"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_imperative_mood_forms(src_dict) -> list:
    imperative_mood_tmpl = {
        'Пв1': imperative_mood_pv1,
        'Пв1-': imperative_mood_pv1_dash,
        'Пв1*': imperative_mood_pv1_prim,
        'Пв1|2': imperative_mood_pv1_2,
        'Пв1|3': imperative_mood_pv1_3,
        'Пв2': imperative_mood_pv2,
        'Пв2-': imperative_mood_pv2_dash,
        'Пв2!': imperative_mood_pv2_excl,
        'Пв2!&3': imperative_mood_pv2_excl_and_3,
        'Пв2**': imperative_mood_pv2_2prim,
        'Пв2**-': imperative_mood_pv2_2prim_dash,
        'Пв2|2': imperative_mood_pv2_2,
        'Пв3': imperative_mood_pv3,
        'Пв3-': imperative_mood_pv3_dash,
        'Пв4': imperative_mood_pv4,
    }
    return imperative_mood_tmpl[src_dict['Inf_5']](src_dict)


# Пв1
def imperative_mood_pv1(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}й'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}йся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1-
def imperative_mood_pv1_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}й', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}йся', '.ГПве'),
        ]
    return word_forms


# Пв1*
def imperative_mood_pv1_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpve = f'{name[:-2]}й'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{name[:-4]}йся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1|2
def imperative_mood_pv1_2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв1|3
def imperative_mood_pv1_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}ь'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ься'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв2
def imperative_mood_pv2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}и'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}ись'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв2-
def imperative_mood_pv2_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}и', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}ись', '.ГПве'),
        ]
    return word_forms


# Пв2!
def imperative_mood_pv2_excl(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    return word_forms


# Пв2!&3
def imperative_mood_pv2_excl_and_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве1'),
            WordForm(f'{gnb3mn[:-2]}ь', '.ГПве2'),
            WordForm(gnb2mn, '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-2]}ьте', '.ГПвмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn[:-4]}ься', '.ГПве2'),
            WordForm(gnb2mn, '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-4]}ьтесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв2**
def imperative_mood_pv2_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(name, '.ГПве'),
            WordForm(f'{name}те', '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(name, '.ГПве'),
            WordForm(f'{name[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв2**-
def imperative_mood_pv2_2prim_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}и', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ись', '.ГПве'),
        ]
    return word_forms


# Пв2|2
def imperative_mood_pv2_2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}и'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}ись'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв3
def imperative_mood_pv3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}ь'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}ься'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв3-
def imperative_mood_pv3_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-2]}ь', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-4]}ься', '.ГПве'),
        ]
    return word_forms


# Пв4
def imperative_mood_pv4(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}ы', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ысь', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    return word_forms
