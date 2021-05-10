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
        'III2': get_full_iii2,
        'III3': get_full_iii3,
        'IIIф': get_full_iiif,
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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


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
    return word_forms


# III1
def get_full_iii1(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name}ы'
    else:
        pmv = f'{name}а'
        pmnv = f'{name}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name}а', '.ПмР'),
        WordForm(f'{name}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name}ым', '.ПмТ'),
        WordForm(f'{name}ом', '.ПмП'),
        WordForm(f'{name}а', '.ПжИ'),
        WordForm(f'{name}ой', '.ПжР'),
        WordForm(f'{name}ой', '.ПжД'),
        WordForm(f'{name}у', '.ПжВ'),
        WordForm(f'{name}ой', '.ПжТ1'),
        WordForm(f'{name}ою', '.ПжТ2'),
        WordForm(f'{name}ой', '.ПжП'),
        WordForm(f'{name}о', '.ПсИ'),
        WordForm(f'{name}а', '.ПсР'),
        WordForm(f'{name}у', '.ПсД'),
        WordForm(f'{name}о', '.ПсВ'),
        WordForm(f'{name}ым', '.ПсТ'),
        WordForm(f'{name}ом', '.ПсП'),
        WordForm(f'{name}ы', '.ПмнИ'),
        WordForm(f'{name}ых', '.ПмнР'),
        WordForm(f'{name}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name}ыми', '.ПмнТ'),
        WordForm(f'{name}ых', '.ПмнП'),
    ]
    return word_forms


# III2
def get_full_iii2(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name}ы'
    else:
        pmv = f'{name}ого'
        pmnv = f'{name}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name}ого', '.ПмР'),
        WordForm(f'{name}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name}ым', '.ПмТ'),
        WordForm(f'{name}ом', '.ПмП'),
        WordForm(f'{name}а', '.ПжИ'),
        WordForm(f'{name}ой', '.ПжР'),
        WordForm(f'{name}ой', '.ПжД'),
        WordForm(f'{name}у', '.ПжВ'),
        WordForm(f'{name}ой', '.ПжТ1'),
        WordForm(f'{name}ою', '.ПжТ2'),
        WordForm(f'{name}ой', '.ПжП'),
        WordForm(f'{name}о', '.ПсИ'),
        WordForm(f'{name}ого', '.ПсР'),
        WordForm(f'{name}ому', '.ПсД'),
        WordForm(f'{name}о', '.ПсВ'),
        WordForm(f'{name}ым', '.ПсТ'),
        WordForm(f'{name}ом', '.ПсП'),
        WordForm(f'{name}ы', '.ПмнИ'),
        WordForm(f'{name}ых', '.ПмнР'),
        WordForm(f'{name}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name}ыми', '.ПмнТ'),
        WordForm(f'{name}ых', '.ПмнП'),
    ]
    return word_forms


# III3
def get_full_iii3(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ьи'
    else:
        pmv = f'{name[:-2]}ьего'
        pmnv = f'{name[:-2]}ьих'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ьего', '.ПмР'),
        WordForm(f'{name[:-2]}ьему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}ьим', '.ПмТ'),
        WordForm(f'{name[:-2]}ьем', '.ПмП'),
        WordForm(f'{name[:-2]}ья', '.ПжИ'),
        WordForm(f'{name[:-2]}ьей', '.ПжР'),
        WordForm(f'{name[:-2]}ьей', '.ПжД'),
        WordForm(f'{name[:-2]}ью', '.ПжВ'),
        WordForm(f'{name[:-2]}ьей', '.ПжТ1'),
        WordForm(f'{name[:-2]}ьею', '.ПжТ2'),
        WordForm(f'{name[:-2]}ьей', '.ПжП'),
        WordForm(f'{name[:-2]}ье', '.ПсИ'),
        WordForm(f'{name[:-2]}ьего', '.ПсР'),
        WordForm(f'{name[:-2]}ьему', '.ПсД'),
        WordForm(f'{name[:-2]}ье', '.ПсВ'),
        WordForm(f'{name[:-2]}ьим', '.ПсТ'),
        WordForm(f'{name[:-2]}ьем', '.ПсП'),
        WordForm(f'{name[:-2]}ьи', '.ПмнИ'),
        WordForm(f'{name[:-2]}ьих', '.ПмнР'),
        WordForm(f'{name[:-2]}ьим', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ьими', '.ПмнТ'),
        WordForm(f'{name[:-2]}ьих', '.ПмнП'),
    ]
    return word_forms


# IIIф
def get_full_iiif(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name}ы'
    else:
        pmv = f'{name}а'
        pmnv = f'{name}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name}а', '.ПмР'),
        WordForm(f'{name}у', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name}ым', '.ПмТ'),
        WordForm(f'{name}е', '.ПмП'),
        WordForm(f'{name}а', '.ПжИ'),
        WordForm(f'{name}ой', '.ПжР'),
        WordForm(f'{name}ой', '.ПжД'),
        WordForm(f'{name}у', '.ПжВ'),
        WordForm(f'{name}ой', '.ПжТ1'),
        WordForm(f'{name}ою', '.ПжТ2'),
        WordForm(f'{name}ой', '.ПжП'),
        WordForm(f'{name}ы', '.ПмнИ'),
        WordForm(f'{name}ых', '.ПмнР'),
        WordForm(f'{name}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name}ыми', '.ПмнТ'),
        WordForm(f'{name}ых', '.ПмнП'),
    ]
    return word_forms
