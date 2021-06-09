"""Причастие прошедшего времени страдательное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_passive_past_participle(src_dict) -> list:
    passive_past_participle_tmpl = {
        'ППС1': passive_past_participle_pps1,
        'ППС1*': passive_past_participle_pps1_prim,
        'ППС1**': passive_past_participle_pps1_2prim,
        'ППС2': passive_past_participle_pps2,
        'ППС2ж': passive_past_participle_pps2zh,
        'ППС3': passive_past_participle_pps3,
        'ППС4': passive_past_participle_pps4,
        'ППС4л': passive_past_participle_pps4l,
        'ППС4н': passive_past_participle_pps4n,
        'ППС5ж': passive_past_participle_pps5g,
        'ППС5ж*': passive_past_participle_pps5g_prim,
        'ППС6ж*': passive_past_participle_pps6g_prim,
        'ППС6о': passive_past_participle_pps6o,
        'ППС6ш': passive_past_participle_pps6sh,
        'ППС7': passive_past_participle_pps7,
        'ППС8': passive_past_participle_pps8,
        'ППС9': passive_past_participle_pps9,
        'ППС10': passive_past_participle_pps10,
        'ППС2&2*': passive_past_participle_pps2_2_prim,
        'ППС2&2о': passive_past_participle_pps2_2o,
        'ППС2&5ж*': passive_past_participle_pps2_5zh_prim,
        'ППС3&6ж': passive_past_participle_pps3_6zh,
    }
    return passive_past_participle_tmpl[src_dict['Inf_10']](src_dict)


# ППС1
def passive_past_participle_pps1(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-2]}нный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС1*
def passive_past_participle_pps1_prim(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'роз{name[3:-2]}нный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС1**
def passive_past_participle_pps1_2prim(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'пороз{name[5:-2]}нный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС2
def passive_past_participle_pps2(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb1e[:-1]}енный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС2ж
def passive_past_participle_pps2zh(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb1e[:-1]}денный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС3
def passive_past_participle_pps3(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-2]}тый'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-2]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-2]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-2]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-2]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС4
def passive_past_participle_pps4(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-3]}енный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС4л
def passive_past_participle_pps4l(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-3]}ленный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС4н
def passive_past_participle_pps4n(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-3]}ненный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС5ж
def passive_past_participle_pps5g(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-4]}женный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС5ж*
def passive_past_participle_pps5g_prim(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-4]}жденный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС6ж*
def passive_past_participle_pps6g_prim(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-5]}жденный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС6о
def passive_past_participle_pps6o(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-5]}ованный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС6ш
def passive_past_participle_pps6sh(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-5]}шленный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС7
def passive_past_participle_pps7(src_dict) -> list:
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb1mn[:-2]}енный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС8
def passive_past_participle_pps8(src_dict) -> list:
    gnb2e = list(filter(
        lambda x: x.idf == '.ГНБ2е',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb2e[:-3]}енный'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-3]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-3]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-3]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-3]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС9
def passive_past_participle_pps9(src_dict) -> list:
    name = src_dict['name']
    ppsmi = f'{name[:-3]}тый'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-2]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-2]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-2]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-2]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС10
def passive_past_participle_pps10(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    ppsmi = f'{gnb1e}тый'
    word_forms = [
        WordForm(ppsmi, '.ППСмИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСмР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСмД'),
        WordForm(ppsmi, '.ППСмВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСмП'),
        WordForm(f'{ppsmi[:-2]}ая', '.ППСжИ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжР'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжД'),
        WordForm(f'{ppsmi[:-2]}ую', '.ППСжВ'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжТ1'),
        WordForm(f'{ppsmi[:-2]}ою', '.ППСжТ2'),
        WordForm(f'{ppsmi[:-2]}ой', '.ППСжП'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсИ'),
        WordForm(f'{ppsmi[:-2]}ого', '.ППСсР'),
        WordForm(f'{ppsmi[:-2]}ому', '.ППСсД'),
        WordForm(f'{ppsmi[:-2]}ое', '.ППСсВ'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСсТ'),
        WordForm(f'{ppsmi[:-2]}ом', '.ППСсП'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнИ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнР'),
        WordForm(f'{ppsmi[:-2]}ым', '.ППСмнД'),
        WordForm(f'{ppsmi[:-2]}ые', '.ППСмнВ'),
        WordForm(f'{ppsmi[:-2]}ыми', '.ППСмнТ'),
        WordForm(f'{ppsmi[:-2]}ых', '.ППСмнП'),
        WordForm(f'{ppsmi[:-2]}', '.ППСКм'),
        WordForm(f'{ppsmi[:-2]}а', '.ППСКж'),
        WordForm(f'{ppsmi[:-2]}о', '.ППСКс'),
        WordForm(f'{ppsmi[:-2]}ы', '.ППСКмн'),
    ]

    return word_forms


# ППС2&2*
def passive_past_participle_pps2_2_prim(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    pps1mi = f'{gnb1e[:-1]}енный'
    pps2mi = f'{gnb1e[:2]}о{gnb1e[2:-1]}енный'
    word_forms = [
        WordForm(pps1mi, '.ППС1мИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1мР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1мД'),
        WordForm(pps1mi, '.ППС1мВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1мП'),
        WordForm(f'{pps1mi[:-2]}ая', '.ППС1жИ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жР'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жД'),
        WordForm(f'{pps1mi[:-2]}ую', '.ППС1жВ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жТ1'),
        WordForm(f'{pps1mi[:-2]}ою', '.ППС1жТ2'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жП'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1сР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1сД'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1сТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1сП'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнИ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнР'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мнД'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнВ'),
        WordForm(f'{pps1mi[:-2]}ыми', '.ППС1мнТ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнП'),
        WordForm(f'{pps1mi[:-3]}', '.ППСКм1'),
        WordForm(f'{pps1mi[:-3]}а', '.ППСКж1'),
        WordForm(f'{pps1mi[:-3]}о', '.ППСКс1'),
        WordForm(f'{pps1mi[:-3]}ы', '.ППСКмн1'),

        WordForm(pps2mi, '.ППС2мИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2мР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2мД'),
        WordForm(pps2mi, '.ППС2мВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2мП'),
        WordForm(f'{pps2mi[:-2]}ая', '.ППС2жИ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жР'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жД'),
        WordForm(f'{pps2mi[:-2]}ую', '.ППС2жВ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жТ1'),
        WordForm(f'{pps2mi[:-2]}ою', '.ППС2жТ2'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жП'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2сР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2сД'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2сТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2сП'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнИ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнР'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мнД'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнВ'),
        WordForm(f'{pps2mi[:-2]}ыми', '.ППС2мнТ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнП'),
        WordForm(f'{pps2mi[:-3]}', '.ППСКм2'),
        WordForm(f'{pps2mi[:-3]}а', '.ППСКж2'),
        WordForm(f'{pps2mi[:-3]}о', '.ППСКс2'),
        WordForm(f'{pps2mi[:-3]}ы', '.ППСКмн2'),
    ]

    return word_forms


# ППС2&2о
def passive_past_participle_pps2_2o(src_dict) -> list:
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    pps1mi = f'{gnb1e[:-1]}енный'
    pps2mi = f'{gnb1e[:-3]}ощенный'
    word_forms = [
        WordForm(pps1mi, '.ППС1мИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1мР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1мД'),
        WordForm(pps1mi, '.ППС1мВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1мП'),
        WordForm(f'{pps1mi[:-2]}ая', '.ППС1жИ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жР'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жД'),
        WordForm(f'{pps1mi[:-2]}ую', '.ППС1жВ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жТ1'),
        WordForm(f'{pps1mi[:-2]}ою', '.ППС1жТ2'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жП'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1сР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1сД'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1сТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1сП'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнИ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнР'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мнД'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнВ'),
        WordForm(f'{pps1mi[:-2]}ыми', '.ППС1мнТ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнП'),
        WordForm(f'{pps1mi[:-3]}', '.ППСКм1'),
        WordForm(f'{pps1mi[:-3]}а', '.ППСКж1'),
        WordForm(f'{pps1mi[:-3]}о', '.ППСКс1'),
        WordForm(f'{pps1mi[:-3]}ы', '.ППСКмн1'),

        WordForm(pps2mi, '.ППС2мИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2мР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2мД'),
        WordForm(pps2mi, '.ППС2мВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2мП'),
        WordForm(f'{pps2mi[:-2]}ая', '.ППС2жИ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жР'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жД'),
        WordForm(f'{pps2mi[:-2]}ую', '.ППС2жВ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жТ1'),
        WordForm(f'{pps2mi[:-2]}ою', '.ППС2жТ2'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жП'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2сР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2сД'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2сТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2сП'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнИ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнР'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мнД'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнВ'),
        WordForm(f'{pps2mi[:-2]}ыми', '.ППС2мнТ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнП'),
        WordForm(f'{pps2mi[:-3]}', '.ППСКм2'),
        WordForm(f'{pps2mi[:-3]}а', '.ППСКж2'),
        WordForm(f'{pps2mi[:-3]}о', '.ППСКс2'),
        WordForm(f'{pps2mi[:-3]}ы', '.ППСКмн2'),
    ]

    return word_forms


# ППС2&5ж*
def passive_past_participle_pps2_5zh_prim(src_dict) -> list:
    name = src_dict['name']
    gnb1e = list(filter(
        lambda x: x.idf == '.ГНБ1е',
        get_present_future_forms(src_dict)
    ))[0].name
    pps1mi = f'{gnb1e[:-1]}енный'
    pps2mi = f'{name[:-4]}жденный'
    word_forms = [
        WordForm(pps1mi, '.ППС1мИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1мР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1мД'),
        WordForm(pps1mi, '.ППС1мВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1мП'),
        WordForm(f'{pps1mi[:-2]}ая', '.ППС1жИ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жР'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жД'),
        WordForm(f'{pps1mi[:-2]}ую', '.ППС1жВ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жТ1'),
        WordForm(f'{pps1mi[:-2]}ою', '.ППС1жТ2'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жП'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1сР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1сД'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1сТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1сП'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнИ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнР'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мнД'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнВ'),
        WordForm(f'{pps1mi[:-2]}ыми', '.ППС1мнТ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнП'),
        WordForm(f'{pps1mi[:-3]}', '.ППСКм1'),
        WordForm(f'{pps1mi[:-3]}а', '.ППСКж1'),
        WordForm(f'{pps1mi[:-3]}о', '.ППСКс1'),
        WordForm(f'{pps1mi[:-3]}ы', '.ППСКмн1'),

        WordForm(pps2mi, '.ППС2мИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2мР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2мД'),
        WordForm(pps2mi, '.ППС2мВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2мП'),
        WordForm(f'{pps2mi[:-2]}ая', '.ППС2жИ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жР'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жД'),
        WordForm(f'{pps2mi[:-2]}ую', '.ППС2жВ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жТ1'),
        WordForm(f'{pps2mi[:-2]}ою', '.ППС2жТ2'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жП'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2сР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2сД'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2сТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2сП'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнИ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнР'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мнД'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнВ'),
        WordForm(f'{pps2mi[:-2]}ыми', '.ППС2мнТ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнП'),
        WordForm(f'{pps2mi[:-3]}', '.ППСКм2'),
        WordForm(f'{pps2mi[:-3]}а', '.ППСКж2'),
        WordForm(f'{pps2mi[:-3]}о', '.ППСКс2'),
        WordForm(f'{pps2mi[:-3]}ы', '.ППСКмн2'),
    ]

    return word_forms


# ППС3&6ж
def passive_past_participle_pps3_6zh(src_dict) -> list:
    name = src_dict['name']
    pps1mi = f'{name[:-2]}тый'
    pps2mi = f'{name[:-5]}женный'
    word_forms = [
        WordForm(pps1mi, '.ППС1мИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1мР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1мД'),
        WordForm(pps1mi, '.ППС1мВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1мП'),
        WordForm(f'{pps1mi[:-2]}ая', '.ППС1жИ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жР'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жД'),
        WordForm(f'{pps1mi[:-2]}ую', '.ППС1жВ'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жТ1'),
        WordForm(f'{pps1mi[:-2]}ою', '.ППС1жТ2'),
        WordForm(f'{pps1mi[:-2]}ой', '.ППС1жП'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сИ'),
        WordForm(f'{pps1mi[:-2]}ого', '.ППС1сР'),
        WordForm(f'{pps1mi[:-2]}ому', '.ППС1сД'),
        WordForm(f'{pps1mi[:-2]}ое', '.ППС1сВ'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1сТ'),
        WordForm(f'{pps1mi[:-2]}ом', '.ППС1сП'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнИ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнР'),
        WordForm(f'{pps1mi[:-2]}ым', '.ППС1мнД'),
        WordForm(f'{pps1mi[:-2]}ые', '.ППС1мнВ'),
        WordForm(f'{pps1mi[:-2]}ыми', '.ППС1мнТ'),
        WordForm(f'{pps1mi[:-2]}ых', '.ППС1мнП'),
        WordForm(f'{pps1mi[:-2]}', '.ППСКм1'),
        WordForm(f'{pps1mi[:-2]}а', '.ППСКж1'),
        WordForm(f'{pps1mi[:-2]}о', '.ППСКс1'),
        WordForm(f'{pps1mi[:-2]}ы', '.ППСКмн1'),

        WordForm(pps2mi, '.ППС2мИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2мР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2мД'),
        WordForm(pps2mi, '.ППС2мВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2мП'),
        WordForm(f'{pps2mi[:-2]}ая', '.ППС2жИ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жР'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жД'),
        WordForm(f'{pps2mi[:-2]}ую', '.ППС2жВ'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жТ1'),
        WordForm(f'{pps2mi[:-2]}ою', '.ППС2жТ2'),
        WordForm(f'{pps2mi[:-2]}ой', '.ППС2жП'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сИ'),
        WordForm(f'{pps2mi[:-2]}ого', '.ППС2сР'),
        WordForm(f'{pps2mi[:-2]}ому', '.ППС2сД'),
        WordForm(f'{pps2mi[:-2]}ое', '.ППС2сВ'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2сТ'),
        WordForm(f'{pps2mi[:-2]}ом', '.ППС2сП'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнИ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнР'),
        WordForm(f'{pps2mi[:-2]}ым', '.ППС2мнД'),
        WordForm(f'{pps2mi[:-2]}ые', '.ППС2мнВ'),
        WordForm(f'{pps2mi[:-2]}ыми', '.ППС2мнТ'),
        WordForm(f'{pps2mi[:-2]}ых', '.ППС2мнП'),
        WordForm(f'{pps2mi[:-3]}', '.ППСКм2'),
        WordForm(f'{pps2mi[:-3]}а', '.ППСКж2'),
        WordForm(f'{pps2mi[:-3]}о', '.ППСКс2'),
        WordForm(f'{pps2mi[:-3]}ы', '.ППСКмн2'),
    ]

    return word_forms
