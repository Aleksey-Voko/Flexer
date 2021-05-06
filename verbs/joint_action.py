"""Глаголы форма совместного действия"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_joint_action_forms(src_dict) -> list:
    joint_action_tmpl = {
        'С': joint_action_c,
        'С(2)': joint_action_c2,
        'С(3)': joint_action_c3,
    }
    return joint_action_tmpl[src_dict['Inf_6']](src_dict)


# С
def joint_action_c(src_dict) -> list:
    name = src_dict['name']
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn}те', '.ГСДмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn[:-2]}тесь', '.ГСДмн'),
        ]
    return word_forms


# С(2)
def joint_action_c2(src_dict) -> list:
    name = src_dict['name']
    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn2 = list(filter(
        lambda x: x.idf == '.ГНБ1мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn1}те', '.ГСДмн1'),
            WordForm(f'{gnb1mn2}те', '.ГСДмн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn1[:-2]}тесь', '.ГСДмн1'),
            WordForm(f'{gnb1mn2[:-2]}тесь', '.ГСДмн2'),
        ]
    return word_forms


# С(3)
def joint_action_c3(src_dict) -> list:
    name = src_dict['name']
    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn2 = list(filter(
        lambda x: x.idf == '.ГНБ1мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn3 = list(filter(
        lambda x: x.idf == '.ГНБ1мн3',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{gnb1mn1}те', '.ГСДмн1'),
            WordForm(f'{gnb1mn2}те', '.ГСДмн2'),
            WordForm(f'{gnb1mn3}те', '.ГСДмн3'),
        ]
    else:
        word_forms = [
            WordForm(f'{gnb1mn1[:-2]}тесь', '.ГСДмн1'),
            WordForm(f'{gnb1mn2[:-2]}тесь', '.ГСДмн2'),
            WordForm(f'{gnb1mn3[:-2]}тесь', '.ГСДмн3'),
        ]
    return word_forms
