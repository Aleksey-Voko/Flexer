"""Существительные единственное число"""

from word_form import WordForm


def get_singular_forms(src_dict) -> list:
    singular_tmpl = {
        'I1': get_singl_i1,
        'I1#': get_singl_i1_sharp,
        'I1#й': get_singl_i1_sharp_ii,
        'I1#ь': get_singl_i1_sharp_soft,
        'I2': get_singl_i2,
        'I2#': get_singl_i2_sharp,
        'I2#й': get_singl_i2_sharp_ii,
        'I3': get_singl_i3,
        'I3#': get_singl_i3_sharp,
        'I4': get_singl_i4,
        'I5': get_singl_i5,
        'I5&II2*': get_singl_i5_and_ii2_prim,
        'I6': get_singl_i6,
        'I7': get_singl_i7,
        'II1': get_singl_ii1,
        'II2': get_singl_ii2,
        'II3': get_singl_ii3,
        'II4': get_singl_ii4,
        'II5': get_singl_ii5,
        'II5*': get_singl_ii5_prim,
        'II6': get_singl_ii6,
        'III1': get_singl_iii1,
    }
    return singular_tmpl[src_dict['Inf_3']](src_dict)


# I1
def get_singl_i1(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name}а', '.СеР'),
        WordForm(f'{name}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name}ом', '.СеТ'),
        WordForm(f'{name}е', '.СеП'),
    ]
    return word_forms


# I1#
def get_singl_i1_sharp(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}{name[-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}{name[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}{name[-1]}ом', '.СеТ'),
        WordForm(f'{name[:-2]}{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I1#й
def get_singl_i1_sharp_ii(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}й{name[-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}й{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}й{name[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}й{name[-1]}ом', '.СеТ'),
        WordForm(f'{name[:-2]}й{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I1#ь
def get_singl_i1_sharp_soft(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}ь{name[-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}ь{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}ь{name[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}ь{name[-1]}ом', '.СеТ'),
        WordForm(f'{name[:-2]}ь{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I2
def get_singl_i2(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name}а', '.СеР'),
        WordForm(f'{name}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name}ем', '.СеТ'),
        WordForm(f'{name}е', '.СеП'),
    ]
    return word_forms


# I2#
def get_singl_i2_sharp(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}{name[-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}{name[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}{name[-1]}ем', '.СеТ'),
        WordForm(f'{name[:-2]}{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I2#й
def get_singl_i2_sharp_ii(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}й{name[-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}й{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}й{name[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}й{name[-1]}ем', '.СеТ'),
        WordForm(f'{name[:-2]}й{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I3
def get_singl_i3(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-1]}я'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}я', '.СеР'),
        WordForm(f'{name[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# I3#
def get_singl_i3_sharp(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-3]}{name[-2]}я'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-3]}{name[-2]}я', '.СеР'),
        WordForm(f'{name[:-3]}{name[-2]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-3]}{name[-2]}ем', '.СеТ'),
        WordForm(f'{name[:-3]}{name[-2]}е', '.СеП'),
    ]
    return word_forms


# I4
def get_singl_i4(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-1]}я'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}я', '.СеР'),
        WordForm(f'{name[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-1]}и', '.СеП'),
    ]
    return word_forms


# I5
def get_singl_i5(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}а', '.СеР'),
        WordForm(f'{name[:-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-1]}ом', '.СеТ'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# I5&II2*
def get_singl_i5_and_ii2_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}а', '.СеР1'),
        WordForm(f'{name[:-1]}и', '.СеР2'),
        WordForm(f'{name[:-1]}у', '.СеД1'),
        WordForm(f'{name[:-1]}е', '.СеД2'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name[:-1]}ом', '.СеТ1'),
        WordForm(f'{name[:-1]}ой', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# I6
def get_singl_i6(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-1]}я'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}я', '.СеР'),
        WordForm(f'{name[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# I7
def get_singl_i7(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-1]}а'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}а', '.СеР'),
        WordForm(f'{name[:-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II1
def get_singl_ii1(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}ы', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ой', '.СеТ1'),
        WordForm(f'{name[:-1]}ою', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II2
def get_singl_ii2(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ой', '.СеТ1'),
        WordForm(f'{name[:-1]}ою', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II3
def get_singl_ii3(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}ы', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ1'),
        WordForm(f'{name[:-1]}ею', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II4
def get_singl_ii4(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ1'),
        WordForm(f'{name[:-1]}ею', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II5
def get_singl_ii5(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}ю', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ1'),
        WordForm(f'{name[:-1]}ею', '.СеТ2'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II5*
def get_singl_ii5_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}ю', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# II6
def get_singl_ii6(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}и', '.СеД'),
        WordForm(f'{name[:-1]}ю', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ1'),
        WordForm(f'{name[:-1]}ею', '.СеТ2'),
        WordForm(f'{name[:-1]}и', '.СеП'),
    ]
    return word_forms


# III1
def get_singl_iii1(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}и', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name[:-1]}ью', '.СеТ'),
        WordForm(f'{name[:-1]}и', '.СеП'),
    ]
    return word_forms
