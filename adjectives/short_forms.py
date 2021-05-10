"""Прилагательные краткая форма"""

from word_form import WordForm


def get_short_forms(src_dict) -> list:
    short_tmpl = {
        'К1': get_short_k1,
        'К1#е': get_short_k1_sharp_e,
        'К1е': get_short_k1e,
        'К2#е': get_short_k2_sharp_e,
        'К2о': get_short_k2o,
        'К4': get_short_k4,
        'К5мн': get_short_k5mn,
        'К6': get_short_k6,
        'К6+1е': get_short_k6_and_1e,
    }
    return short_tmpl[src_dict['Inf_1']](src_dict)


# К1
def get_short_k1(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1#е
def get_short_k1_sharp_e(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-4]}е{name[-3:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1е
def get_short_k1e(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-3]}е{name[-3:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К2#е
def get_short_k2_sharp_e(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-4]}е{name[-3:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К2о
def get_short_k2o(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-3]}о{name[-3:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К4
def get_short_k4(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}е', '.ПКс'),
        WordForm(f'{name[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К5мн
def get_short_k5mn(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К6
def get_short_k6(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-3]}', '.ПКм'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К6+1е
def get_short_k6_and_1e(src_dict) -> list:
    name = src_dict['name']
    word_forms = [
        WordForm(f'{name[:-3]}', '.ПКм1'),
        WordForm(f'{name[:-3]}е{name[-3]}', '.ПКм2'),
        WordForm(f'{name[:-2]}а', '.ПКж'),
        WordForm(f'{name[:-2]}о', '.ПКс'),
        WordForm(f'{name[:-2]}ы', '.ПКмн'),
    ]
    return word_forms
