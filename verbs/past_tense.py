"""Глаголы прошедшее время"""
from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_past_tense_forms(src_dict) -> list:
    past_tense_tmpl = {
        'П1': past_tense_p1,
        'П1-': past_tense_p1_dash,
        'П2': past_tense_p2,
        'П3': past_tense_p3,
        'П3г': past_tense_p3g,
        'П3г-': past_tense_p3g_dash,
        'П3к': past_tense_p3k,
        'П4г': past_tense_p4g,
        'П4к': past_tense_p4k,
        'П5': past_tense_p5,
        'П5-': past_tense_p5_dash,
        'П6': past_tense_p6,
        'П7': past_tense_p7,
        'П7б': past_tense_p7b,
        'П8': past_tense_p8,
        'П9': past_tense_p9,
        'П9-': past_tense_p9_dash,
        'П10о': past_tense_p10o,
        'П*': past_tense_p_prim,
    }
    return past_tense_tmpl[src_dict['Inf_4']](src_dict)


# П1
def past_tense_p1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}а', '.ГПж'),
            WordForm(f'{gpm}о', '.ГПс'),
            WordForm(f'{gpm}и', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}ась', '.ГПж'),
            WordForm(f'{gpm[:-2]}ось', '.ГПс'),
            WordForm(f'{gpm[:-2]}ись', '.ГПмн'),
        ]
    return word_forms


# П1-
def past_tense_p1_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ло', '.ГПс'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}лось', '.ГПс'),
        ]
    return word_forms


# П2
def past_tense_p2(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}л', '.ГПм'),
            WordForm(f'{name[:-4]}ла', '.ГПж'),
            WordForm(f'{name[:-4]}ло', '.ГПс'),
            WordForm(f'{name[:-4]}ли', '.ГПмн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}лся', '.ГПм'),
            WordForm(f'{name[:-6]}лась', '.ГПж'),
            WordForm(f'{name[:-6]}лось', '.ГПс'),
            WordForm(f'{name[:-6]}лись', '.ГПмн'),
        ]
    return word_forms


# П3
def past_tense_p3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}ся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П3г
def past_tense_p3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}г'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}гся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П3г-
def past_tense_p3g_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}г'
        word_forms = [
            WordForm(f'{gpm}ло', '.ГПс'),
        ]
    else:
        gpm = f'{name[:-4]}гся'
        word_forms = [
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
        ]
    return word_forms


# П3к
def past_tense_p3k(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}к'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}кся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П4г
def past_tense_p4g(src_dict) -> list:
    name = src_dict['name']
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}г'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-1]}ла', '.ГПж'),
            WordForm(f'{gnb1e[:-1]}ло', '.ГПс'),
            WordForm(f'{gnb1e[:-1]}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}гся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-3]}лась', '.ГПж'),
            WordForm(f'{gnb1e[:-3]}лось', '.ГПс'),
            WordForm(f'{gnb1e[:-3]}лись', '.ГПмн'),
        ]
    return word_forms


# П4к
def past_tense_p4k(src_dict) -> list:
    name = src_dict['name']
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-2]}к'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-1]}ла', '.ГПж'),
            WordForm(f'{gnb1e[:-1]}ло', '.ГПс'),
            WordForm(f'{gnb1e[:-1]}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-4]}кся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-3]}лась', '.ГПж'),
            WordForm(f'{gnb1e[:-3]}лось', '.ГПс'),
            WordForm(f'{gnb1e[:-3]}лись', '.ГПмн'),
        ]
    return word_forms


# П5
def past_tense_p5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}а', '.ГПж'),
            WordForm(f'{gpm}о', '.ГПс'),
            WordForm(f'{gpm}и', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}ась', '.ГПж'),
            WordForm(f'{gpm[:-2]}ось', '.ГПс'),
            WordForm(f'{gpm[:-2]}ись', '.ГПмн'),
        ]
    return word_forms


# П5-
def past_tense_p5_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ло', '.ГПс'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}лось', '.ГПс'),
        ]
    return word_forms


# П6
def past_tense_p6(src_dict) -> list:
    name = src_dict['name']
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-2]}ла', '.ГПж'),
            WordForm(f'{gnb1e[:-2]}ло', '.ГПс'),
            WordForm(f'{gnb1e[:-2]}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gnb1e[:-4]}лась', '.ГПж'),
            WordForm(f'{gnb1e[:-4]}лось', '.ГПс'),
            WordForm(f'{gnb1e[:-4]}лись', '.ГПмн'),
        ]
    return word_forms


# П7
def past_tense_p7(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}ся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П7б
def past_tense_p7b(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-3]}б'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-5]}бся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П8
def past_tense_p8(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-4]}л'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}а', '.ГПж'),
            WordForm(f'{gpm}о', '.ГПс'),
            WordForm(f'{gpm}и', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-6]}лся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}ась', '.ГПж'),
            WordForm(f'{gpm[:-2]}ось', '.ГПс'),
            WordForm(f'{gpm[:-2]}ись', '.ГПмн'),
        ]
    return word_forms


# П9
def past_tense_p9(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-4]}'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-6]}ся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П9-
def past_tense_p9_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ло', '.ГПс'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}лось', '.ГПс'),
        ]
    return word_forms


# П10о
def past_tense_p10o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        gpm = f'{name[:-4]}ос'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm}ла', '.ГПж'),
            WordForm(f'{gpm}ло', '.ГПс'),
            WordForm(f'{gpm}ли', '.ГПмн'),
        ]
    else:
        gpm = f'{name[:-6]}осся'
        word_forms = [
            WordForm(gpm, '.ГПм'),
            WordForm(f'{gpm[:-2]}лась', '.ГПж'),
            WordForm(f'{gpm[:-2]}лось', '.ГПс'),
            WordForm(f'{gpm[:-2]}лись', '.ГПмн'),
        ]
    return word_forms


# П*
def past_tense_p_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(name, '.ГПм'),
            WordForm(f'{name[:-2]}ла', '.ГПж'),
            WordForm(f'{name[:-2]}ло', '.ГПс'),
            WordForm(f'{name[:-2]}ли', '.ГПмн'),
        ]
    else:
        word_forms = [
            WordForm(name, '.ГПм'),
            WordForm(f'{name[:-4]}лась', '.ГПж'),
            WordForm(f'{name[:-4]}лось', '.ГПс'),
            WordForm(f'{name[:-4]}лись', '.ГПмн'),
        ]
    return word_forms
