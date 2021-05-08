"""Существительные множественное число"""
from word_form import WordForm


def get_plural_forms(src_dict, singl_word_forms) -> list:
    plural_tmpl = {
        'I1': get_plural_i1,
        'I1*': get_plural_i1_prim,
        'I1**': get_plural_i1_2prim,
        'I2': get_plural_i2,
        'I2*': get_plural_i2_prim,
        'I2**': get_plural_i2_2prim,
        'I3': get_plural_i3,
        'I3*': get_plural_i3_prim,
        'I4': get_plural_i4,
        'I4*': get_plural_i4_prim,
        'I5': get_plural_i5,
        'I5**': get_plural_i5_2prim,
        'I6': get_plural_i6,
        'I7': get_plural_i7,
        'I7*': get_plural_i7_prim,
        'I7#е': get_plural_i7_sharp_e,
        'I8#ч': get_plural_i8_sharp_ch,
        'I8#ш': get_plural_i8_sharp_sh,
        'I9': get_plural_i9,
        'I10': get_plural_i10,
        'I11': get_plural_i11,
        'I11*': get_plural_i11_prim,
        'I12': get_plural_i12,
        'I13': get_plural_i13,
        'I13е': get_plural_i13e,
        'I13е**': get_plural_i13e_2prim,
        'I13о': get_plural_i13o,
        'I14о': get_plural_i14o,
        'I15о': get_plural_i15o,
        'I16': get_plural_i16,
        'I16*': get_plural_i16_prim,
        'I16е': get_plural_i16e,
        'I16е*': get_plural_i16e_prim,
        'I16е*-': get_plural_i16e_prim_dash,
        'I16#е': get_plural_i16sharp_e,
        'I16#е*': get_plural_i16sharp_e_prim,
        'I16#е*-': get_plural_i16sharp_e_prim_dash,
        'I16о': get_plural_i16o,
        'I16о*': get_plural_i16o_prim,
        'I17': get_plural_i17,
        'I17е': get_plural_i17e,
        'I17#е': get_plural_i17sharp_e,
        'I18е': get_plural_i18e,
        'I19': get_plural_i19,
        'I19е': get_plural_i19e,
        'I19е*': get_plural_i19e_prim,
        'I19о': get_plural_i19o,
        'I19#о': get_plural_i19_sharp_o,
        'II1': get_plural_ii1,
        'II1*': get_plural_ii1_prim,
        'II1**': get_plural_ii1_2prim,
        'II2': get_plural_ii2,
        'II3': get_plural_ii3,
        'II3*': get_plural_ii3_prim,
        'II4': get_plural_ii4,
        'II5': get_plural_ii5,
        'II6': get_plural_ii6,
        'II6*': get_plural_ii6_prim,
        'II6е': get_plural_ii6e,
        'II6е*': get_plural_ii6e_prim,
        'II6#е': get_plural_ii6_sharp_e,
        'II6#е*': get_plural_ii6_sharp_e_prim,
        'II6о': get_plural_ii6o,
        'II7': get_plural_ii7,
        'III1': get_plural_iii1,
        'III2': get_plural_iii2,
        'III2*': get_plural_iii2_prim,
        'III3': get_plural_iii3,
        'III4': get_plural_iii4,
        'III5': get_plural_iii5,
        'III6': get_plural_iii6,
        'III7': get_plural_iii7,
        'III7*': get_plural_iii7_prim,
        'III8': get_plural_iii8,
        'III9': get_plural_iii9,
        'III10': get_plural_iii10,
        'III11': get_plural_iii11,
        'III12': get_plural_iii12,
        'III12*': get_plural_iii12_prim,
        'IV1': get_plural_iv1,
        'IV2': get_plural_iv2,
        'IV3': get_plural_iv3,
        'IV3*': get_plural_iv3_prim,
        'IV4': get_plural_iv4,
        'IV5': get_plural_iv5,
        'IV6': get_plural_iv6,
        'IV6*': get_plural_iv6_prim,
        'IV6е': get_plural_iv6e,
        'IV6е*': get_plural_iv6e_prim,
        'IV6#е': get_plural_iv6_sharp_e,
        'IV6#е*': get_plural_iv6_sharp_e_prim,
        'IV6#и': get_plural_iv6_sharp_i,
        'IV6о': get_plural_iv6o,
        'IV7': get_plural_iv7,
        'IV7#я': get_plural_iv7_sharp_y,
        'IV8': get_plural_iv8,
        'IV9': get_plural_iv9,
        'IV10': get_plural_iv10,
        'IV11': get_plural_iv11,
        'IV12': get_plural_iv12,
        'IV13': get_plural_iv13,

        'I1&IV11': get_plural_i1_and_iv11,
        'I4+III7': get_plural_i4_and_iii7,
        'II1*+6*': get_plural_ii1_prim_and_6_prim,
        'II1+IV1': get_plural_ii1_and_iv1,
        'IV1+I1': get_plural_iv1_and_i1,
        'IV6*+I13*': get_plural_iv6_prim_and_i13,
        'IV6*+II5*': get_plural_iv6_prim_and_ii5_prim,
        'IV6+I13': get_plural_iv6_and_i13,
        'V2': get_plural_v2,
    }
    return plural_tmpl[src_dict['Inf_6']](src_dict, singl_word_forms)


# I1
def get_plural_i1(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ов'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1*
def get_plural_i1_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ов'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1**
def get_plural_i1_2prim(_, singl_word_forms) -> list:
    ser2 = list(filter(lambda x: x.idf == '.СеР2', singl_word_forms))[0].name
    smni = f'{ser2[:-1]}и'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(f'{smni[:-1]}ов', '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I2
def get_plural_i2(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I2*
def get_plural_i2_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I2**
def get_plural_i2_2prim(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I3
def get_plural_i3(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I3*
def get_plural_i3_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I4
def get_plural_i4(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I4*
def get_plural_i4_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I5
def get_plural_i5(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I5**
def get_plural_i5_2prim(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР1', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I6
def get_plural_i6(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I7
def get_plural_i7(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ьми', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I7*
def get_plural_i7_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ьми', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I7#е
def get_plural_i7_sharp_e(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-3]}е{sei[-2]}и'
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ьми', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I8#ч
def get_plural_i8_sharp_ch(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}чи'
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I8#ш
def get_plural_i8_sharp_sh(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}ши'
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I9
def get_plural_i9(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I10
def get_plural_i10(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}ий'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I11
def get_plural_i11(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}й'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I11*
def get_plural_i11_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}й'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I12
def get_plural_i12(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = sei
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I13
def get_plural_i13(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I13е
def get_plural_i13e(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-2]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I13е**
def get_plural_i13e_2prim(_, singl_word_forms) -> list:
    ser2 = list(filter(lambda x: x.idf == '.СеР2', singl_word_forms))[0].name
    smni = f'{ser2[:-1]}и'
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I13о
def get_plural_i13o(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-2]}о{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I14о
def get_plural_i14o(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-4]}ятки'
    smnr = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I15о
def get_plural_i15o(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-6]}ятки'
    smnr = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16
def get_plural_i16(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16*
def get_plural_i16_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е
def get_plural_i16e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е*
def get_plural_i16e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е*-
def get_plural_i16e_prim_dash(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16#е
def get_plural_i16sharp_e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-3]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16#е*
def get_plural_i16sharp_e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-3]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16#е*-
def get_plural_i16sharp_e_prim_dash(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16о
def get_plural_i16o(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}о{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16о*
def get_plural_i16o_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}о{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I17
def get_plural_i17(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I17е
def get_plural_i17e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I17#е
def get_plural_i17sharp_e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I18е
def get_plural_i18e(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-4]}ошки'
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I19
def get_plural_i19(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ь'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19е
def get_plural_i19e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}е{smni[-2]}ь'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19е*
def get_plural_i19e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}е{smni[-2]}ь'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19о
def get_plural_i19o(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}о{smni[-2]}ь'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19#о
def get_plural_i19_sharp_o(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-3]}о{ser[-2]}и'
    smnr = f'{smni[:-1]}ь'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# II1
def get_plural_ii1(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ы'
    smnr = f'{smni[:-1]}ов'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1*
def get_plural_ii1_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ов'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1**
def get_plural_ii1_2prim(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ов'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II2
def get_plural_ii2(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}ы'
    smnr = f'{smni[:-1]}ов'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II3
def get_plural_ii3(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ы'
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II3*
def get_plural_ii3_prim(src_dict, singl_word_forms) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II4
def get_plural_ii4(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ы'
    smnr = sei
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II5
def get_plural_ii5(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-1]}ы'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6
def get_plural_ii6(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6*
def get_plural_ii6_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6е
def get_plural_ii6e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}е{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6е*
def get_plural_ii6e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6#е
def get_plural_ii6_sharp_e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6#е*
def get_plural_ii6_sharp_e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6о
def get_plural_ii6o(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}о{smni[-2]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II7
def get_plural_ii7(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}ы'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# III1
def get_plural_iii1(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei}я'
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III2
def get_plural_iii2(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III2*
def get_plural_iii2_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III3
def get_plural_iii3(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ья'
    smnr = f'{smni[:-1]}ев'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III4
def get_plural_iii4(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-1]}чья'
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III5
def get_plural_iii5(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei}овья'
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III6
def get_plural_iii6(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}онья'
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III7
def get_plural_iii7(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III7*
def get_plural_iii7_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III8
def get_plural_iii8(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III9
def get_plural_iii9(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ья'
    smnr = f'{smni[:-2]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III10
def get_plural_iii10(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-1]}зья'
    smnr = f'{smni[:-2]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III11
def get_plural_iii11(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei}овья'
    smnr = f'{smni[:-2]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III12
def get_plural_iii12(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}ий'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III12*
def get_plural_iii12_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}ий'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# IV1
def get_plural_iv1(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ов'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV2
def get_plural_iv2(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}а'
    smnr = f'{smni[:-1]}ов'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV3
def get_plural_iv3(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV3*
def get_plural_iv3_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV4
def get_plural_iv4(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV5
def get_plural_iv5(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6
def get_plural_iv6(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*
def get_plural_iv6_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6е
def get_plural_iv6e(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6е*
def get_plural_iv6e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6#е
def get_plural_iv6_sharp_e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6#е*
def get_plural_iv6_sharp_e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6#и
def get_plural_iv6_sharp_i(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-3]}и{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6о
def get_plural_iv6o(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV7
def get_plural_iv7(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}а'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV7#я
def get_plural_iv7_sharp_y(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}а'
    smnr = f'{smni[:-3]}я{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV8
def get_plural_iv8(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-2]}а'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV9
def get_plural_iv9(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-1]}еса'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV10
def get_plural_iv10(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-2]}ева'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV11
def get_plural_iv11(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-2]}ята'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV12
def get_plural_iv12(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-4]}ята'
    smnr = f'{smni[:-1]}'
    inf_0 = src_dict['Inf_0']
    if inf_0 == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV13
def get_plural_iv13(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.И', singl_word_forms))[0].name
    smni = f'{sei[:-4]}ата'
    smnr = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1&IV11
def get_plural_i1_and_iv11(src_dict, singl_word_forms) -> list:
    name = src_dict['name']
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ1'),
        WordForm(f'{name[:-2]}ята', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР1'),
        WordForm(f'{name[:-2]}ят', '.СмнР2'),
        WordForm(f'{ser[:-1]}ам', '.СмнД1'),
        WordForm(f'{name[:-2]}ятам', '.СмнД2'),
        WordForm(f'{ser[:-1]}ов', '.СмнВ1'),
        WordForm(f'{name[:-2]}ят', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ1'),
        WordForm(f'{name[:-2]}ятами', '.СмнТ2'),
        WordForm(f'{ser[:-1]}ах', '.СмнП1'),
        WordForm(f'{name[:-2]}ятах', '.СмнП2'),
    ]
    return word_forms


# I4+III7
def get_plural_i4_and_iii7(src_dict, singl_word_forms) -> list:
    inf_0 = src_dict['Inf_0']
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv1 = WordForm(f'{ser[:-1]}и', '.СмнВ1')
        smnv2 = WordForm(f'{ser}', '.СмнВ2')
        smnv = ''
    else:
        smnv1 = ''
        smnv2 = ''
        smnv = WordForm(f'{ser[:-1]}и', '.СмнВ'),
    word_forms = [
        WordForm(f'{ser[:-1]}и', '.СмнИ1'),
        WordForm(f'{ser}', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ей', '.СмнР'),
        WordForm(f'{ser[:-1]}ям', '.СмнД'),
        smnv1,
        smnv2,
        smnv,
        WordForm(f'{ser[:-1]}ями', '.СмнТ'),
        WordForm(f'{ser[:-1]}ях', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# II1*+6*
def get_plural_ii1_prim_and_6_prim(src_dict, _) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СмнИ'),
        WordForm(f'{name[:-1]}ов', '.СмнР1'),
        WordForm(f'{name[:-1]}', '.СмнР2'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1+IV1
def get_plural_ii1_and_iv1(src_dict, singl_word_forms) -> list:
    inf_0 = src_dict['Inf_0']
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    if inf_0 == 'неод':
        smnv1 = WordForm(f'{ser[:-1]}ы', '.СмнВ1')
        smnv2 = WordForm(f'{ser}', '.СмнВ2')
        smnv = ''
    else:
        smnv1 = ''
        smnv2 = ''
        smnv = WordForm(f'{ser[:-1]}ов', '.СмнВ3'),
    word_forms = [
        WordForm(f'{ser[:-1]}ы', '.СмнИ1'),
        WordForm(f'{ser}', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        smnv1,
        smnv2,
        smnv,
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# IV1+I1
def get_plural_iv1_and_i1(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ1'),
        WordForm(f'{ser[:-1]}и', '.СмнИ2'),
        WordForm(f'{ser[:-1]}ов', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ1'),
        WordForm(f'{ser[:-1]}и', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+I13*
def get_plural_iv6_prim_and_i13(src_dict, _) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СмнИ1'),
        WordForm(f'{name[:-1]}и', '.СмнИ2'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ1'),
        WordForm(f'{name[:-1]}и', '.СмнВ2'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+II5*
def get_plural_iv6_prim_and_ii5_prim(src_dict, _) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name}', '.СмнИ1'),
        WordForm(f'{name[:-1]}ы', '.СмнИ2'),
        WordForm(f'{name[:-1]}', '.СмнР'),
        WordForm(f'{name[:-1]}ам', '.СмнД'),
        WordForm(f'{name}', '.СмнВ1'),
        WordForm(f'{name[:-1]}ы', '.СмнВ2'),
        WordForm(f'{name[:-1]}ами', '.СмнТ'),
        WordForm(f'{name[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6+I13
def get_plural_iv6_and_i13(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    word_forms = [
        WordForm(f'{ser}', '.СмнИ1'),
        WordForm(f'{ser[:-1]}и', '.СмнИ2'),
        WordForm(f'{ser[:-1]}', '.СмнР'),
        WordForm(f'{ser[:-1]}ам', '.СмнД'),
        WordForm(f'{ser}', '.СмнВ1'),
        WordForm(f'{ser[:-1]}и', '.СмнВ2'),
        WordForm(f'{ser[:-1]}ами', '.СмнТ'),
        WordForm(f'{ser[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# V2
def get_plural_v2(src_dict, _) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}е', '.СмнИ'),
        WordForm(f'{name[:-2]}', '.СмнР'),
        WordForm(f'{name[:-2]}ам', '.СмнД'),
        WordForm(f'{name[:-2]}', '.СмнВ'),
        WordForm(f'{name[:-2]}ами', '.СмнТ'),
        WordForm(f'{name[:-2]}ах', '.СмнП'),
    ]
    return word_forms
