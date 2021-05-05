"""Причастие прошедшего времени действительное"""

from verbs.past_tense import get_past_tense_forms
from word_form import WordForm


def get_past_participle_is_valid(src_dict) -> list:
    past_participle_tmpl = {
        'ППД1в': past_participle_is_valid_ppd1v,
        'ППД2в': past_participle_is_valid_ppd2v,
        'ППД2в&5': past_participle_is_valid_ppd2v_and_5,
        'ППД5': past_participle_is_valid_ppd5,
    }
    return past_participle_tmpl[src_dict['Inf_9']](src_dict)


# ППД1в
def past_participle_is_valid_ppd1v(src_dict) -> list:
    name = src_dict['name']
    gpm = list(filter(
        lambda x: x.idf == '.ГПм',
        get_past_tense_forms(src_dict)
    ))[0].name
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{gpm[:-1]}вший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{gpm[:-3]}вшийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms


# ППД2в
def past_participle_is_valid_ppd2v(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{name[:-2]}вший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{name[:-4]}вшийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms


# ППД2в&5
def past_participle_is_valid_ppd2v_and_5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdm1i = f'{name[:-2]}вший'
        ppdm2i = f'{name[:-4]}ший'
        word_forms = [
            WordForm(ppdm1i, '.ППД1мИ'),
            WordForm(f'{ppdm1i[:-2]}его', '.ППД1мР'),
            WordForm(f'{ppdm1i[:-2]}ему', '.ППД1мД'),
            WordForm(ppdm1i, '.ППД1мВ'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1мТ'),
            WordForm(f'{ppdm1i[:-2]}ем', '.ППД1мП'),
            WordForm(f'{ppdm1i[:-2]}ая', '.ППД1жИ'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жР'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жД'),
            WordForm(f'{ppdm1i[:-2]}ую', '.ППД1жВ'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жТ1'),
            WordForm(f'{ppdm1i[:-2]}ею', '.ППД1жТ2'),
            WordForm(f'{ppdm1i[:-2]}ей', '.ППД1жП'),
            WordForm(f'{ppdm1i[:-2]}ее', '.ППД1сИ'),
            WordForm(f'{ppdm1i[:-2]}его', '.ППД1сР'),
            WordForm(f'{ppdm1i[:-2]}ему', '.ППД1сД'),
            WordForm(f'{ppdm1i[:-2]}ее', '.ППД1сВ'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1сТ'),
            WordForm(f'{ppdm1i[:-2]}ем', '.ППД1сП'),
            WordForm(f'{ppdm1i[:-2]}ие', '.ППД1мнИ'),
            WordForm(f'{ppdm1i[:-2]}их', '.ППД1мнР'),
            WordForm(f'{ppdm1i[:-2]}им', '.ППД1мнД'),
            WordForm(f'{ppdm1i[:-2]}ие', '.ППД1мнВ'),
            WordForm(f'{ppdm1i[:-2]}ими', '.ППД1мнТ'),
            WordForm(f'{ppdm1i[:-2]}их', '.ППД1мнП'),
            WordForm(ppdm2i, '.ППД2мИ'),
            WordForm(f'{ppdm2i[:-2]}его', '.ППД2мР'),
            WordForm(f'{ppdm2i[:-2]}ему', '.ППД2мД'),
            WordForm(ppdm2i, '.ППД2мВ'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2мТ'),
            WordForm(f'{ppdm2i[:-2]}ем', '.ППД2мП'),
            WordForm(f'{ppdm2i[:-2]}ая', '.ППД2жИ'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жР'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жД'),
            WordForm(f'{ppdm2i[:-2]}ую', '.ППД2жВ'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жТ1'),
            WordForm(f'{ppdm2i[:-2]}ею', '.ППД2жТ2'),
            WordForm(f'{ppdm2i[:-2]}ей', '.ППД2жП'),
            WordForm(f'{ppdm2i[:-2]}ее', '.ППД2сИ'),
            WordForm(f'{ppdm2i[:-2]}его', '.ППД2сР'),
            WordForm(f'{ppdm2i[:-2]}ему', '.ППД2сД'),
            WordForm(f'{ppdm2i[:-2]}ее', '.ППД2сВ'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2сТ'),
            WordForm(f'{ppdm2i[:-2]}ем', '.ППД2сП'),
            WordForm(f'{ppdm2i[:-2]}ие', '.ППД2мнИ'),
            WordForm(f'{ppdm2i[:-2]}их', '.ППД2мнР'),
            WordForm(f'{ppdm2i[:-2]}им', '.ППД2мнД'),
            WordForm(f'{ppdm2i[:-2]}ие', '.ППД2мнВ'),
            WordForm(f'{ppdm2i[:-2]}ими', '.ППД2мнТ'),
            WordForm(f'{ppdm2i[:-2]}их', '.ППД2мнП'),
        ]
    else:
        ppdm1i = f'{name[:-4]}вшийся'
        ppdm2i = f'{name[:-6]}шийся'
        word_forms = [
            WordForm(ppdm1i, '.ППД1мИ'),
            WordForm(f'{ppdm1i[:-4]}егося', '.ППД1мР'),
            WordForm(f'{ppdm1i[:-4]}емуся', '.ППД1мД'),
            WordForm(ppdm1i, '.ППД1мВ'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1мТ'),
            WordForm(f'{ppdm1i[:-4]}емся', '.ППД1мП'),
            WordForm(f'{ppdm1i[:-4]}аяся', '.ППД1жИ'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жР'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жД'),
            WordForm(f'{ppdm1i[:-4]}уюся', '.ППД1жВ'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жТ1'),
            WordForm(f'{ppdm1i[:-4]}еюся', '.ППД1жТ2'),
            WordForm(f'{ppdm1i[:-4]}ейся', '.ППД1жП'),
            WordForm(f'{ppdm1i[:-4]}ееся', '.ППД1сИ'),
            WordForm(f'{ppdm1i[:-4]}егося', '.ППД1сР'),
            WordForm(f'{ppdm1i[:-4]}емуся', '.ППД1сД'),
            WordForm(f'{ppdm1i[:-4]}ееся', '.ППД1сВ'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1сТ'),
            WordForm(f'{ppdm1i[:-4]}емся', '.ППД1сП'),
            WordForm(f'{ppdm1i[:-4]}иеся', '.ППД1мнИ'),
            WordForm(f'{ppdm1i[:-4]}ихся', '.ППД1мнР'),
            WordForm(f'{ppdm1i[:-4]}имся', '.ППД1мнД'),
            WordForm(f'{ppdm1i[:-4]}иеся', '.ППД1мнВ'),
            WordForm(f'{ppdm1i[:-4]}имися', '.ППД1мнТ'),
            WordForm(f'{ppdm1i[:-4]}ихся', '.ППД1мнП'),
            WordForm(ppdm2i, '.ППД2мИ'),
            WordForm(f'{ppdm2i[:-4]}егося', '.ППД2мР'),
            WordForm(f'{ppdm2i[:-4]}емуся', '.ППД2мД'),
            WordForm(ppdm2i, '.ППД2мВ'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2мТ'),
            WordForm(f'{ppdm2i[:-4]}емся', '.ППД2мП'),
            WordForm(f'{ppdm2i[:-4]}аяся', '.ППД2жИ'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жР'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жД'),
            WordForm(f'{ppdm2i[:-4]}уюся', '.ППД2жВ'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жТ1'),
            WordForm(f'{ppdm2i[:-4]}еюся', '.ППД2жТ2'),
            WordForm(f'{ppdm2i[:-4]}ейся', '.ППД2жП'),
            WordForm(f'{ppdm2i[:-4]}ееся', '.ППД2сИ'),
            WordForm(f'{ppdm2i[:-4]}егося', '.ППД2сР'),
            WordForm(f'{ppdm2i[:-4]}емуся', '.ППД2сД'),
            WordForm(f'{ppdm2i[:-4]}ееся', '.ППД2сВ'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2сТ'),
            WordForm(f'{ppdm2i[:-4]}емся', '.ППД2сП'),
            WordForm(f'{ppdm2i[:-4]}иеся', '.ППД2мнИ'),
            WordForm(f'{ppdm2i[:-4]}ихся', '.ППД2мнР'),
            WordForm(f'{ppdm2i[:-4]}имся', '.ППД2мнД'),
            WordForm(f'{ppdm2i[:-4]}иеся', '.ППД2мнВ'),
            WordForm(f'{ppdm2i[:-4]}имися', '.ППД2мнТ'),
            WordForm(f'{ppdm2i[:-4]}ихся', '.ППД2мнП'),
        ]
    return word_forms


# ППД5
def past_participle_is_valid_ppd5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        ppdmi = f'{name[:-4]}ший'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДмР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДмП'),
            WordForm(f'{ppdmi[:-2]}ая', '.ППДжИ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжР'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжД'),
            WordForm(f'{ppdmi[:-2]}ую', '.ППДжВ'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-2]}ею', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-2]}ей', '.ППДжП'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсИ'),
            WordForm(f'{ppdmi[:-2]}его', '.ППДсР'),
            WordForm(f'{ppdmi[:-2]}ему', '.ППДсД'),
            WordForm(f'{ppdmi[:-2]}ее', '.ППДсВ'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДсТ'),
            WordForm(f'{ppdmi[:-2]}ем', '.ППДсП'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнР'),
            WordForm(f'{ppdmi[:-2]}им', '.ППДмнД'),
            WordForm(f'{ppdmi[:-2]}ие', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-2]}ими', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-2]}их', '.ППДмнП'),
        ]
    else:
        ppdmi = f'{name[:-6]}шийся'
        word_forms = [
            WordForm(ppdmi, '.ППДмИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДмР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДмД'),
            WordForm(ppdmi, '.ППДмВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДмП'),
            WordForm(f'{ppdmi[:-4]}аяся', '.ППДжИ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжР'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжД'),
            WordForm(f'{ppdmi[:-4]}уюся', '.ППДжВ'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжТ1'),
            WordForm(f'{ppdmi[:-4]}еюся', '.ППДжТ2'),
            WordForm(f'{ppdmi[:-4]}ейся', '.ППДжП'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсИ'),
            WordForm(f'{ppdmi[:-4]}егося', '.ППДсР'),
            WordForm(f'{ppdmi[:-4]}емуся', '.ППДсД'),
            WordForm(f'{ppdmi[:-4]}ееся', '.ППДсВ'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДсТ'),
            WordForm(f'{ppdmi[:-4]}емся', '.ППДсП'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнИ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнР'),
            WordForm(f'{ppdmi[:-4]}имся', '.ППДмнД'),
            WordForm(f'{ppdmi[:-4]}иеся', '.ППДмнВ'),
            WordForm(f'{ppdmi[:-4]}имися', '.ППДмнТ'),
            WordForm(f'{ppdmi[:-4]}ихся', '.ППДмнП'),
        ]
    return word_forms
