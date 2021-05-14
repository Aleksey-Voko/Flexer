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
        'I1&1#': get_singular_i1_and_1_sharp,
        'I3#&3#*': get_singular_i3_sharp_and_3_sharp_prim,
        'I5&II2*': get_singular_i5_and_ii2_prim,
        'I7&II4*': get_singular_i7_and_ii4_prim,
        'III1&1*': get_singular_iii1_and_1_prim,
        'II1/&1/*': get_singular_ii1_slash_1_slash_prim,
    }
    return singular_tmpl[src_dict['Inf_3']](src_dict)


# I1
def get_singular_i1(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei}а', '.СеР'),
        WordForm(f'{sei}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei}ом', '.СеТ'),
        WordForm(f'{sei}е', '.СеП'),
    ]
    return word_forms


# I1*
def get_singular_i1_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}а', '.СеР'),
        WordForm(f'{sei[:-2]}у', '.СеД'),
        WordForm(f'{sei[:-2]}а', '.СеВ'),
        WordForm(f'{sei[:-2]}ом', '.СеТ'),
        WordForm(f'{sei[:-2]}е', '.СеП'),
    ]
    return word_forms


# I1#
def get_singular_i1_sharp(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}{sei[-1]}ом', '.СеТ'),
        WordForm(f'{sei[:-2]}{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I1#ь
def get_singular_i1_sharp_soft(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}ь{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}ом', '.СеТ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I1#й
def get_singular_i1_sharp_j(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}й{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}й{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}ом', '.СеТ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I2
def get_singular_i2(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei}а', '.СеР'),
        WordForm(f'{sei}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei}ем', '.СеТ'),
        WordForm(f'{sei}е', '.СеП'),
    ]
    return word_forms


# I2#
def get_singular_i2_sharp(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}{sei[-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-2]}{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I2#ь
def get_singular_i2_sharp_soft(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}ь{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-2]}ь{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I2#й
def get_singular_i2_sharp_ii(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}й{sei[-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}й{sei[-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-2]}й{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# I3
def get_singular_i3(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-1]}я'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}я', '.СеР'),
        WordForm(f'{sei[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# I3#
def get_singular_i3_sharp(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-3]}{sei[-2]}я'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-3]}{sei[-2]}я', '.СеР'),
        WordForm(f'{sei[:-3]}{sei[-2]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-3]}{sei[-2]}ем', '.СеТ'),
        WordForm(f'{sei[:-3]}{sei[-2]}е', '.СеП'),
    ]
    return word_forms


# I3#ь
def get_singular_i3_sharp_soft(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-2]}ья'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}ья', '.СеР'),
        WordForm(f'{sei[:-2]}ью', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-2]}ьем', '.СеТ'),
        WordForm(f'{sei[:-2]}ье', '.СеП'),
    ]
    return word_forms


# I3#ь*
def get_singular_i3_sharp_soft_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-3]}ь{sei[-2]}я', '.СеР'),
        WordForm(f'{sei[:-3]}ь{sei[-2]}ю', '.СеД'),
        WordForm(f'{sei[:-3]}ь{sei[-2]}я', '.СеВ'),
        WordForm(f'{sei[:-3]}ь{sei[-2]}ем', '.СеТ'),
        WordForm(f'{sei[:-3]}ь{sei[-2]}е', '.СеП'),
    ]
    return word_forms


# I4
def get_singular_i4(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-1]}я'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}я', '.СеР'),
        WordForm(f'{sei[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-1]}и', '.СеП'),
    ]
    return word_forms


# I5
def get_singular_i5(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-1]}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}а', '.СеР'),
        WordForm(f'{sei[:-1]}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-1]}ом', '.СеТ'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# I6
def get_singular_i6(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei[:-1]}я'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}я', '.СеР'),
        WordForm(f'{sei[:-1]}ю', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei[:-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# I7
def get_singular_i7(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}а', '.СеР'),
        WordForm(f'{sei[:-1]}у', '.СеД'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei[:-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II1
def get_singular_ii1(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}ы', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ой', '.СеТ1'),
        WordForm(f'{sei[:-1]}ою', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II2
def get_singular_ii2(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ой', '.СеТ1'),
        WordForm(f'{sei[:-1]}ою', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II3
def get_singular_ii3(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}ы', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ1'),
        WordForm(f'{sei[:-1]}ею', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II4
def get_singular_ii4(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ1'),
        WordForm(f'{sei[:-1]}ею', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II5
def get_singular_ii5(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}ю', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ1'),
        WordForm(f'{sei[:-1]}ею', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II5*
def get_singular_ii5_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}ю', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# II6
def get_singular_ii6(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}и', '.СеД'),
        WordForm(f'{sei[:-1]}ю', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ1'),
        WordForm(f'{sei[:-1]}ею', '.СеТ2'),
        WordForm(f'{sei[:-1]}и', '.СеП'),
    ]
    return word_forms


# II4**
def get_singular_ii4_2prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ей', '.СеТ1'),
        WordForm(f'{sei[:-1]}ею', '.СеТ2'),
        WordForm(f'{sei[:-1]}ью', '.СеТ3'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# III1
def get_singular_iii1(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}и', '.СеД'),
        WordForm(f'{sei}', '.СеВ'),
        WordForm(f'{sei[:-1]}ью', '.СеТ'),
        WordForm(f'{sei[:-1]}и', '.СеП'),
    ]
    return word_forms


# III1#
def get_singular_iii1_sharp(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-3]}{sei[-2]}и', '.СеР'),
        WordForm(f'{sei[:-3]}{sei[-2]}и', '.СеД'),
        WordForm(f'{sei}', '.СеВ'),
        WordForm(f'{sei}ю', '.СеТ'),
        WordForm(f'{sei[:-3]}{sei[-2]}и', '.СеП'),
    ]
    return word_forms


# III2
def get_singular_iii2(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}ени', '.СеР'),
        WordForm(f'{sei[:-1]}ени', '.СеД'),
        WordForm(f'{sei}', '.СеВ'),
        WordForm(f'{sei[:-1]}енем', '.СеТ'),
        WordForm(f'{sei[:-1]}ени', '.СеП'),
    ]
    return word_forms


# III3
def get_singular_iii3(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}ери', '.СеР'),
        WordForm(f'{sei[:-1]}ери', '.СеД'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei[:-1]}ерью', '.СеТ'),
        WordForm(f'{sei[:-1]}ери', '.СеП'),
    ]
    return word_forms


# III4
def get_singular_iii4(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}и', '.СеД'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei[:-1]}ем', '.СеТ'),
        WordForm(f'{sei[:-1]}и', '.СеП'),
    ]
    return word_forms


# III5
def get_singular_iii5(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei}ти', '.СеР'),
        WordForm(f'{sei}ти', '.СеД'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei}тей', '.СеТ1'),
        WordForm(f'{sei}тею', '.СеТ1'),
        WordForm(f'{sei}ти', '.СеП'),
    ]
    return word_forms


# I1/*
def get_singular_i1_slash_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}а', '.СеР/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}у', '.СеД/'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ом', '.СеТ/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# I1/**
def get_singular_i1_slash_2prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(f'полу{sei[4:-1]}а', '.СеР/'),
        WordForm(f'полу{sei[4:-1]}у', '.СеД/'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'полу{sei[4:-1]}ом', '.СеТ/'),
        WordForm(f'полу{sei[4:-1]}е', '.СеП/'),
    ]
    return word_forms


# II1/
def get_singular_ii1_slash(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(sei, '.СеР/'),
        WordForm(f'{sei[:-1]}е', '.СеД/'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'{sei[:-1]}ой', '.СеТ/1'),
        WordForm(f'{sei[:-1]}ою', '.СеТ/2'),
        WordForm(f'{sei[:-1]}е', '.СеП/'),
    ]
    return word_forms


# II1/*
def get_singular_ii1_slash_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(f'{sei[:3]}у{sei[3:]}', '.СеР/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеД/'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ой', '.СеТ/1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ою', '.СеТ/2'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# II4**/*
def get_singular_ii4_2prim_slash_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(f'{sei[:3]}у{sei[3:]}', '.СеР/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеД/'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ей', '.СеТ/1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ею', '.СеТ/2'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ью', '.СеТ/3'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеП/'),
    ]
    return word_forms


# I1+2
def get_singular_i1_2(src_dict) -> list:
    sei = src_dict['name']
    if src_dict['Inf_0'] == 'неод':
        sev = sei
    else:
        sev = f'{sei}а'
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei}а', '.СеР'),
        WordForm(f'{sei}у', '.СеД'),
        WordForm(sev, '.СеВ'),
        WordForm(f'{sei}ом', '.СеТ1'),
        WordForm(f'{sei}ем', '.СеТ2'),
        WordForm(f'{sei}е', '.СеП'),
    ]
    return word_forms


# I1#+2#
def get_singular_i1_sharp_2_sharp(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-2]}{sei[-1]}а', '.СеР'),
        WordForm(f'{sei[:-2]}{sei[-1]}у', '.СеД'),
        WordForm(f'{sei[:-2]}{sei[-1]}а', '.СеВ'),
        WordForm(f'{sei[:-2]}{sei[-1]}ом', '.СеТ1'),
        WordForm(f'{sei[:-2]}{sei[-1]}ем', '.СеТ2'),
        WordForm(f'{sei[:-2]}{sei[-1]}е', '.СеП'),
    ]
    return word_forms


# II2+4
def get_singular_i2_4(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР'),
        WordForm(f'{sei[:-1]}е', '.СеД'),
        WordForm(f'{sei[:-1]}у', '.СеВ'),
        WordForm(f'{sei[:-1]}ой', '.СеТ1'),
        WordForm(f'{sei[:-1]}ою', '.СеТ2'),
        WordForm(f'{sei[:-1]}ей', '.СеТ3'),
        WordForm(f'{sei[:-1]}ею', '.СеТ4'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# I1&1#
def get_singular_i1_and_1_sharp(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei}а', '.СеР1'),
        WordForm(f'{sei[:-2]}{sei[-1]}а', '.СеР2'),
        WordForm(f'{sei}у', '.СеД1'),
        WordForm(f'{sei[:-2]}{sei[-1]}у', '.СеД2'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei}ом', '.СеТ1'),
        WordForm(f'{sei[:-2]}{sei[-1]}ом', '.СеТ2'),
        WordForm(f'{sei}е', '.СеП1'),
        WordForm(f'{sei[:-2]}{sei[-1]}е', '.СеП2'),
    ]
    return word_forms


# I3#&3#*
def get_singular_i3_sharp_and_3_sharp_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-3]}{sei[-2]}я', '.СеР1'),
        WordForm(f'{sei[:3]}у{sei[3:-3]}{sei[-2]}я', '.СеР2'),
        WordForm(f'{sei[:-3]}{sei[-2]}ю', '.СеД1'),
        WordForm(f'{sei[:3]}у{sei[3:-3]}{sei[-2]}ю', '.СеД2'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei[:-3]}{sei[-2]}ем', '.СеТ1'),
        WordForm(f'{sei[:3]}у{sei[3:-3]}{sei[-2]}ем', '.СеТ2'),
        WordForm(f'{sei[:-3]}{sei[-2]}е', '.СеП1'),
        WordForm(f'{sei[:3]}у{sei[3:-3]}{sei[-2]}е', '.СеП2'),
    ]
    return word_forms


# I5&II2*
def get_singular_i5_and_ii2_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}а', '.СеР1'),
        WordForm(f'{sei[:-1]}и', '.СеР2'),
        WordForm(f'{sei[:-1]}у', '.СеД1'),
        WordForm(f'{sei[:-1]}е', '.СеД2'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei[:-1]}ом', '.СеТ1'),
        WordForm(f'{sei[:-1]}ой', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# I7&II4*
def get_singular_i7_and_ii4_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}а', '.СеР1'),
        WordForm(f'{sei[:-1]}и', '.СеР2'),
        WordForm(f'{sei[:-1]}у', '.СеД1'),
        WordForm(f'{sei[:-1]}е', '.СеД2'),
        WordForm(f'{sei[:-1]}а', '.СеВ1'),
        WordForm(f'{sei[:-1]}у', '.СеВ2'),
        WordForm(f'{sei[:-1]}ем', '.СеТ1'),
        WordForm(f'{sei[:-1]}ей', '.СеТ2'),
        WordForm(f'{sei[:-1]}е', '.СеП'),
    ]
    return word_forms


# III1&1*
def get_singular_iii1_and_1_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ'),
        WordForm(f'{sei[:-1]}и', '.СеР1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}и', '.СеР2'),
        WordForm(f'{sei[:-1]}и', '.СеД1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}и', '.СеД2'),
        WordForm(sei, '.СеВ'),
        WordForm(f'{sei}ю', '.СеТ1'),
        WordForm(f'{sei[:3]}у{sei[3:]}ю', '.СеТ2'),
        WordForm(f'{sei[:-1]}и', '.СеП1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}и', '.СеП1'),
    ]
    return word_forms


# II1/&1/*
def get_singular_ii1_slash_1_slash_prim(src_dict) -> list:
    sei = src_dict['name']
    word_forms = [
        WordForm(sei, '.СеИ/'),
        WordForm(sei, '.СеР/1'),
        WordForm(f'{sei[:3]}у{sei[3:]}', '.СеР/2'),
        WordForm(f'{sei[:-1]}е', '.СеД/1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеД/2'),
        WordForm(sei, '.СеВ/'),
        WordForm(f'{sei[:-1]}ой', '.СеТ/1'),
        WordForm(f'{sei[:-1]}ою', '.СеТ/2'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ой', '.СеТ/3'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}ою', '.СеТ/4'),
        WordForm(f'{sei[:-1]}е', '.СеП/1'),
        WordForm(f'{sei[:3]}у{sei[3:-1]}е', '.СеП/2'),
    ]
    return word_forms
