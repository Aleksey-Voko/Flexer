"""Причастие настоящего времени действительное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_present_participle_is_valid(src_dict) -> list:
    present_participle_tmpl = {
        'ПНД1': present_participle_is_valid_pnd1,
        'ПНД1*': present_participle_is_valid_pnd1_dash,
        'ПНД2': present_participle_is_valid_pnd2,
        'ПНД1|1': present_participle_is_valid_pnd1_1,
    }
    return present_participle_tmpl[src_dict['Inf_7']](src_dict)


# ПНД1
def present_participle_is_valid_pnd1(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        pndmi = f'{gnb3mn[:-1]}щий'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДмР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДмП'),
            WordForm(f'{pndmi[:-2]}ая', '.ПНДжИ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжР'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжД'),
            WordForm(f'{pndmi[:-2]}ую', '.ПНДжВ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-2]}ею', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжП'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДсР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДсД'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДсТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДсП'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнР'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмнД'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-2]}ими', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнП'),
        ]
    else:
        pndmi = f'{gnb3mn[:-3]}щийся'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДмР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДмП'),
            WordForm(f'{pndmi[:-4]}аяся', '.ПНДжИ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжР'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжД'),
            WordForm(f'{pndmi[:-4]}уюся', '.ПНДжВ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-4]}еюся', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжП'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДсР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДсД'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДсТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДсП'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнР'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмнД'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-4]}имися', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнП'),
        ]
    return word_forms


# ПНД1*
def present_participle_is_valid_pnd1_dash(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        pndmi = f'{gnb3mn1[:-1]}щий'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДмР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДмП'),
            WordForm(f'{pndmi[:-2]}ая', '.ПНДжИ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжР'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжД'),
            WordForm(f'{pndmi[:-2]}ую', '.ПНДжВ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-2]}ею', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжП'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДсР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДсД'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДсТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДсП'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнР'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмнД'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-2]}ими', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнП'),
        ]
    else:
        pndmi = f'{gnb3mn1[:-3]}щийся'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДмР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДмП'),
            WordForm(f'{pndmi[:-4]}аяся', '.ПНДжИ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжР'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжД'),
            WordForm(f'{pndmi[:-4]}уюся', '.ПНДжВ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-4]}еюся', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжП'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДсР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДсД'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДсТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДсП'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнР'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмнД'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-4]}имися', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнП'),
        ]
    return word_forms


# ПНД2
def present_participle_is_valid_pnd2(src_dict) -> list:
    name = src_dict['name']
    gnb3mn = list(filter(
        lambda x: x.idf == '.ГНБ3мн',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        pndmi = f'{gnb3mn[:-1]}щий'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДмР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДмП'),
            WordForm(f'{pndmi[:-2]}ая', '.ПНДжИ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжР'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжД'),
            WordForm(f'{pndmi[:-2]}ую', '.ПНДжВ'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-2]}ею', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-2]}ей', '.ПНДжП'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсИ'),
            WordForm(f'{pndmi[:-2]}его', '.ПНДсР'),
            WordForm(f'{pndmi[:-2]}ему', '.ПНДсД'),
            WordForm(f'{pndmi[:-2]}ее', '.ПНДсВ'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДсТ'),
            WordForm(f'{pndmi[:-2]}ем', '.ПНДсП'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнР'),
            WordForm(f'{pndmi[:-2]}им', '.ПНДмнД'),
            WordForm(f'{pndmi[:-2]}ие', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-2]}ими', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-2]}их', '.ПНДмнП'),
            WordForm(f'{pndmi[:-2]}', '.ПНДКм'),
            WordForm(f'{pndmi[:-2]}а', '.ПНДКж'),
            WordForm(f'{pndmi[:-2]}е', '.ПНДКс'),
            WordForm(f'{pndmi[:-2]}и', '.ПНДКмн'),
        ]
    else:
        pndmi = f'{gnb3mn[:-3]}щийся'
        word_forms = [
            WordForm(pndmi, '.ПНДмИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДмР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДмД'),
            WordForm(pndmi, '.ПНДмВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДмП'),
            WordForm(f'{pndmi[:-4]}аяся', '.ПНДжИ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжР'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжД'),
            WordForm(f'{pndmi[:-4]}уюся', '.ПНДжВ'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжТ1'),
            WordForm(f'{pndmi[:-4]}еюся', '.ПНДжТ2'),
            WordForm(f'{pndmi[:-4]}ейся', '.ПНДжП'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсИ'),
            WordForm(f'{pndmi[:-4]}егося', '.ПНДсР'),
            WordForm(f'{pndmi[:-4]}емуся', '.ПНДсД'),
            WordForm(f'{pndmi[:-4]}ееся', '.ПНДсВ'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДсТ'),
            WordForm(f'{pndmi[:-4]}емся', '.ПНДсП'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнИ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнР'),
            WordForm(f'{pndmi[:-4]}имся', '.ПНДмнД'),
            WordForm(f'{pndmi[:-4]}иеся', '.ПНДмнВ'),
            WordForm(f'{pndmi[:-4]}имися', '.ПНДмнТ'),
            WordForm(f'{pndmi[:-4]}ихся', '.ПНДмнП'),
            WordForm(f'{pndmi[:-4]}', '.ПНДКм'),
            WordForm(f'{pndmi[:-4]}а', '.ПНДКж'),
            WordForm(f'{pndmi[:-4]}е', '.ПНДКс'),
            WordForm(f'{pndmi[:-4]}и', '.ПНДКмн'),
        ]
    return word_forms


# ПНД1|1
def present_participle_is_valid_pnd1_1(src_dict) -> list:
    name = src_dict['name']
    gnb3mn1 = list(filter(
        lambda x: x.idf == '.ГНБ3мн1',
        get_present_future_forms(src_dict)
    ))[0].name
    gnb3mn2 = list(filter(
        lambda x: x.idf == '.ГНБ3мн2',
        get_present_future_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        pnd1mi = f'{gnb3mn1[:-1]}щий'
        pnd2mi = f'{gnb3mn2[:-1]}щий'
        word_forms = [
            WordForm(pnd1mi, '.ПНД1мИ'),
            WordForm(f'{pnd1mi[:-2]}его', '.ПНД1мР'),
            WordForm(f'{pnd1mi[:-2]}ему', '.ПНД1мД'),
            WordForm(pnd1mi, '.ПНД1мВ'),
            WordForm(f'{pnd1mi[:-2]}им', '.ПНД1мТ'),
            WordForm(f'{pnd1mi[:-2]}ем', '.ПНД1мП'),
            WordForm(f'{pnd1mi[:-2]}ая', '.ПНД1жИ'),
            WordForm(f'{pnd1mi[:-2]}ей', '.ПНД1жР'),
            WordForm(f'{pnd1mi[:-2]}ей', '.ПНД1жД'),
            WordForm(f'{pnd1mi[:-2]}ую', '.ПНД1жВ'),
            WordForm(f'{pnd1mi[:-2]}ей', '.ПНД1жТ1'),
            WordForm(f'{pnd1mi[:-2]}ею', '.ПНД1жТ2'),
            WordForm(f'{pnd1mi[:-2]}ей', '.ПНД1жП'),
            WordForm(f'{pnd1mi[:-2]}ее', '.ПНД1сИ'),
            WordForm(f'{pnd1mi[:-2]}его', '.ПНД1сР'),
            WordForm(f'{pnd1mi[:-2]}ему', '.ПНД1сД'),
            WordForm(f'{pnd1mi[:-2]}ее', '.ПНД1сВ'),
            WordForm(f'{pnd1mi[:-2]}им', '.ПНД1сТ'),
            WordForm(f'{pnd1mi[:-2]}ем', '.ПНД1сП'),
            WordForm(f'{pnd1mi[:-2]}ие', '.ПНД1мнИ'),
            WordForm(f'{pnd1mi[:-2]}их', '.ПНД1мнР'),
            WordForm(f'{pnd1mi[:-2]}им', '.ПНД1мнД'),
            WordForm(f'{pnd1mi[:-2]}ие', '.ПНД1мнВ'),
            WordForm(f'{pnd1mi[:-2]}ими', '.ПНД1мнТ'),
            WordForm(f'{pnd1mi[:-2]}их', '.ПНД1мнП'),

            WordForm(pnd2mi, '.ПНД2мИ'),
            WordForm(f'{pnd2mi[:-2]}его', '.ПНД2мР'),
            WordForm(f'{pnd2mi[:-2]}ему', '.ПНД2мД'),
            WordForm(pnd2mi, '.ПНД2мВ'),
            WordForm(f'{pnd2mi[:-2]}им', '.ПНД2мТ'),
            WordForm(f'{pnd2mi[:-2]}ем', '.ПНД2мП'),
            WordForm(f'{pnd2mi[:-2]}ая', '.ПНД2жИ'),
            WordForm(f'{pnd2mi[:-2]}ей', '.ПНД2жР'),
            WordForm(f'{pnd2mi[:-2]}ей', '.ПНД2жД'),
            WordForm(f'{pnd2mi[:-2]}ую', '.ПНД2жВ'),
            WordForm(f'{pnd2mi[:-2]}ей', '.ПНД2жТ1'),
            WordForm(f'{pnd2mi[:-2]}ею', '.ПНД2жТ2'),
            WordForm(f'{pnd2mi[:-2]}ей', '.ПНД2жП'),
            WordForm(f'{pnd2mi[:-2]}ее', '.ПНД2сИ'),
            WordForm(f'{pnd2mi[:-2]}его', '.ПНД2сР'),
            WordForm(f'{pnd2mi[:-2]}ему', '.ПНД2сД'),
            WordForm(f'{pnd2mi[:-2]}ее', '.ПНД2сВ'),
            WordForm(f'{pnd2mi[:-2]}им', '.ПНД2сТ'),
            WordForm(f'{pnd2mi[:-2]}ем', '.ПНД2сП'),
            WordForm(f'{pnd2mi[:-2]}ие', '.ПНД2мнИ'),
            WordForm(f'{pnd2mi[:-2]}их', '.ПНД2мнР'),
            WordForm(f'{pnd2mi[:-2]}им', '.ПНД2мнД'),
            WordForm(f'{pnd2mi[:-2]}ие', '.ПНД2мнВ'),
            WordForm(f'{pnd2mi[:-2]}ими', '.ПНД2мнТ'),
            WordForm(f'{pnd2mi[:-2]}их', '.ПНД2мнП'),
        ]
    else:
        pnd1mi = f'{gnb3mn1[:-3]}щийся'
        pnd2mi = f'{gnb3mn2[:-3]}щийся'
        word_forms = [
            WordForm(pnd1mi, '.ПНД1мИ'),
            WordForm(f'{pnd1mi[:-4]}егося', '.ПНД1мР'),
            WordForm(f'{pnd1mi[:-4]}емуся', '.ПНД1мД'),
            WordForm(pnd1mi, '.ПНД1мВ'),
            WordForm(f'{pnd1mi[:-4]}имся', '.ПНД1мТ'),
            WordForm(f'{pnd1mi[:-4]}емся', '.ПНД1мП'),
            WordForm(f'{pnd1mi[:-4]}аяся', '.ПНД1жИ'),
            WordForm(f'{pnd1mi[:-4]}ейся', '.ПНД1жР'),
            WordForm(f'{pnd1mi[:-4]}ейся', '.ПНД1жД'),
            WordForm(f'{pnd1mi[:-4]}уюся', '.ПНД1жВ'),
            WordForm(f'{pnd1mi[:-4]}ейся', '.ПНД1жТ1'),
            WordForm(f'{pnd1mi[:-4]}еюся', '.ПНД1жТ2'),
            WordForm(f'{pnd1mi[:-4]}ейся', '.ПНД1жП'),
            WordForm(f'{pnd1mi[:-4]}ееся', '.ПНД1сИ'),
            WordForm(f'{pnd1mi[:-4]}егося', '.ПНД1сР'),
            WordForm(f'{pnd1mi[:-4]}емуся', '.ПНД1сД'),
            WordForm(f'{pnd1mi[:-4]}ееся', '.ПНД1сВ'),
            WordForm(f'{pnd1mi[:-4]}имся', '.ПНД1сТ'),
            WordForm(f'{pnd1mi[:-4]}емся', '.ПНД1сП'),
            WordForm(f'{pnd1mi[:-4]}иеся', '.ПНД1мнИ'),
            WordForm(f'{pnd1mi[:-4]}ихся', '.ПНД1мнР'),
            WordForm(f'{pnd1mi[:-4]}имся', '.ПНД1мнД'),
            WordForm(f'{pnd1mi[:-4]}иеся', '.ПНД1мнВ'),
            WordForm(f'{pnd1mi[:-4]}имися', '.ПНД1мнТ'),
            WordForm(f'{pnd1mi[:-4]}ихся', '.ПНД1мнП'),

            WordForm(pnd2mi, '.ПНД2мИ'),
            WordForm(f'{pnd2mi[:-4]}егося', '.ПНД2мР'),
            WordForm(f'{pnd2mi[:-4]}емуся', '.ПНД2мД'),
            WordForm(pnd2mi, '.ПНД2мВ'),
            WordForm(f'{pnd2mi[:-4]}имся', '.ПНД2мТ'),
            WordForm(f'{pnd2mi[:-4]}емся', '.ПНД2мП'),
            WordForm(f'{pnd2mi[:-4]}аяся', '.ПНД2жИ'),
            WordForm(f'{pnd2mi[:-4]}ейся', '.ПНД2жР'),
            WordForm(f'{pnd2mi[:-4]}ейся', '.ПНД2жД'),
            WordForm(f'{pnd2mi[:-4]}уюся', '.ПНД2жВ'),
            WordForm(f'{pnd2mi[:-4]}ейся', '.ПНД2жТ1'),
            WordForm(f'{pnd2mi[:-4]}еюся', '.ПНД2жТ2'),
            WordForm(f'{pnd2mi[:-4]}ейся', '.ПНД2жП'),
            WordForm(f'{pnd2mi[:-4]}ееся', '.ПНД2сИ'),
            WordForm(f'{pnd2mi[:-4]}егося', '.ПНД2сР'),
            WordForm(f'{pnd2mi[:-4]}емуся', '.ПНД2сД'),
            WordForm(f'{pnd2mi[:-4]}ееся', '.ПНД2сВ'),
            WordForm(f'{pnd2mi[:-4]}имся', '.ПНД2сТ'),
            WordForm(f'{pnd2mi[:-4]}емся', '.ПНД2сП'),
            WordForm(f'{pnd2mi[:-4]}иеся', '.ПНД2мнИ'),
            WordForm(f'{pnd2mi[:-4]}ихся', '.ПНД2мнР'),
            WordForm(f'{pnd2mi[:-4]}имся', '.ПНД2мнД'),
            WordForm(f'{pnd2mi[:-4]}иеся', '.ПНД2мнВ'),
            WordForm(f'{pnd2mi[:-4]}имися', '.ПНД2мнТ'),
            WordForm(f'{pnd2mi[:-4]}ихся', '.ПНД2мнП'),
        ]
    return word_forms
