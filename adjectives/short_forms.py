"""Прилагательные краткая форма"""

from word_form import WordForm


def get_short_forms(src_dict) -> list:
    short_tmpl = {
        'К1': get_short_k1,
        'К1*': get_short_k1_prim,
        'К1#*': get_short_k1_sharp_prim,
        'К1-м': get_short_k1_m,
        'К1е': get_short_k1e,
        'К1#е': get_short_k1_sharp_e,
        'К1о': get_short_k1o,
        'К1#и': get_short_k1_sharp_i,
        'К2': get_short_k2,
        'К2-м': get_short_k2_m,
        'К2е': get_short_k2e,
        'К2#е': get_short_k2_sharp_e,
        'К2о': get_short_k2o,
        'К3': get_short_k3,
        'К4': get_short_k4,
        'К5': get_short_k5,
        'К5е': get_short_k5e,
        'К5#е': get_short_k5_sharp_e,
        'К5мн': get_short_k5mn,
        'К6': get_short_k6,
        'К7': get_short_k7,
        'К8': get_short_k8,
        'К1+1е': get_short_k1_1e,
        'К6+1е': get_short_k6_and_1e,
        'К1&1#о': get_short_k1_1_sharp_o,
        'К6&8': get_short_k6_8,
    }
    return short_tmpl[src_dict['Inf_1']](src_dict)


# К1
def get_short_k1(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1*
def get_short_k1_prim(src_dict) -> list:
    pkm = src_dict['name']
    word_forms = [
        WordForm(pkm, '.ПКм'),
        WordForm(f'{pkm}а', '.ПКж'),
        WordForm(f'{pkm}о', '.ПКс'),
        WordForm(f'{pkm}ы', '.ПКмн'),
    ]
    return word_forms


# К1#*
def get_short_k1_sharp_prim(src_dict) -> list:
    pkm = src_dict['name']
    word_forms = [
        WordForm(pkm, '.ПКм'),
        WordForm(f'{pkm[:-2]}{pkm[-1]}а', '.ПКж'),
        WordForm(f'{pkm[:-2]}{pkm[-1]}о', '.ПКс'),
        WordForm(f'{pkm[:-2]}{pkm[-1]}ы', '.ПКмн'),
    ]
    return word_forms


# К1-м
def get_short_k1_m(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1е
def get_short_k1e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1#е
def get_short_k1_sharp_e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1о
def get_short_k1o(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}о{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1#и
def get_short_k1_sharp_i(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}и{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К2
def get_short_k2(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К2-м
def get_short_k2_m(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К2е
def get_short_k2e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К2#е
def get_short_k2_sharp_e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К2о
def get_short_k2o(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}о{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К3
def get_short_k3(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К4
def get_short_k4(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К5
def get_short_k5(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}ь', '.ПКм'),
        WordForm(f'{pmi[:-2]}я', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К5е
def get_short_k5e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}я', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К5#е
def get_short_k5_sharp_e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-4]}е{pmi[-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}я', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К5мн
def get_short_k5mn(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К6
def get_short_k6(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К7
def get_short_k7(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}я', '.ПКж'),
        WordForm(f'{pmi[:-2]}е', '.ПКс'),
        WordForm(f'{pmi[:-2]}и', '.ПКмн'),
    ]
    return word_forms


# К8
def get_short_k8(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}', '.ПКм'),
        WordForm(f'{pmi[:-3]}а', '.ПКж'),
        WordForm(f'{pmi[:-3]}о', '.ПКс'),
        WordForm(f'{pmi[:-3]}ы', '.ПКмн'),
    ]
    return word_forms


# К1+1е
def get_short_k1_1e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-2]}', '.ПКм1'),
        WordForm(f'{pmi[:-3]}е{pmi[-3]}', '.ПКм2'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К6+1е
def get_short_k6_and_1e(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}', '.ПКм1'),
        WordForm(f'{pmi[:-3]}е{pmi[-3]}', '.ПКм2'),
        WordForm(f'{pmi[:-2]}а', '.ПКж'),
        WordForm(f'{pmi[:-2]}о', '.ПКс'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн'),
    ]
    return word_forms


# К1&1#о
def get_short_k1_1_sharp_o(src_dict) -> list:
    pmi = src_dict['name']
    pkm1 = f'{pmi[:-2]}'
    pkm2 = f'{pmi[:-4]}о{pmi[-3]}'
    word_forms = [
        WordForm(pkm1, '.ПКм1'),
        WordForm(pkm2, '.ПКм2'),
        WordForm(f'{pkm1}а', '.ПКж1'),
        WordForm(f'{pkm2}а', '.ПКж2'),
        WordForm(f'{pkm1}о', '.ПКс1'),
        WordForm(f'{pkm2}о', '.ПКс2'),
        WordForm(f'{pkm1}ы', '.ПКмн1'),
        WordForm(f'{pkm2}ы', '.ПКмн2'),
    ]
    return word_forms


# К6&8
def get_short_k6_8(src_dict) -> list:
    pmi = src_dict['name']
    word_forms = [
        WordForm(f'{pmi[:-3]}', '.ПКм'),
        WordForm(f'{pmi[:-2]}а', '.ПКж1'),
        WordForm(f'{pmi[:-3]}а', '.ПКж2'),
        WordForm(f'{pmi[:-2]}о', '.ПКс1'),
        WordForm(f'{pmi[:-3]}о', '.ПКс2'),
        WordForm(f'{pmi[:-2]}ы', '.ПКмн1'),
        WordForm(f'{pmi[:-3]}ы', '.ПКмн2'),
    ]
    return word_forms
