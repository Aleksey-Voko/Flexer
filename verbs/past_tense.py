"""Глаголы прошедшее время"""

from word_form import WordForm


def get_past_tense_forms(src_dict) -> list:
    past_tense_tmpl = {
        'П1': past_tense_p1,
        'П1-': past_tense_p1_dash,
        'П10о': past_tense_p10o,
        'П2': past_tense_p2,
        'П3г': past_tense_p3g,
        'П5': past_tense_p5,
        'П7б': past_tense_p7b,
        'П9': past_tense_p9,
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
