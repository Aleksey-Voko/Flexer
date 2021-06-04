"""Глаголы повелительное наклонение"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_imperative_mood_forms(src_dict) -> list:
    imperative_mood_tmpl = {
        'Пв1': imperative_mood_pv1,
        'Пв1-': imperative_mood_pv1_dash,
        'Пв1*': imperative_mood_pv1_prim,
        'Пв1*-': imperative_mood_pv1_prim_dash,
        'Пв1е': imperative_mood_pv1_prim_e,
        'Пв2': imperative_mood_pv2,
        'Пв2-': imperative_mood_pv2_dash,
        'Пв2**-': imperative_mood_pv2_2prim_dash,
        'Пв2г-': imperative_mood_pv2g_dash,
        'Пв2**': imperative_mood_pv2_2prim,
        'Пв2!': imperative_mood_pv2_excl,
        'Пв2!*': imperative_mood_pv2_excl_dash,
        'Пв3': imperative_mood_pv3,
        'Пв3-': imperative_mood_pv3_dash,
        'Пв3**': imperative_mood_pv3_2prim,
        'Пв3***': imperative_mood_pv3_3prim,
        'Пв4': imperative_mood_pv4,
        'Пв5': imperative_mood_pv5,
        'Пв1|1': imperative_mood_pv1_1,
        'Пв1|2': imperative_mood_pv1_2,
        'Пв1|2!': imperative_mood_pv1_2_excl,
        'Пв1|3': imperative_mood_pv1_3,
        'Пв1зж&3': imperative_mood_pv1zzh_3,
        'Пв2|2': imperative_mood_pv2_2,
        'Пв2|2!': imperative_mood_pv2_2_excl,
        'Пв2&3': imperative_mood_pv2_3,
        'Пв2!&3': imperative_mood_pv2_excl_and_3,
        'Пв2*&3*': imperative_mood_pv2_prim_3_prim,
        'Пв2!+3*-': imperative_mood_pv2_excl_3_prim_dash,
        'Пв2*-+3': imperative_mood_pv2_prim_dash_3,
        'Пв1|2|2': imperative_mood_pv1_2_2,
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


# Пв1*-
def imperative_mood_pv1_prim_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpve = f'{name[:-2]}й'
        word_forms = [
            WordForm(gpve, '.ГПве'),
        ]
    else:
        gpve = f'{name[:-4]}йся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
        ]
    return word_forms


# Пв1е
def imperative_mood_pv1_prim_e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpve = f'{name[:-3]}ей'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{name[:-5]}ейся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
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


# Пв2г-
def imperative_mood_pv2g_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3e = list(filter(
        lambda x: x.idf == '.ГНБ3е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3e[:-3]}ги', '.ГПве'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3e[:-5]}гись', '.ГПве'),
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


# Пв2!*
def imperative_mood_pv2_excl_dash(src_dict) -> list:
    name = src_dict['name']
    gnb2mn = list(filter(
        lambda x: x.idf == '.ГНБ2мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}и', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ись', '.ГПве'),
            WordForm(gnb2mn, '.ГПвмн'),
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


# Пв3**
def imperative_mood_pv3_2prim(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn1[:-2]}ь'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn1[:-4]}ься'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв3***
def imperative_mood_pv3_3prim(src_dict) -> list:
    name = src_dict['name']
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(gnb2e, '.ГПве'),
            WordForm(f'{gnb2e}те', '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(gnb2e, '.ГПве'),
            WordForm(f'{gnb2e[:-2]}тесь', '.ГПвмн'),
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


# Пв5
def imperative_mood_pv5(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve = f'{gnb3mn[:-2]}'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve}те', '.ГПвмн'),
        ]
    else:
        gpve = f'{gnb3mn[:-4]}ся'
        word_forms = [
            WordForm(gpve, '.ГПве'),
            WordForm(f'{gpve[:-2]}тесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1|1
def imperative_mood_pv1_1(src_dict) -> list:
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
        gpve2 = f'{gnb3mn2[:-2]}й'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}йся'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
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


# Пв1|2!
def imperative_mood_pv1_2_excl(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn2 = list(filter(
        lambda x: x.idf == '.ГНБ2мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(gnb2mn2, '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(gnb2mn2, '.ГПвмн2'),
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


# Пв1зж&3
def imperative_mood_pv1zzh_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn[:-3]}зжай'
        gpve2 = f'{gnb3mn[:-2]}ь'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn[:-5]}зжайся'
        gpve2 = f'{gnb3mn[:-4]}ься'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
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


# Пв2|2!
def imperative_mood_pv2_2_excl(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb2mn2 = list(filter(
        lambda x: x.idf == '.ГНБ2мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}и'
        gpve2 = f'{gnb3mn2[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(gnb2mn2, '.ГПвмн2'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}ись'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(gnb2mn2, '.ГПвмн2'),
        ]
    return word_forms


# Пв2&3
def imperative_mood_pv2_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве1'),
            WordForm(f'{gnb3mn[:-2]}ь', '.ГПве2'),
            WordForm(f'{gnb3mn[:-2]}ите', '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-2]}ьте', '.ГПвмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn[:-4]}ься', '.ГПве2'),
            WordForm(f'{gnb3mn[:-4]}итесь', '.ГПвмн1'),
            WordForm(f'{gnb3mn[:-4]}ьтесь', '.ГПвмн2'),
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


# Пв2*&3*
def imperative_mood_pv2_prim_3_prim(src_dict) -> list:
    name = src_dict['name']
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn2[:-2]}и', '.ГПве1'),
            WordForm(f'{gnb3mn2[:-2]}ь', '.ГПве2'),
            WordForm(f'{gnb3mn2[:-2]}ите', '.ГПвмн1'),
            WordForm(f'{gnb3mn2[:-2]}ьте', '.ГПвмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn2[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn2[:-4]}ься', '.ГПве2'),
            WordForm(f'{gnb3mn2[:-4]}итесь', '.ГПвмн1'),
            WordForm(f'{gnb3mn2[:-4]}ьтесь', '.ГПвмн2'),
        ]
    return word_forms


# Пв2!+3*-
def imperative_mood_pv2_excl_3_prim_dash(src_dict) -> list:
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
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn[:-4]}ься', '.ГПве2'),
            WordForm(gnb2mn, '.ГПвмн'),
        ]
    return word_forms


# Пв2*-+3
def imperative_mood_pv2_prim_dash_3(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb3mn[:-2]}и', '.ГПве1'),
            WordForm(f'{gnb3mn[:-2]}ь', '.ГПве2'),
            WordForm(f'{gnb3mn[:-2]}ьте', '.ГПвмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb3mn[:-4]}ись', '.ГПве1'),
            WordForm(f'{gnb3mn[:-4]}ься', '.ГПве2'),
            WordForm(f'{gnb3mn[:-4]}ьтесь', '.ГПвмн'),
        ]
    return word_forms


# Пв1|2|2
def imperative_mood_pv1_2_2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn3 = list(filter(
        lambda x: x.idf == '.ГНБ3мн3',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpve1 = f'{gnb3mn1[:-2]}й'
        gpve2 = f'{gnb3mn2[:-2]}и'
        gpve3 = f'{gnb3mn3[:-2]}и'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(gpve3, '.ГПве3'),
            WordForm(f'{gpve1}те', '.ГПвмн1'),
            WordForm(f'{gpve2}те', '.ГПвмн2'),
            WordForm(f'{gpve3}те', '.ГПвмн3'),
        ]
    else:
        gpve1 = f'{gnb3mn1[:-4]}йся'
        gpve2 = f'{gnb3mn2[:-4]}ись'
        gpve3 = f'{gnb3mn3[:-2]}ись'
        word_forms = [
            WordForm(gpve1, '.ГПве1'),
            WordForm(gpve2, '.ГПве2'),
            WordForm(gpve3, '.ГПве3'),
            WordForm(f'{gpve1[:-2]}тесь', '.ГПвмн1'),
            WordForm(f'{gpve2[:-2]}тесь', '.ГПвмн2'),
            WordForm(f'{gpve3[:-2]}тесь', '.ГПвмн3'),
        ]
    return word_forms
