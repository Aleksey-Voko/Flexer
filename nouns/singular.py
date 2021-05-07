"""Существительные единственное число"""

from word_form import WordForm


def get_singular_forms(src_dict) -> list:
    singular_tmpl = {
        'I1': get_singular_i1,
        'I1*': get_singular_i1_prim,
        'I1#': get_singular_i1_sharp,
        'I1#ь': get_singular_i1_sharp_soft,
        'I1#й': get_singular_i1_sharp_j,
        'I2': get_singular_i2,
        'I2#': get_singular_i2_sharp,
        'I2#ь': get_singular_i2_sharp_soft,
        'I2#й': get_singular_i2_sharp_ii,
        'I3': get_singular_i3,
        'I3#': get_singular_i3_sharp,
        'I3#ь': get_singular_i3_sharp_soft,
        'I3#ь*': get_singular_i3_sharp_soft_prim,
        'I4': get_singular_i4,
        'I5': get_singular_i5,
        'I6': get_singular_i6,
        'I7': get_singular_i7,
        'II1': get_singular_ii1,
        'II2': get_singular_ii2,
        'II3': get_singular_ii3,
        'II4': get_singular_ii4,
        'II5': get_singular_ii5,
        'II5*': get_singular_ii5_prim,
        'II6': get_singular_ii6,
        'II4**': get_singular_ii4_2prim,
        'III1': get_singular_iii1,
        'III1#': get_singular_iii1_sharp,
        'III2': get_singular_iii2,
        'III3': get_singular_iii3,
        'III4': get_singular_iii4,
        'III5': get_singular_iii5,
        'I1/*': get_singular_i1_slash_prim,
        'I1/**': get_singular_i1_slash_2prim,
        'II1/': get_singular_ii1_slash,
        'II1/*': get_singular_ii1_slash_prim,
        'II4**/*': get_singular_ii4_2prim_slash_prim,
        'I1+2': get_singular_i1_2,
        'I1#+2#': get_singular_i1_sharp_2_sharp,
        'II2+4': get_singular_i2_4,

        'I5&II2*': get_singular_i5_and_ii2_prim,
    }
    return singular_tmpl[src_dict['Inf_3']](src_dict)


# I1
def get_singular_i1(src_dict) -> list:
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


# I1*
def get_singular_i1_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}а', '.СеР'),
        WordForm(f'{name[:-2]}у', '.СеД'),
        WordForm(f'{name[:-2]}а', '.СеВ'),
        WordForm(f'{name[:-2]}ом', '.СеТ'),
        WordForm(f'{name[:-2]}е', '.СеП'),
    ]
    return word_forms


# I1#
def get_singular_i1_sharp(src_dict) -> list:
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


# I1#ь
def get_singular_i1_sharp_soft(src_dict) -> list:
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


# I1#й
def get_singular_i1_sharp_j(src_dict) -> list:
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


# I2
def get_singular_i2(src_dict) -> list:
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
def get_singular_i2_sharp(src_dict) -> list:
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


# I2#ь
def get_singular_i2_sharp_soft(src_dict) -> list:
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
        WordForm(f'{name[:-2]}ь{name[-1]}ем', '.СеТ'),
        WordForm(f'{name[:-2]}ь{name[-1]}е', '.СеП'),
    ]
    return word_forms


# I2#й
def get_singular_i2_sharp_ii(src_dict) -> list:
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
def get_singular_i3(src_dict) -> list:
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
def get_singular_i3_sharp(src_dict) -> list:
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


# I3#ь
def get_singular_i3_sharp_soft(src_dict) -> list:
    name = src_dict['name']
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        sev = f'{name}'
    else:
        sev = f'{name[:-2]}ья'
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}ья', '.СеР'),
        WordForm(f'{name[:-2]}ью', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{name[:-2]}ьем', '.СеТ'),
        WordForm(f'{name[:-2]}ье', '.СеП'),
    ]
    return word_forms


# I3#ь*
def get_singular_i3_sharp_soft_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-3]}ь{name[-2:-1]}я', '.СеР'),
        WordForm(f'{name[:-3]}ь{name[-2:-1]}ю', '.СеД'),
        WordForm(f'{name[:-3]}ь{name[-2:-1]}я', '.СеВ'),
        WordForm(f'{name[:-3]}ь{name[-2:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-3]}ь{name[-2:-1]}е', '.СеП'),
    ]
    return word_forms


# I4
def get_singular_i4(src_dict) -> list:
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
def get_singular_i5(src_dict) -> list:
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


# I6
def get_singular_i6(src_dict) -> list:
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
def get_singular_i7(src_dict) -> list:
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
def get_singular_ii1(src_dict) -> list:
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
def get_singular_ii2(src_dict) -> list:
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
def get_singular_ii3(src_dict) -> list:
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
def get_singular_ii4(src_dict) -> list:
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
def get_singular_ii5(src_dict) -> list:
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
def get_singular_ii5_prim(src_dict) -> list:
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
def get_singular_ii6(src_dict) -> list:
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


# II4**
def get_singular_ii4_2prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ей', '.СеТ1'),
        WordForm(f'{name[:-1]}ею', '.СеТ2'),
        WordForm(f'{name[:-1]}ью', '.СеТ3'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# III1
def get_singular_iii1(src_dict) -> list:
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


# III1#
def get_singular_iii1_sharp(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-3]}{name[-2:-1]}и', '.СеР'),
        WordForm(f'{name[:-3]}{name[-2:-1]}и', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name}ю', '.СеТ'),
        WordForm(f'{name[:-3]}{name[-2:-1]}и', '.СеП'),
    ]
    return word_forms


# III2
def get_singular_iii2(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}ени', '.СеР'),
        WordForm(f'{name[:-1]}ени', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name[:-1]}енем', '.СеТ'),
        WordForm(f'{name[:-1]}ени', '.СеП'),
    ]
    return word_forms


# III3
def get_singular_iii3(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}ери', '.СеР'),
        WordForm(f'{name[:-1]}ери', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name[:-1]}ерью', '.СеТ'),
        WordForm(f'{name[:-1]}ери', '.СеП'),
    ]
    return word_forms


# III4
def get_singular_iii4(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}и', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name[:-1]}ем', '.СеТ'),
        WordForm(f'{name[:-1]}и', '.СеП'),
    ]
    return word_forms


# III5
def get_singular_iii5(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name}ти', '.СеР'),
        WordForm(f'{name}ти', '.СеД'),
        WordForm(f'{name}', '.СеВ'),
        WordForm(f'{name}тей', '.СеТ1'),
        WordForm(f'{name}тею', '.СеТ1'),
        WordForm(f'{name}ти', '.СеП'),
    ]
    return word_forms


# I1/*
def get_singular_i1_slash_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ/'),
        WordForm(f'{name[:3]}у{name[3:-1]}а', '.СеР/'),
        WordForm(f'{name[:3]}у{name[3:-1]}у', '.СеД/'),
        WordForm(f'{name}', '.СеВ/'),
        WordForm(f'{name[:3]}у{name[3:-1]}ом', '.СеТ/'),
        WordForm(f'{name[:3]}у{name[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# I1/**
def get_singular_i1_slash_2prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ/'),
        WordForm(f'полу{name[3:-1]}а', '.СеР/'),
        WordForm(f'полу{name[3:-1]}у', '.СеД/'),
        WordForm(f'{name}', '.СеВ/'),
        WordForm(f'полу{name[3:-1]}ом', '.СеТ/'),
        WordForm(f'полу{name[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# II1/
def get_singular_ii1_slash(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ/'),
        WordForm(f'{name}', '.СеР/'),
        WordForm(f'{name[:-1]}е', '.СеД/'),
        WordForm(f'{name}', '.СеВ/'),
        WordForm(f'{name[:-1]}ой', '.СеТ/1'),
        WordForm(f'{name[:-1]}ою', '.СеТ/2'),
        WordForm(f'{name[:-1]}е', '.СеП/'),
    ]
    return word_forms


# II1/*
def get_singular_ii1_slash_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ/'),
        WordForm(f'{name[:3]}у{name[3:]}', '.СеР/'),
        WordForm(f'{name[:3]}у{name[3:-1]}е', '.СеД/'),
        WordForm(f'{name}', '.СеВ/'),
        WordForm(f'{name[:3]}у{name[3:-1]}ой', '.СеТ/1'),
        WordForm(f'{name[:3]}у{name[3:-1]}ою', '.СеТ/2'),
        WordForm(f'{name[:3]}у{name[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# II4**/*
def get_singular_ii4_2prim_slash_prim(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ/'),
        WordForm(f'{name[:3]}у{name[3:]}', '.СеР/'),
        WordForm(f'{name[:3]}у{name[3:-1]}е', '.СеД/'),
        WordForm(f'{name}', '.СеВ/'),
        WordForm(f'{name[:3]}у{name[3:-1]}ей', '.СеТ/1'),
        WordForm(f'{name[:3]}у{name[3:-1]}ею', '.СеТ/2'),
        WordForm(f'{name[:3]}у{name[3:-1]}ью', '.СеТ/3'),
        WordForm(f'{name[:3]}у{name[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# I1+2
def get_singular_i1_2(src_dict) -> list:
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
        WordForm(f'{name}ом', '.СеТ1'),
        WordForm(f'{name}ем', '.СеТ2'),
        WordForm(f'{name}е', '.СеП'),
    ]
    return word_forms


# I1#+2#
def get_singular_i1_sharp_2_sharp(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-2]}{name[-1]}а', '.СеР'),
        WordForm(f'{name[:-2]}{name[-1]}у', '.СеД'),
        WordForm(f'{name[:-2]}{name[-1]}а', '.СеВ'),
        WordForm(f'{name[:-2]}{name[-1]}ом', '.СеТ1'),
        WordForm(f'{name[:-2]}{name[-1]}ем', '.СеТ2'),
        WordForm(f'{name[:-2]}{name[-1]}е', '.СеП'),
    ]
    return word_forms


# II2+4
def get_singular_i2_4(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СеИ'),
        WordForm(f'{name[:-1]}и', '.СеР'),
        WordForm(f'{name[:-1]}е', '.СеД'),
        WordForm(f'{name[:-1]}у', '.СеВ'),
        WordForm(f'{name[:-1]}ой', '.СеТ1'),
        WordForm(f'{name[:-1]}ою', '.СеТ2'),
        WordForm(f'{name[:-1]}ей', '.СеТ3'),
        WordForm(f'{name[:-1]}ею', '.СеТ4'),
        WordForm(f'{name[:-1]}е', '.СеП'),
    ]
    return word_forms


# I5&II2*
def get_singular_i5_and_ii2_prim(src_dict) -> list:
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
