"""Прилагательные полная форма"""

from word_form import WordForm


def get_full_forms(src_dict) -> list:
    full_tmpl = {
        'I1ж': get_full_i1g,
        'I2': get_full_i2,
        'I2*': get_full_i2_prim,
        'I2ж': get_full_i2g,
        'I3': get_full_i3,
        'I3-с': get_full_i3_c,
        'II1': get_full_ii1,
        'II1-с': get_full_ii1_c,
        'II1ж': get_full_ii1g,
        'II1с': get_full_ii1c,
        'II2': get_full_ii2,
        'II2-с': get_full_ii2_c,
        'II3': get_full_ii3,
        'III1': get_full_iii1,
        'III2': get_full_iii2,
        'III3': get_full_iii3,
        'IIIф': get_full_iiif,
    }
    return full_tmpl[src_dict['Inf_0']](src_dict)


# I1ж
def get_full_i1g(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmnv = f'{name[:-2]}ие'
    else:
        pmnv = f'{name[:-2]}их'
    word_forms = [
        WordForm(f'{name}', '.ПжИ'),
        WordForm(f'{name[:-2]}ей', '.ПжР'),
        WordForm(f'{name[:-2]}ей', '.ПжД'),
        WordForm(f'{name[:-2]}юю', '.ПжВ'),
        WordForm(f'{name[:-2]}ей', '.ПжТ1'),
        WordForm(f'{name[:-2]}ею', '.ПжТ2'),
        WordForm(f'{name[:-2]}ей', '.ПжП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
    ]
    if src_dict['Inf_5'] != 'е':
        return word_forms
    else:
        return word_forms[:7]


# I2
def get_full_i2(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ие'
    else:
        pmv = f'{name[:-2]}его'
        pmnv = f'{name[:-2]}их'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}его', '.ПмР'),
        WordForm(f'{name[:-2]}ему', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}им', '.ПмТ'),
        WordForm(f'{name[:-2]}ем', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name[:-2]}ей', '.ПжР'),
        WordForm(f'{name[:-2]}ей', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ей', '.ПжТ1'),
        WordForm(f'{name[:-2]}ею', '.ПжТ2'),
        WordForm(f'{name[:-2]}ей', '.ПжП'),
        WordForm(f'{name[:-2]}ее', '.ПсИ'),
        WordForm(f'{name[:-2]}его', '.ПсР'),
        WordForm(f'{name[:-2]}ему', '.ПсД'),
        WordForm(f'{name[:-2]}ее', '.ПсВ'),
        WordForm(f'{name[:-2]}им', '.ПсТ'),
        WordForm(f'{name[:-2]}ем', '.ПсП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
    ]
    return word_forms


# I2*
def get_full_i2_prim(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-4]}иеся'
    else:
        pmv = f'{name[:-4]}егося'
        pmnv = f'{name[:-4]}ихся'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-4]}егося', '.ПмР'),
        WordForm(f'{name[:-4]}емуся', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-4]}имся', '.ПмТ'),
        WordForm(f'{name[:-4]}емся', '.ПмП'),
        WordForm(f'{name[:-4]}аяся', '.ПжИ'),
        WordForm(f'{name[:-4]}ейся', '.ПжР'),
        WordForm(f'{name[:-4]}ейся', '.ПжД'),
        WordForm(f'{name[:-4]}уюся', '.ПжВ'),
        WordForm(f'{name[:-4]}ейся', '.ПжТ1'),
        WordForm(f'{name[:-4]}еюся', '.ПжТ2'),
        WordForm(f'{name[:-4]}ейся', '.ПжП'),
        WordForm(f'{name[:-4]}ееся', '.ПсИ'),
        WordForm(f'{name[:-4]}егося', '.ПсР'),
        WordForm(f'{name[:-4]}емуся', '.ПсД'),
        WordForm(f'{name[:-4]}ееся', '.ПсВ'),
        WordForm(f'{name[:-4]}имся', '.ПсТ'),
        WordForm(f'{name[:-4]}емся', '.ПсП'),
        WordForm(f'{name[:-4]}иеся', '.ПмнИ'),
        WordForm(f'{name[:-4]}ихся', '.ПмнР'),
        WordForm(f'{name[:-4]}имся', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-4]}имися', '.ПмнТ'),
        WordForm(f'{name[:-4]}ихся', '.ПмнП'),
    ]
    return word_forms


# I2ж
def get_full_i2g(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmnv = f'{name[:-2]}ие'
    else:
        pmnv = f'{name[:-2]}их'
    word_forms = [
        WordForm(f'{name}', '.ПжИ'),
        WordForm(f'{name[:-2]}ей', '.ПжР'),
        WordForm(f'{name[:-2]}ей', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ей', '.ПжТ1'),
        WordForm(f'{name[:-2]}ею', '.ПжТ2'),
        WordForm(f'{name[:-2]}ей', '.ПжП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
    ]
    return word_forms


# I3
def get_full_i3(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ие'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}их'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}им', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name[:-2]}ой', '.ПжР'),
        WordForm(f'{name[:-2]}ой', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ой', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name[:-2]}ой', '.ПжП'),
        WordForm(f'{name[:-2]}ое', '.ПсИ'),
        WordForm(f'{name[:-2]}ого', '.ПсР'),
        WordForm(f'{name[:-2]}ому', '.ПсД'),
        WordForm(f'{name[:-2]}ое', '.ПсВ'),
        WordForm(f'{name[:-2]}им', '.ПсТ'),
        WordForm(f'{name[:-2]}ом', '.ПсП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
    ]
    return word_forms


# I3-с
def get_full_i3_c(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ие'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}их'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}им', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name[:-2]}ой', '.ПжР'),
        WordForm(f'{name[:-2]}ой', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ой', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name[:-2]}ой', '.ПжП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
    ]
    return word_forms


# II1
def get_full_ii1(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ые'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}ым', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name[:-2]}ой', '.ПжР'),
        WordForm(f'{name[:-2]}ой', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ой', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name[:-2]}ой', '.ПжП'),
        WordForm(f'{name[:-2]}ое', '.ПсИ'),
        WordForm(f'{name[:-2]}ого', '.ПсР'),
        WordForm(f'{name[:-2]}ому', '.ПсД'),
        WordForm(f'{name[:-2]}ое', '.ПсВ'),
        WordForm(f'{name[:-2]}ым', '.ПсТ'),
        WordForm(f'{name[:-2]}ом', '.ПсП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II1-с
def get_full_ii1_c(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ые'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}ым', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name[:-2]}ой', '.ПжР'),
        WordForm(f'{name[:-2]}ой', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ой', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name[:-2]}ой', '.ПжП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II1ж
def get_full_ii1g(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmnv = f'{name[:-2]}ые'
    else:
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПжИ'),
        WordForm(f'{name[:-2]}ой', '.ПжР'),
        WordForm(f'{name[:-2]}ой', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name[:-2]}ой', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name[:-2]}ой', '.ПжП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II1с
def get_full_ii1c(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmnv = f'{name[:-2]}ые'
    else:
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПсИ'),
        WordForm(f'{name[:-2]}ого', '.ПсР'),
        WordForm(f'{name[:-2]}ому', '.ПсД'),
        WordForm(f'{name}', '.ПсВ'),
        WordForm(f'{name[:-2]}ым', '.ПсТ'),
        WordForm(f'{name[:-2]}ом', '.ПсП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II2
def get_full_ii2(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ые'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}ым', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name}', '.ПжР'),
        WordForm(f'{name}', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name}', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name}', '.ПжП'),
        WordForm(f'{name[:-2]}ое', '.ПсИ'),
        WordForm(f'{name[:-2]}ого', '.ПсР'),
        WordForm(f'{name[:-2]}ому', '.ПсД'),
        WordForm(f'{name[:-2]}ое', '.ПсВ'),
        WordForm(f'{name[:-2]}ым', '.ПсТ'),
        WordForm(f'{name[:-2]}ом', '.ПсП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II2-с
def get_full_ii2_c(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ые'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}ых'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}ым', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name}', '.ПжР'),
        WordForm(f'{name}', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name}', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name}', '.ПжП'),
        WordForm(f'{name[:-2]}ые', '.ПмнИ'),
        WordForm(f'{name[:-2]}ых', '.ПмнР'),
        WordForm(f'{name[:-2]}ым', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ыми', '.ПмнТ'),
        WordForm(f'{name[:-2]}ых', '.ПмнП'),
    ]
    return word_forms


# II3
def get_full_ii3(src_dict) -> list:
    name = src_dict['name']
    if src_dict['Inf_4'] != 'о':
        pmv = f'{name}'
        pmnv = f'{name[:-2]}ие'
    else:
        pmv = f'{name[:-2]}ого'
        pmnv = f'{name[:-2]}их'

    word_forms = [
        WordForm(f'{name}', '.ПмИ'),
        WordForm(f'{name[:-2]}ого', '.ПмР'),
        WordForm(f'{name[:-2]}ому', '.ПмД'),
        WordForm(pmv, '.ПмВ'),
        WordForm(f'{name[:-2]}им', '.ПмТ'),
        WordForm(f'{name[:-2]}ом', '.ПмП'),
        WordForm(f'{name[:-2]}ая', '.ПжИ'),
        WordForm(f'{name}', '.ПжР'),
        WordForm(f'{name}', '.ПжД'),
        WordForm(f'{name[:-2]}ую', '.ПжВ'),
        WordForm(f'{name}', '.ПжТ1'),
        WordForm(f'{name[:-2]}ою', '.ПжТ2'),
        WordForm(f'{name}', '.ПжП'),
        WordForm(f'{name[:-2]}ое', '.ПсИ'),
        WordForm(f'{name[:-2]}ого', '.ПсР'),
        WordForm(f'{name[:-2]}ому', '.ПсД'),
        WordForm(f'{name[:-2]}ое', '.ПсВ'),
        WordForm(f'{name[:-2]}им', '.ПсТ'),
        WordForm(f'{name[:-2]}ом', '.ПсП'),
        WordForm(f'{name[:-2]}ие', '.ПмнИ'),
        WordForm(f'{name[:-2]}их', '.ПмнР'),
        WordForm(f'{name[:-2]}им', '.ПмнД'),
        WordForm(pmnv, '.ПмнВ'),
        WordForm(f'{name[:-2]}ими', '.ПмнТ'),
        WordForm(f'{name[:-2]}их', '.ПмнП'),
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
