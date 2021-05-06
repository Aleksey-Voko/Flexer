"""Причастие настоящего времени страдательное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_passive_present_participle(src_dict) -> list:
    passive_present_tmpl = {
        'ПНС1': passive_present_participle_pns1,
        'ПНС1*': passive_present_participle_pns1_prim,
        'ПНС1!': passive_present_participle_pns1_excl,
        'ПНС2': passive_present_participle_pns2,
        'ПНС2*': passive_present_participle_pns2_prim,
        'ПНС2!': passive_present_participle_pns2_excl,
        'ПНС3': passive_present_participle_pns3,
        'ПНС1|1': passive_present_participle_pns1_1,
        'ПНС1|2!': passive_present_participle_pns1_2_excl,
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


# ПНС1*
def passive_present_participle_pns1_prim(src_dict) -> list:
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn1[:-2]}емый'
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
        WordForm(gnb1mn1, '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ПНС1!
def passive_present_participle_pns1_excl(src_dict) -> list:
    name = src_dict['name']
    pnsmi = f'{name[:-2]}емый'
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
        WordForm(f'{pnsmi[:-2]}', '.ПНСКм'),
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


# ПНС2*
def passive_present_participle_pns2_prim(src_dict) -> list:
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb1mn = list(filter(
        lambda x: x.idf == '.ГНБ1мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn1[:-2]}имый'
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


# ПНС2!
def passive_present_participle_pns2_excl(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
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
        WordForm(f'{pnsmi[:-2]}', '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ПНС3
def passive_present_participle_pns3(src_dict) -> list:
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name

    pnsmi = f'{gnb3mn[:-2]}омый'
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
        WordForm(f'{pnsmi[:-2]}', '.ПНСКм'),
        WordForm(f'{pnsmi[:-2]}а', '.ПНСКж'),
        WordForm(f'{pnsmi[:-2]}о', '.ПНСКс'),
        WordForm(f'{pnsmi[:-2]}ы', '.ПНСКмн'),
    ]

    return word_forms


# ПНС1|1
def passive_present_participle_pns1_1(src_dict) -> list:
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name

    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name

    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name

    gnb1mn2 = list(filter(
        lambda x: x.idf == '.ГНБ1мн2',
        get_present_future_forms(src_dict)
    ))[0].name

    pns1mi = f'{gnb3mn1[:-2]}емый'
    pns2mi = f'{gnb3mn2[:-2]}емый'

    word_forms = [
        WordForm(pns1mi, '.ПНС1мИ'),
        WordForm(f'{pns1mi[:-2]}ого', '.ПНС1мР'),
        WordForm(f'{pns1mi[:-2]}ому', '.ПНС1мД'),
        WordForm(pns1mi, '.ПНС1мВ'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1мТ'),
        WordForm(f'{pns1mi[:-2]}ом', '.ПНС1мП'),
        WordForm(f'{pns1mi[:-2]}ая', '.ПНС1жИ'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жР'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жД'),
        WordForm(f'{pns1mi[:-2]}ую', '.ПНС1жВ'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жТ1'),
        WordForm(f'{pns1mi[:-2]}ою', '.ПНС1жТ2'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жП'),
        WordForm(f'{pns1mi[:-2]}ое', '.ПНС1сИ'),
        WordForm(f'{pns1mi[:-2]}ого', '.ПНС1сР'),
        WordForm(f'{pns1mi[:-2]}ому', '.ПНС1сД'),
        WordForm(f'{pns1mi[:-2]}ое', '.ПНС1сВ'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1сТ'),
        WordForm(f'{pns1mi[:-2]}ом', '.ПНС1сП'),
        WordForm(f'{pns1mi[:-2]}ые', '.ПНС1мнИ'),
        WordForm(f'{pns1mi[:-2]}ых', '.ПНС1мнР'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1мнД'),
        WordForm(f'{pns1mi[:-2]}ые', '.ПНС1мнВ'),
        WordForm(f'{pns1mi[:-2]}ыми', '.ПНС1мнТ'),
        WordForm(f'{pns1mi[:-2]}ых', '.ПНС1мнП'),
        WordForm(gnb1mn1, '.ПНСКм1'),
        WordForm(f'{pns1mi[:-2]}а', '.ПНСКж1'),
        WordForm(f'{pns1mi[:-2]}о', '.ПНСКс1'),
        WordForm(f'{pns1mi[:-2]}ы', '.ПНСКмн1'),

        WordForm(pns2mi, '.ПНС2мИ'),
        WordForm(f'{pns2mi[:-2]}ого', '.ПНС2мР'),
        WordForm(f'{pns2mi[:-2]}ому', '.ПНС2мД'),
        WordForm(pns2mi, '.ПНС2мВ'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2мТ'),
        WordForm(f'{pns2mi[:-2]}ом', '.ПНС2мП'),
        WordForm(f'{pns2mi[:-2]}ая', '.ПНС2жИ'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жР'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жД'),
        WordForm(f'{pns2mi[:-2]}ую', '.ПНС2жВ'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жТ1'),
        WordForm(f'{pns2mi[:-2]}ою', '.ПНС2жТ2'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жП'),
        WordForm(f'{pns2mi[:-2]}ое', '.ПНС2сИ'),
        WordForm(f'{pns2mi[:-2]}ого', '.ПНС2сР'),
        WordForm(f'{pns2mi[:-2]}ому', '.ПНС2сД'),
        WordForm(f'{pns2mi[:-2]}ое', '.ПНС2сВ'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2сТ'),
        WordForm(f'{pns2mi[:-2]}ом', '.ПНС2сП'),
        WordForm(f'{pns2mi[:-2]}ые', '.ПНС2мнИ'),
        WordForm(f'{pns2mi[:-2]}ых', '.ПНС2мнР'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2мнД'),
        WordForm(f'{pns2mi[:-2]}ые', '.ПНС2мнВ'),
        WordForm(f'{pns2mi[:-2]}ыми', '.ПНС2мнТ'),
        WordForm(f'{pns2mi[:-2]}ых', '.ПНС2мнП'),
        WordForm(gnb1mn2, '.ПНСКм2'),
        WordForm(f'{pns2mi[:-2]}а', '.ПНСКж2'),
        WordForm(f'{pns2mi[:-2]}о', '.ПНСКс2'),
        WordForm(f'{pns2mi[:-2]}ы', '.ПНСКмн2'),
    ]

    return word_forms


# ПНС1|2!
def passive_present_participle_pns1_2_excl(src_dict) -> list:
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name

    gnb1mn1 = list(filter(
        lambda x: x.idf == '.ГНБ1мн1',
        get_present_future_forms(src_dict)
    ))[0].name

    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name

    pns1mi = f'{gnb3mn1[:-2]}емый'
    pns2mi = f'{gnb3mn2[:-2]}имый'

    word_forms = [
        WordForm(pns1mi, '.ПНС1мИ'),
        WordForm(f'{pns1mi[:-2]}ого', '.ПНС1мР'),
        WordForm(f'{pns1mi[:-2]}ому', '.ПНС1мД'),
        WordForm(pns1mi, '.ПНС1мВ'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1мТ'),
        WordForm(f'{pns1mi[:-2]}ом', '.ПНС1мП'),
        WordForm(f'{pns1mi[:-2]}ая', '.ПНС1жИ'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жР'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жД'),
        WordForm(f'{pns1mi[:-2]}ую', '.ПНС1жВ'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жТ1'),
        WordForm(f'{pns1mi[:-2]}ою', '.ПНС1жТ2'),
        WordForm(f'{pns1mi[:-2]}ой', '.ПНС1жП'),
        WordForm(f'{pns1mi[:-2]}ое', '.ПНС1сИ'),
        WordForm(f'{pns1mi[:-2]}ого', '.ПНС1сР'),
        WordForm(f'{pns1mi[:-2]}ому', '.ПНС1сД'),
        WordForm(f'{pns1mi[:-2]}ое', '.ПНС1сВ'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1сТ'),
        WordForm(f'{pns1mi[:-2]}ом', '.ПНС1сП'),
        WordForm(f'{pns1mi[:-2]}ые', '.ПНС1мнИ'),
        WordForm(f'{pns1mi[:-2]}ых', '.ПНС1мнР'),
        WordForm(f'{pns1mi[:-2]}ым', '.ПНС1мнД'),
        WordForm(f'{pns1mi[:-2]}ые', '.ПНС1мнВ'),
        WordForm(f'{pns1mi[:-2]}ыми', '.ПНС1мнТ'),
        WordForm(f'{pns1mi[:-2]}ых', '.ПНС1мнП'),
        WordForm(gnb1mn1, '.ПНСКм1'),
        WordForm(f'{pns1mi[:-2]}а', '.ПНСКж1'),
        WordForm(f'{pns1mi[:-2]}о', '.ПНСКс1'),
        WordForm(f'{pns1mi[:-2]}ы', '.ПНСКмн1'),

        WordForm(pns2mi, '.ПНС2мИ'),
        WordForm(f'{pns2mi[:-2]}ого', '.ПНС2мР'),
        WordForm(f'{pns2mi[:-2]}ому', '.ПНС2мД'),
        WordForm(pns2mi, '.ПНС2мВ'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2мТ'),
        WordForm(f'{pns2mi[:-2]}ом', '.ПНС2мП'),
        WordForm(f'{pns2mi[:-2]}ая', '.ПНС2жИ'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жР'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жД'),
        WordForm(f'{pns2mi[:-2]}ую', '.ПНС2жВ'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жТ1'),
        WordForm(f'{pns2mi[:-2]}ою', '.ПНС2жТ2'),
        WordForm(f'{pns2mi[:-2]}ой', '.ПНС2жП'),
        WordForm(f'{pns2mi[:-2]}ое', '.ПНС2сИ'),
        WordForm(f'{pns2mi[:-2]}ого', '.ПНС2сР'),
        WordForm(f'{pns2mi[:-2]}ому', '.ПНС2сД'),
        WordForm(f'{pns2mi[:-2]}ое', '.ПНС2сВ'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2сТ'),
        WordForm(f'{pns2mi[:-2]}ом', '.ПНС2сП'),
        WordForm(f'{pns2mi[:-2]}ые', '.ПНС2мнИ'),
        WordForm(f'{pns2mi[:-2]}ых', '.ПНС2мнР'),
        WordForm(f'{pns2mi[:-2]}ым', '.ПНС2мнД'),
        WordForm(f'{pns2mi[:-2]}ые', '.ПНС2мнВ'),
        WordForm(f'{pns2mi[:-2]}ыми', '.ПНС2мнТ'),
        WordForm(f'{pns2mi[:-2]}ых', '.ПНС2мнП'),
        WordForm(f'{pns2mi[:-2]}', '.ПНСКм2'),
        WordForm(f'{pns2mi[:-2]}а', '.ПНСКж2'),
        WordForm(f'{pns2mi[:-2]}о', '.ПНСКс2'),
        WordForm(f'{pns2mi[:-2]}ы', '.ПНСКмн2'),
    ]

    return word_forms
