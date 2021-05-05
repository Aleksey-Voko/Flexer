"""Причастие настоящего времени действительное"""

from verbs.present_future import get_present_future_forms
from word_form import WordForm


def get_present_participle_is_valid(src_dict) -> list:
    present_participle_tmpl = {
        'ПНД1': present_participle_is_valid_pnd1,
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
