"""Причастие настоящего времени страдательное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_passive_present_participle(src_dict) -> list:
    passive_present_tmpl = {
        'ПНС1': passive_present_participle_pns1,
        'ПНС2': passive_present_participle_pns2,
    }
    return passive_present_tmpl[src_dict['Inf_8']](src_dict)


# ПНС1
def passive_present_participle_pns1(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn[:-2]}емый'
    word_forms = [
        WordForm(pnsmi, '.ПНСмИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСмР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСмД'),
        WordForm(pnsmi, '.ПНСмВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСмП'),
        WordForm(f'{pnsmi[:-2]}ая', '.ПНСжИ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжР'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжД'),
        WordForm(f'{pnsmi[:-2]}ую', '.ПНСжВ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжТ1'),
        WordForm(f'{pnsmi[:-2]}ою', '.ПНСжТ2'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжП'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСсР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСсД'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСсТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСсП'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнИ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнР'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмнД'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнВ'),
        WordForm(f'{pnsmi[:-2]}ыми', '.ПНСмнТ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнП'),
        WordForm(gnb1mn, '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ПНС2
def passive_present_participle_pns2(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn[:-2]}имый'
    word_forms = [
        WordForm(pnsmi, '.ПНСмИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСмР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСмД'),
        WordForm(pnsmi, '.ПНСмВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСмП'),
        WordForm(f'{pnsmi[:-2]}ая', '.ПНСжИ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжР'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжД'),
        WordForm(f'{pnsmi[:-2]}ую', '.ПНСжВ'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжТ1'),
        WordForm(f'{pnsmi[:-2]}ою', '.ПНСжТ2'),
        WordForm(f'{pnsmi[:-2]}ой', '.ПНСжП'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсИ'),
        WordForm(f'{pnsmi[:-2]}ого', '.ПНСсР'),
        WordForm(f'{pnsmi[:-2]}ому', '.ПНСсД'),
        WordForm(f'{pnsmi[:-2]}ое', '.ПНСсВ'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСсТ'),
        WordForm(f'{pnsmi[:-2]}ом', '.ПНСсП'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнИ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнР'),
        WordForm(f'{pnsmi[:-2]}ым', '.ПНСмнД'),
        WordForm(f'{pnsmi[:-2]}ые', '.ПНСмнВ'),
        WordForm(f'{pnsmi[:-2]}ыми', '.ПНСмнТ'),
        WordForm(f'{pnsmi[:-2]}ых', '.ПНСмнП'),
        WordForm(gnb1mn, '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms
