"""Причастие прошедшего времени страдательное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_passive_past_participle(src_dict) -> list:
    passive_past_participle_tmpl = {
        'ППС1': passive_past_participle_pps1,
        'ППС2': passive_past_participle_pps2,
        'ППС3': passive_past_participle_pps3,
        'ППС5ж': passive_past_participle_pps5g,
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
