"""Прилагательные полная форма"""

from word_form import WordForm


def get_full_forms(src_dict) -> list:
    full_tmpl = {
        'I1': get_full_i1,
        'I1ж': get_full_i1zh,
        'I2': get_full_i2,
        'I2*': get_full_i2_prim,
        'I2м': get_full_i2m,
        'I2ж': get_full_i2zh,
        'I2с': get_full_i2s,
        'I2-с': get_full_i2_s,
        'I3': get_full_i3,
        'I3м': get_full_i3m,
        'I3с': get_full_i3s,
        'I3-с': get_full_i3_s,
        'I4': get_full_i4,
        'II1': get_full_ii1,
        'II1м': get_full_ii1m,
        'II1ж': get_full_ii1zh,
        'II1с': get_full_ii1s,
        'II1-с': get_full_ii1_s,
        'II1мн': get_full_ii1mn,
        'II2': get_full_ii2,
        'II2-с': get_full_ii2_s,
        'II3': get_full_ii3,
        'II3ж': get_full_ii3zh,
        'II3с': get_full_ii3s,
        'II3-с': get_full_ii3_s,
        'II4': get_full_ii4,
        'III1': get_full_iii1,
        'III1м': get_full_iii1m,
        'III1ж': get_full_iii1zh,
        'III1с': get_full_iii1s,
        'III2': get_full_iii2,
        'III3': get_full_iii3,
        'III4#': get_full_iii4_sharp,
        'IIIф': get_full_iiif,
        'IIIфм': get_full_iiifm,
    }
    return full_tmpl[src_dict['Inf_0']](src_dict)


# I1
def get_full_i1(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}его'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПмП'),
        WordForm(f'{pmi[:-2]}яя', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжР'),
        WordForm(f'{pmi[:-2]}ей', '.ПжД'),
        WordForm(f'{pmi[:-2]}юю', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ей', '.ПжП'),
        WordForm(f'{pmi[:-2]}ее', '.ПсИ'),
        WordForm(f'{pmi[:-2]}его', '.ПсР'),
        WordForm(f'{pmi[:-2]}ему', '.ПсД'),
        WordForm(f'{pmi[:-2]}ее', '.ПсВ'),
        WordForm(f'{pmi[:-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# I1ж
def get_full_i1zh(src_dict) -> list:
    pzhi = src_dict['name']
    pmni = f'{pzhi[:-2]}ие'
    pmnr = f'{pzhi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pzhi, '.ПжИ'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжР'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжД'),
        WordForm(f'{pzhi[:-2]}юю', '.ПжВ'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pzhi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pzhi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pzhi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pzhi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# I2
def get_full_i2(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}его'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжР'),
        WordForm(f'{pmi[:-2]}ей', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ей', '.ПжП'),
        WordForm(f'{pmi[:-2]}ее', '.ПсИ'),
        WordForm(f'{pmi[:-2]}его', '.ПсР'),
        WordForm(f'{pmi[:-2]}ему', '.ПсД'),
        WordForm(f'{pmi[:-2]}ее', '.ПсВ'),
        WordForm(f'{pmi[:-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# I2*
def get_full_i2_prim(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-4]}егося'
    pmni = f'{pmi[:-4]}иеся'
    pmnr = f'{pmi[:-4]}ихся'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-4]}емуся', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-4]}имся', '.ПмТ'),
        WordForm(f'{pmi[:-4]}емся', '.ПмП'),
        WordForm(f'{pmi[:-4]}аяся', '.ПжИ'),
        WordForm(f'{pmi[:-4]}ейся', '.ПжР'),
        WordForm(f'{pmi[:-4]}ейся', '.ПжД'),
        WordForm(f'{pmi[:-4]}уюся', '.ПжВ'),
        WordForm(f'{pmi[:-4]}ейся', '.ПжТ1'),
        WordForm(f'{pmi[:-4]}еюся', '.ПжТ2'),
        WordForm(f'{pmi[:-4]}ейся', '.ПжП'),
        WordForm(f'{pmi[:-4]}ееся', '.ПсИ'),
        WordForm(f'{pmi[:-4]}егося', '.ПсР'),
        WordForm(f'{pmi[:-4]}емуся', '.ПсД'),
        WordForm(f'{pmi[:-4]}ееся', '.ПсВ'),
        WordForm(f'{pmi[:-4]}имся', '.ПсТ'),
        WordForm(f'{pmi[:-4]}емся', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-4]}имся', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-4]}имися', '.ПмнТ'),
        WordForm(f'{pmi[:-4]}ихся', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# I2м
def get_full_i2m(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}его'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПмП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# I2ж
def get_full_i2zh(src_dict) -> list:
    pzhi = src_dict['name']
    pmni = f'{pzhi[:-2]}ие'
    pmnr = f'{pzhi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pzhi, '.ПжИ'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжР'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжД'),
        WordForm(f'{pzhi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pzhi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pzhi[:-2]}ей', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pzhi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pzhi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pzhi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# I2с
def get_full_i2s(src_dict) -> list:
    psi = src_dict['name']
    pmni = f'{psi[:-2]}ие'
    pmnr = f'{psi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(f'{psi[:-2]}ее', '.ПсИ'),
        WordForm(f'{psi[:-2]}его', '.ПсР'),
        WordForm(f'{psi[:-2]}ему', '.ПсД'),
        WordForm(psi, '.ПсВ'),
        WordForm(f'{psi[:-2]}им', '.ПсТ'),
        WordForm(f'{psi[:-2]}ем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{psi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{psi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{psi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# I2-с
def get_full_i2_s(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}его'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжР'),
        WordForm(f'{pmi[:-2]}ей', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ей', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# I3
def get_full_i3(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжР'),
        WordForm(f'{pmi[:-2]}ой', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ой', '.ПжП'),
        WordForm(f'{pmi[:-2]}ое', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ого', '.ПсР'),
        WordForm(f'{pmi[:-2]}ому', '.ПсД'),
        WordForm(f'{pmi[:-2]}ое', '.ПсВ'),
        WordForm(f'{pmi[:-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# I3м
def get_full_i3m(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# I3с
def get_full_i3s(src_dict) -> list:
    psi = src_dict['name']
    pmni = f'{psi[:-2]}ие'
    pmnr = f'{psi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(psi, '.ПсИ'),
        WordForm(f'{psi[:-2]}ого', '.ПсР'),
        WordForm(f'{psi[:-2]}ому', '.ПсД'),
        WordForm(psi, '.ПсВ'),
        WordForm(f'{psi[:-2]}им', '.ПсТ'),
        WordForm(f'{psi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{psi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{psi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{psi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# I3-с
def get_full_i3_s(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжР'),
        WordForm(f'{pmi[:-2]}ой', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# I4
def get_full_i4(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}оего', '.ПмР*'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(f'{pmi[:-2]}оему', '.ПмД*'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}оим', '.ПмТ*'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}оем', '.ПмП*'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжР'),
        WordForm(f'{pmi[:-2]}оей', '.ПжР*'),
        WordForm(f'{pmi[:-2]}ой', '.ПжД'),
        WordForm(f'{pmi[:-2]}оей', '.ПжД*'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}оей', '.ПжТ1*'),
        WordForm(f'{pmi[:-2]}оею', '.ПжТ2*'),
        WordForm(f'{pmi[:-2]}ой', '.ПжП'),
        WordForm(f'{pmi[:-2]}оей', '.ПжП*'),
        WordForm(f'{pmi[:-2]}ое', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ого', '.ПсР'),
        WordForm(f'{pmi[:-2]}оего', '.ПсР*'),
        WordForm(f'{pmi[:-2]}ому', '.ПсД'),
        WordForm(f'{pmi[:-2]}оему', '.ПсД*'),
        WordForm(f'{pmi[:-2]}ое', '.ПсВ'),
        WordForm(f'{pmi[:-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-2]}оим', '.ПсТ*'),
        WordForm(f'{pmi[:-2]}ом', '.ПсП'),
        WordForm(f'{pmi[:-2]}оем', '.ПсП*'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}оих', '.ПмнР*'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(f'{pmi[:-2]}оим', '.ПмнД*'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}оими', '.ПмнТ*'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
        WordForm(f'{pmi[:-2]}оих', '.ПмнП*'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:32]


# II1
def get_full_ii1(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжР'),
        WordForm(f'{pmi[:-2]}ой', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ой', '.ПжП'),
        WordForm(f'{pmi[:-2]}ое', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ого', '.ПсР'),
        WordForm(f'{pmi[:-2]}ому', '.ПсД'),
        WordForm(f'{pmi[:-2]}ое', '.ПсВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# II1м
def get_full_ii1m(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# II1ж
def get_full_ii1zh(src_dict) -> list:
    pzhi = src_dict['name']
    pmni = f'{pzhi[:-2]}ые'
    pmnr = f'{pzhi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pzhi, '.ПжИ'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжР'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжД'),
        WordForm(f'{pzhi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pzhi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pzhi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pzhi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pzhi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# II1с
def get_full_ii1s(src_dict) -> list:
    psi = src_dict['name']
    pmni = f'{psi[:-2]}ые'
    pmnr = f'{psi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(psi, '.ПсИ'),
        WordForm(f'{psi[:-2]}ого', '.ПсР'),
        WordForm(f'{psi[:-2]}ому', '.ПсД'),
        WordForm(f'{psi[:-2]}ое', '.ПсВ'),
        WordForm(f'{psi[:-2]}ым', '.ПсТ'),
        WordForm(f'{psi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{psi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{psi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{psi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# II1-с
def get_full_ii1_s(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжР'),
        WordForm(f'{pmi[:-2]}ой', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# II1мн
def get_full_ii1mn(src_dict) -> list:
    pmni = src_dict['name']
    pmnr = f'{pmni[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmni[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmni[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmni[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II2
def get_full_ii2(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(pmi, '.ПжР'),
        WordForm(pmi, '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(pmi, '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(pmi, '.ПжП'),
        WordForm(f'{pmi[:-2]}ое', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ого', '.ПсР'),
        WordForm(f'{pmi[:-2]}ому', '.ПсД'),
        WordForm(f'{pmi[:-2]}ое', '.ПсВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# II2-с
def get_full_ii2_s(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(pmi, '.ПжР'),
        WordForm(pmi, '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(pmi, '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(pmi, '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# II3
def get_full_ii3(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(pmi, '.ПжР'),
        WordForm(pmi, '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(pmi, '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(pmi, '.ПжП'),
        WordForm(f'{pmi[:-2]}ое', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ого', '.ПсР'),
        WordForm(f'{pmi[:-2]}ому', '.ПсД'),
        WordForm(f'{pmi[:-2]}ое', '.ПсВ'),
        WordForm(f'{pmi[:-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# II3ж
def get_full_ii3zh(src_dict) -> list:
    pzhi = src_dict['name']
    pmni = f'{pzhi[:-2]}ие'
    pmnr = f'{pzhi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pzhi, '.ПжИ'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжР'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжД'),
        WordForm(f'{pzhi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжТ1'),
        WordForm(f'{pzhi[:-2]}ою', '.ПжТ2'),
        WordForm(f'{pzhi[:-2]}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pzhi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pzhi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pzhi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# II3с
def get_full_ii3s(src_dict) -> list:
    psi = src_dict['name']
    pmni = f'{psi[:-2]}ие'
    pmnr = f'{psi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(psi, '.ПсИ'),
        WordForm(f'{psi[:-2]}ого', '.ПсР'),
        WordForm(f'{psi[:-2]}ому', '.ПсД'),
        WordForm(psi, '.ПсВ'),
        WordForm(f'{psi[:-2]}им', '.ПсТ'),
        WordForm(f'{psi[:-2]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{psi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{psi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{psi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# II3-с
def get_full_ii3_s(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ого'
    pmni = f'{pmi[:-2]}ие'
    pmnr = f'{pmi[:-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ом', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(pmi, '.ПжР'),
        WordForm(pmi, '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(pmi, '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ою', '.ПжТ2'),
        WordForm(pmi, '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# II4
def get_full_ii4(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}его'
    pmni = f'{pmi[:-2]}ые'
    pmnr = f'{pmi[:-2]}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПмП'),
        WordForm(f'{pmi[:-2]}ая', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжР'),
        WordForm(f'{pmi[:-2]}ей', '.ПжД'),
        WordForm(f'{pmi[:-2]}ую', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ей', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ею', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ей', '.ПжП'),
        WordForm(f'{pmi[:-2]}ее', '.ПсИ'),
        WordForm(f'{pmi[:-2]}его', '.ПсР'),
        WordForm(f'{pmi[:-2]}ему', '.ПсД'),
        WordForm(f'{pmi[:-2]}ее', '.ПсВ'),
        WordForm(f'{pmi[:-2]}ым', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# III1
def get_full_iii1(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi}а'
    pmni = f'{pmi}ы'
    pmnr = f'{pmi}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi}ым', '.ПмТ'),
        WordForm(f'{pmi}ом', '.ПмП'),
        WordForm(f'{pmi}а', '.ПжИ'),
        WordForm(f'{pmi}ой', '.ПжР'),
        WordForm(f'{pmi}ой', '.ПжД'),
        WordForm(f'{pmi}у', '.ПжВ'),
        WordForm(f'{pmi}ой', '.ПжТ1'),
        WordForm(f'{pmi}ою', '.ПжТ2'),
        WordForm(f'{pmi}ой', '.ПжП'),
        WordForm(f'{pmi}о', '.ПсИ'),
        WordForm(f'{pmi}а', '.ПсР'),
        WordForm(f'{pmi}у', '.ПсД'),
        WordForm(f'{pmi}о', '.ПсВ'),
        WordForm(f'{pmi}ым', '.ПсТ'),
        WordForm(f'{pmi}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi}ыми', '.ПмнТ'),
        WordForm(f'{pmi}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# III1м
def get_full_iii1m(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi}а'
    pmni = f'{pmi}ы'
    pmnr = f'{pmi}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi}ым', '.ПмТ'),
        WordForm(f'{pmi}ом', '.ПмП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi}ыми', '.ПмнТ'),
        WordForm(f'{pmi}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# III1ж
def get_full_iii1zh(src_dict) -> list:
    pzhi = src_dict['name']
    pmni = f'{pzhi[:-1]}ы'
    pmnr = f'{pzhi[:-1]}ых'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(pzhi, '.ПжИ'),
        WordForm(f'{pzhi[:-1]}ой', '.ПжР'),
        WordForm(f'{pzhi[:-1]}ой', '.ПжД'),
        WordForm(f'{pzhi[:-1]}у', '.ПжВ'),
        WordForm(f'{pzhi[:-1]}ой', '.ПжТ1'),
        WordForm(f'{pzhi[:-1]}ою', '.ПжТ2'),
        WordForm(f'{pzhi[:-1]}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pzhi[:-1]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pzhi[:-1]}ыми', '.ПмнТ'),
        WordForm(f'{pzhi[:-1]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# III1с
def get_full_iii1s(src_dict) -> list:
    psi = src_dict['name']
    pmni = f'{psi[:-1]}ы'
    pmnr = f'{psi[:-1]}ых'
    if src_dict['Inf_4'] != 'о':
        pmnv = pmni
    else:
        pmnv = pmnr
    word_forms = [
        WordForm(psi, '.ПсИ'),
        WordForm(f'{psi[:-1]}а', '.ПсР'),
        WordForm(f'{psi[:-1]}у', '.ПсД'),
        WordForm(psi, '.ПсВ'),
        WordForm(f'{psi[:-1]}ым', '.ПсТ'),
        WordForm(f'{psi[:-1]}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{psi[:-1]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{psi[:-1]}ыми', '.ПмнТ'),
        WordForm(f'{psi[:-1]}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]


# III2
def get_full_iii2(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi}ого'
    pmni = f'{pmi}ы'
    pmnr = f'{pmi}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi}ым', '.ПмТ'),
        WordForm(f'{pmi}ом', '.ПмП'),
        WordForm(f'{pmi}а', '.ПжИ'),
        WordForm(f'{pmi}ой', '.ПжР'),
        WordForm(f'{pmi}ой', '.ПжД'),
        WordForm(f'{pmi}у', '.ПжВ'),
        WordForm(f'{pmi}ой', '.ПжТ1'),
        WordForm(f'{pmi}ою', '.ПжТ2'),
        WordForm(f'{pmi}ой', '.ПжП'),
        WordForm(f'{pmi}о', '.ПсИ'),
        WordForm(f'{pmi}ого', '.ПсР'),
        WordForm(f'{pmi}ому', '.ПсД'),
        WordForm(f'{pmi}о', '.ПсВ'),
        WordForm(f'{pmi}ым', '.ПсТ'),
        WordForm(f'{pmi}ом', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi}ыми', '.ПмнТ'),
        WordForm(f'{pmi}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# III3
def get_full_iii3(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-2]}ьего'
    pmni = f'{pmi[:-2]}ьи'
    pmnr = f'{pmi[:-2]}ьих'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-2]}ьему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-2]}ьим', '.ПмТ'),
        WordForm(f'{pmi[:-2]}ьем', '.ПмП'),
        WordForm(f'{pmi[:-2]}ья', '.ПжИ'),
        WordForm(f'{pmi[:-2]}ьей', '.ПжР'),
        WordForm(f'{pmi[:-2]}ьей', '.ПжД'),
        WordForm(f'{pmi[:-2]}ью', '.ПжВ'),
        WordForm(f'{pmi[:-2]}ьей', '.ПжТ1'),
        WordForm(f'{pmi[:-2]}ьею', '.ПжТ2'),
        WordForm(f'{pmi[:-2]}ьей', '.ПжП'),
        WordForm(f'{pmi[:-2]}ье', '.ПсИ'),
        WordForm(f'{pmi[:-2]}ьего', '.ПсР'),
        WordForm(f'{pmi[:-2]}ьему', '.ПсД'),
        WordForm(f'{pmi[:-2]}ье', '.ПсВ'),
        WordForm(f'{pmi[:-2]}ьим', '.ПсТ'),
        WordForm(f'{pmi[:-2]}ьем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-2]}ьим', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-2]}ьими', '.ПмнТ'),
        WordForm(f'{pmi[:-2]}ьих', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# III4#
def get_full_iii4_sharp(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi[:-3]}{pmi[-2]}я'
    pmni = f'{pmi[:-3]}{pmi[-2]}и'
    pmnr = f'{pmi[:-3]}{pmi[-2]}их'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ю', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}им', '.ПмТ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ем', '.ПмП'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}я', '.ПжИ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ей', '.ПжР'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ей', '.ПжД'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ю', '.ПжВ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ей', '.ПжТ1'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ею', '.ПжТ2'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ей', '.ПжП'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}е', '.ПсИ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}я', '.ПсР'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ю', '.ПсД'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}е', '.ПсВ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}им', '.ПсТ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ем', '.ПсП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}ими', '.ПмнТ'),
        WordForm(f'{pmi[:-3]}{pmi[-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:19]


# IIIф
def get_full_iiif(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi}а'
    pmni = f'{pmi}ы'
    pmnr = f'{pmi}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi}ым', '.ПмТ'),
        WordForm(f'{pmi}е', '.ПмП'),
        WordForm(f'{pmi}а', '.ПжИ'),
        WordForm(f'{pmi}ой', '.ПжР'),
        WordForm(f'{pmi}ой', '.ПжД'),
        WordForm(f'{pmi}у', '.ПжВ'),
        WordForm(f'{pmi}ой', '.ПжТ1'),
        WordForm(f'{pmi}ою', '.ПжТ2'),
        WordForm(f'{pmi}ой', '.ПжП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi}ыми', '.ПмнТ'),
        WordForm(f'{pmi}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:13]


# IIIфм
def get_full_iiifm(src_dict) -> list:
    pmi = src_dict['name']
    pmr = f'{pmi}а'
    pmni = f'{pmi}ы'
    pmnr = f'{pmi}ых'
    if src_dict['Inf_4'] != 'о':
        pmv = pmi
        pmnv = pmni
    else:
        pmv = pmr
        pmnv = pmnr
    word_forms = [
        WordForm(pmi, '.ПмИ'),
        WordForm(pmr, '.ПмР'),
        WordForm(f'{pmi}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{pmi}ым', '.ПмТ'),
        WordForm(f'{pmi}е', '.ПмП'),
        WordForm(pmni, '.ПмнИ'),
        WordForm(pmnr, '.ПмнР'),
        WordForm(f'{pmi}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{pmi}ыми', '.ПмнТ'),
        WordForm(f'{pmi}ых', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:6]
