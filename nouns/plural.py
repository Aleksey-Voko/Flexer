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
        'V1': get_plural_v1,
        'V2': get_plural_v2,
        'I1+12': get_plural_v1_v2,
        'I1+13е': get_plural_v1_13e,
        'I1*+16е*': get_plural_i1_prim_16e_prim,
        'I1*+16о*': get_plural_i1_prim_16o_prim,
        'I4*+19е*': get_plural_i4_prim_19e,
        'I5+16': get_plural_i5_16,
        'I6+7': get_plural_i6_7,
        'I6+17': get_plural_i6_17,
        'I11+2***': get_plural_i11_2_3prim,
        'I16+16о': get_plural_i16_16o,
        'I16е*+16о*': get_plural_i16e_prim_16o_prim,
        'I17е+6': get_plural_i16e_6,
        'I19+6': get_plural_i19_6,
        'I19е+6': get_plural_i19e_6,
        'I4+III7': get_plural_i4_iii7,
        'II1+3': get_plural_ii1_3,
        'II1+4': get_plural_ii1_4,
        'II1*+6*': get_plural_ii1_prim_6_prim,
        'II3*+6е*': get_plural_ii3_prim_6e_prim,
        'II3*+6#е*': get_plural_ii3_prim_6_sharp_e_prim,
        'II6+1**': get_plural_ii6_1_2prim,
        'II6е+6о': get_plural_ii6e_6o,
        'II1+IV1': get_plural_ii1_iv1,
        'III2+12': get_plural_iii2_12,
        'III3+9': get_plural_iii3_9,
        'IV1+I1': get_plural_iv1_i1,
        'IV3+6е': get_plural_iv3_6e,
        'IV3+6#е': get_plural_iv3_6_sharp_e,
        'IV3*+6е*': get_plural_iv3_prim_6e_prim,
        'IV4+6': get_plural_iv4_6,
        'IV6|6': get_plural_iv6_6,
        'IV6+6е': get_plural_iv6_6e,
        'IV6*+6е*': get_plural_iv6_prim_6e_prim,
        'IV6+I13': get_plural_iv6_i13,
        'IV6*+I13*': get_plural_iv6_prim_i13_prim,
        'IV6+II5': get_plural_iv6_ii5,
        'IV6*+II5*': get_plural_iv6_prim_ii5_prim,
        'V2+II7': get_plural_v2_ii7,
        'I4|4': get_plural_i4_4,
        'I1&14о': get_plural_i1_14o,
        'I1&II2': get_plural_i1_ii2,
        'I1&III4': get_plural_i1_iii4,
        'I1&IV11': get_plural_i1_iv11,
        'I1&IV12': get_plural_i1_iv12,
        'I3&III9': get_plural_i3_iii19,
        'I4&III1': get_plural_i4_iii1,
        'I6&III3': get_plural_i6_iii3,
        'I12&IV13': get_plural_i12_iv13,
        'II1&III3': get_plural_ii1_iii3,
        'II1&III11': get_plural_ii1_iii11,
        'III3&IV6': get_plural_iii3_iv6,
        'IV2&6е': get_plural_iv2_6e,
    }
    return plural_tmpl[src_dict['Inf_6']](src_dict, singl_word_forms)


# I1
def get_plural_i1(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ов'
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
def get_plural_i2_2prim(src_dict, singl_word_forms) -> list:
    sep = list(filter(lambda x: x.idf == '.СеП', singl_word_forms))[0].name
    smni = sep
    smnr = f'{smni[:-1]}ев'
    if src_dict['Inf_0'] == 'неод':
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


# I3
def get_plural_i3(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = f'{smni[:-1]}ей'
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr = sei
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
def get_plural_ii1_2prim(_, singl_word_forms) -> list:
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
def get_plural_ii2(_, singl_word_forms) -> list:
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
    if src_dict['Inf_0'] == 'неод':
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
def get_plural_ii3_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr = f'{smni[:-1]}ев'
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
    if src_dict['Inf_0'] == 'неод':
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
def get_plural_iv6e(_, singl_word_forms) -> list:
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
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
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-4]}ята'
    smnr = f'{smni[:-1]}'
    if src_dict['Inf_0'] == 'неод':
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
def get_plural_iv13(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
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


# V1
def get_plural_v1(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    sep = list(filter(lambda x: x.idf == '.СеП', singl_word_forms))[0].name
    smni = sep
    smnr = sei
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# V2
def get_plural_v2(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni = f'{sei[:-2]}е'
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


# I1+12
def get_plural_v1_v2(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = sei
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1+13е
def get_plural_v1_13e(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}и'
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1*+16е*
def get_plural_i1_prim_16e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I1*+16о*
def get_plural_i1_prim_16o_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I4*+19е*
def get_plural_i4_prim_19e(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ей'
    smnr2 = f'{smni[:-2]}е{smni[-2]}ь'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I5+16
def get_plural_i5_16(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ей'
    smnr2 = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I6+7
def get_plural_i6_7(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr = f'{smni[:-1]}ей'
    if src_dict['Inf_0'] == 'неод':
        smnv = smni
    else:
        smnv = smnr
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnv, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni[:-1]}ьми', '.СмнТ2'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I6+17
def get_plural_i6_17(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ей'
    smnr2 = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I11+2***
def get_plural_i11_2_3prim(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}й'
    smnr2 = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I16+16о
def get_plural_i16_16o(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}'
    smnr2 = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr1, '.СмнВ2'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I16е*+16о*
def get_plural_i16e_prim_16o_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-2]}е{smni[-2]}'
    smnr2 = f'{smni[:-2]}о{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I17е+6
def get_plural_i16e_6(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-2]}е{smni[-2]}'
    smnr2 = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I19+6
def get_plural_i19_6(src_dict, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ь'
    smnr2 = f'{smni[:-1]}ей'
    if src_dict['Inf_0'] == 'неод':
        smnv_form = WordForm(smni, '.СмнВ')
        smnv1_form = ''
        smnv2_form = ''
    else:
        smnv_form = ''
        smnv1_form = WordForm(smnr1, '.СмнВ1')
        smnv2_form = WordForm(smnr2, '.СмнВ2'),
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        smnv_form,
        smnv1_form,
        smnv2_form,
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# I19е+6
def get_plural_i19e_6(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-2]}е{smni[-2]}ь'
    smnr2 = f'{smni[:-1]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# I4+III7
def get_plural_i4_iii7(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = ser
    smnr = f'{smni1[:-1]}ей'
    if src_dict['Inf_0'] == 'неод':
        smnv1_form = WordForm(smni1, '.СмнВ1')
        smnv2_form = WordForm(smni2, '.СмнВ2')
        smnv_form = ''
    else:
        smnv1_form = ''
        smnv2_form = ''
        smnv_form = WordForm(smnr, '.СмнВ')
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД'),
        smnv1_form,
        smnv2_form,
        smnv_form,
        WordForm(f'{smni1[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# II1+3
def get_plural_ii1_3(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ы'
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = f'{smni[:-1]}ев'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1+4
def get_plural_ii1_4(src_dict, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ы'
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = sei
    if src_dict['Inf_0'] == 'неод':
        smnv_form = WordForm(smni, '.СмнВ')
        smnv1_form = ''
        smnv2_form = ''
    else:
        smnv_form = ''
        smnv1_form = WordForm(smnr1, '.СмнВ1')
        smnv2_form = WordForm(smnr2, '.СмнВ2')
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        smnv_form,
        smnv1_form,
        smnv2_form,
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# II1*+6*
def get_plural_ii1_prim_6_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ов'
    smnr2 = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II3*+6е*
def get_plural_ii3_prim_6e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II3*+6#е*
def get_plural_ii3_prim_6_sharp_e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6+1**
def get_plural_ii6_1_2prim(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}'
    smnr2 = f'{smni[:-1]}ов'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II6е+6о
def get_plural_ii6e_6o(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-2]}е{smni[:-2]}'
    smnr2 = f'{smni[:-2]}о{smni[:-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# II1+IV1
def get_plural_ii1_iv1(src_dict, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}ы'
    smni2 = ser
    smnr = f'{smni1[:-1]}ов'
    if src_dict['Inf_0'] == 'неод':
        smnv1_form = WordForm(smni1, '.СмнВ1')
        smnv2_form = WordForm(smni2, '.СмнВ2')
        smnv_form = ''
    else:
        smnv1_form = ''
        smnv2_form = ''
        smnv_form = WordForm(smnr, '.СмнВ')
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        smnv1_form,
        smnv2_form,
        smnv_form,
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return list(filter(None, word_forms))


# III2+12
def get_plural_iii2_12(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-2]}ий'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# III3+9
def get_plural_iii3_9(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni = f'{ser[:-1]}ья'
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-2]}ей'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ям', '.СмнД'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni[:-1]}ями', '.СмнТ'),
        WordForm(f'{smni[:-1]}ях', '.СмнП'),
    ]
    return word_forms


# IV1+I1
def get_plural_iv1_i1(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = ser
    smni2 = f'{ser[:-1]}и'
    smnr = f'{smni1[:-1]}ов'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV3+6е
def get_plural_iv3_6e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV3+6#е
def get_plural_iv3_6_sharp_e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-3]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV3*+6е*
def get_plural_iv3_prim_6e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}ев'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV4+6
def get_plural_iv4_6(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}ей'
    smnr2 = f'{smni[:-1]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6|6
def get_plural_iv6_6(_, singl_word_forms) -> list:
    smni1 = list(filter(lambda x: x.idf == '.СеР1', singl_word_forms))[0].name
    smni2 = list(filter(lambda x: x.idf == '.СеР2', singl_word_forms))[0].name
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6+6е
def get_plural_iv6_6e(_, singl_word_forms) -> list:
    smni = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smnr1 = f'{smni[:-1]}'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+6е*
def get_plural_iv6_prim_6e_prim(src_dict, _) -> list:
    smni = src_dict['name']
    smnr1 = f'{smni[:-1]}'
    smnr2 = f'{smni[:-2]}е{smni[-2]}'
    word_forms = [
        WordForm(smni, '.СмнИ'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni[:-1]}ам', '.СмнД'),
        WordForm(smni, '.СмнВ'),
        WordForm(f'{smni[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6+I13
def get_plural_iv6_i13(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = ser
    smni2 = f'{ser[:-1]}и'
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+I13*
def get_plural_iv6_prim_i13_prim(src_dict, _) -> list:
    smni1 = src_dict['name']
    smni2 = f'{smni1[:-1]}и'
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6+II5
def get_plural_iv6_ii5(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni1 = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni2 = f'{sei[:-1]}ы'
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# IV6*+II5*
def get_plural_iv6_prim_ii5_prim(src_dict, _) -> list:
    smni1 = src_dict['name']
    smni2 = f'{smni1[:-1]}ы'
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# V2+II7
def get_plural_v2_ii7(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    smni1 = f'{sei[:-2]}е'
    smni2 = f'{sei[:-2]}ы'
    smnr = f'{smni1[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП'),
    ]
    return word_forms


# I4|4
def get_plural_i4_4(_, singl_word_forms) -> list:
    ser1 = list(filter(lambda x: x.idf == '.СеР1', singl_word_forms))[0].name
    ser2 = list(filter(lambda x: x.idf == '.СеР2', singl_word_forms))[0].name
    smni1 = f'{ser1[:-1]}и'
    smni2 = f'{ser2[:-1]}и'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(f'{smni1[:-1]}ей', '.СмнР1'),
        WordForm(f'{smni2[:-1]}ей', '.СмнР2'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# I1&14о
def get_plural_i1_14o(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{ser[:-4]}ятки'
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-2]}о{smni2[-2]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# I1&II2
def get_plural_i1_ii2(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei[:-2]}ы'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(f'{smni1[:-1]}ов', '.СмнР1'),
        WordForm(f'{smni2[:-1]}ов', '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# I1&III4
def get_plural_i1_iii4(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei[:-1]}чья'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(f'{smni1[:-1]}ов', '.СмнР1'),
        WordForm(f'{smni2[:-1]}ев', '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# I1&IV11
def get_plural_i1_iv11(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei[:-2]}ята'
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# I1&IV12
def get_plural_i1_iv12(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei[:-4]}ята'
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# I3&III9
def get_plural_i3_iii19(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{ser[:-1]}ья'
    smnr = f'{smni1[:-1]}ей'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr, '.СмнР'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smnr, '.СмнВ'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# I4&III1
def get_plural_i4_iii1(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei}я'
    smnr1 = f'{smni1[:-1]}ей'
    smnr2 = f'{smni2[:-1]}ев'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# I6&III3
def get_plural_i6_iii3(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = ser
    smni2 = f'{ser[:-1]}ья'
    smnr1 = f'{smni1[:-1]}ей'
    smnr2 = f'{smni2[:-1]}ев'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# I12&IV13
def get_plural_i12_iv13(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = f'{sei[:-4]}ата'
    smnr1 = sei
    smnr2 = f'{smni2[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# II1&III3
def get_plural_ii1_iii3(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}ы'
    smni2 = f'{ser[:-1]}ья'
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-1]}ев'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# II1&III11
def get_plural_ii1_iii11(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}ы'
    smni2 = f'{sei}овья'
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-2]}ей'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ям', '.СмнД2'),
        WordForm(smnr1, '.СмнВ1'),
        WordForm(smnr2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ями', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ях', '.СмнП2'),
    ]
    return word_forms


# III3&IV6
def get_plural_iii3_iv6(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}ья'
    smni2 = ser
    smnr1 = f'{smni1[:-1]}ев'
    smnr2 = f'{smni2[:-1]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# IV2&6е
def get_plural_iv2_6e(_, singl_word_forms) -> list:
    sei = list(filter(lambda x: x.idf == '.СеИ', singl_word_forms))[0].name
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{sei[:-2]}а'
    smni2 = ser
    smnr1 = f'{smni1[:-1]}ов'
    smnr2 = f'{smni2[:-2]}е{smni2[-2]}'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(f'{smni1[:-1]}ам', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(f'{smni1[:-1]}ами', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni1[:-1]}ах', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
    ]
    return word_forms


# I4&IV6&III3
def get_plural_i4_iv6_iii3(_, singl_word_forms) -> list:
    ser = list(filter(lambda x: x.idf == '.СеР', singl_word_forms))[0].name
    smni1 = f'{ser[:-1]}и'
    smni2 = ser
    smni3 = f'{ser[:-1]}ья'
    smnr1 = f'{smni1[:-1]}ей'
    smnr2 = f'{smni2[:-1]}'
    smnr3 = f'{smni3[:-1]}ев'
    word_forms = [
        WordForm(smni1, '.СмнИ1'),
        WordForm(smni2, '.СмнИ2'),
        WordForm(smni3, '.СмнИ3'),
        WordForm(smnr1, '.СмнР1'),
        WordForm(smnr2, '.СмнР2'),
        WordForm(smnr3, '.СмнР3'),
        WordForm(f'{smni1[:-1]}ям', '.СмнД1'),
        WordForm(f'{smni2[:-1]}ам', '.СмнД2'),
        WordForm(f'{smni3[:-1]}ям', '.СмнД3'),
        WordForm(smni1, '.СмнВ1'),
        WordForm(smni2, '.СмнВ2'),
        WordForm(smni3, '.СмнВ3'),
        WordForm(f'{smni1[:-1]}ями', '.СмнТ1'),
        WordForm(f'{smni2[:-1]}ами', '.СмнТ2'),
        WordForm(f'{smni3[:-1]}ями', '.СмнТ3'),
        WordForm(f'{smni1[:-1]}ях', '.СмнП1'),
        WordForm(f'{smni2[:-1]}ах', '.СмнП2'),
        WordForm(f'{smni3[:-1]}ях', '.СмнП3'),
    ]
    return word_forms
