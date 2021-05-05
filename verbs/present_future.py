"""Глаголы настоящее/будущее время"""

from word_form import WordForm


def get_present_future_forms(src_dict) -> list:
    present_future_tmpl = {
        'НБI1': present_future_nbi1,
        'НБI2': present_future_nbi2,
        'НБI2в': present_future_nbi2v,
        'НБI2в-': present_future_nbi2v_dash,
        'НБI2г': present_future_nbi2g,
        'НБI2г*': present_future_nbi2g_prim,
        'НБI2д': present_future_nbi2d,
        'НБI2ж-': present_future_nbi2zh_dash,
        'НБI2к': present_future_nbi2k,
        'НБI2н': present_future_nbi2n,
        'НБI2н-': present_future_nbi2n_dash,
        'НБI3': present_future_nbi3,
        'НБI3-': present_future_nbi3_dash,
        'НБI4': present_future_nbi4,
        'НБI4-': present_future_nbi4_dash,
        'НБI4б': present_future_nbi4b,
        'НБI4г': present_future_nbi4g,
        'НБI4д': present_future_nbi4d,
        'НБI4д-': present_future_nbi4d_dash,
        'НБI4ж': present_future_nbi4zh,
        'НБI4и': present_future_nbi4i,
        'НБI4к': present_future_nbi4k,
        'НБI4м': present_future_nbi4m,
        'НБI4н': present_future_nbi4n,
        'НБI4т': present_future_nbi4t,
        'НБI4т-': present_future_nbi4t_dash,
        'НБI4у': present_future_nbi4u,
        'НБI4я': present_future_nbi4j,
        'НБI4г*': present_future_nbi4g_prim,
        'НБI4г**': present_future_nbi4g_2prim,
        'НБI4г***': present_future_nbi4g_3prim,
        'НБI4д*': present_future_nbi4d_prim,
        'НБI4м*': present_future_nbi4m_prim,
        'НБI4м**': present_future_nbi4m_2prim,
        'НБI4м***': present_future_nbi4m_3prim,
        'НБI4н*': present_future_nbi4n_prim,
        'НБI4н**': present_future_nbi4n_2prim,
        'НБI4н***': present_future_nbi4n_3prim,
        'НБI4н****': present_future_nbi4n_4prim,
        'НБI4н*****': present_future_nbi4n_5prim,
        'НБI5': present_future_nbi5,
        'НБI5е': present_future_nbi5e,
        'НБI5л': present_future_nbi5l,
        'НБI5л-': present_future_nbi5l_dash,
        'НБI5о': present_future_nbi5o,
        'НБI5у': present_future_nbi5u,
        'НБI5ь': present_future_nbi5y,
        'НБI5ь*': present_future_nbi5y_prim,
        'НБI5ь**': present_future_nbi5y_2prim,
        'НБI5ь***': present_future_nbi5y_3prim,
        'НБI5ь****': present_future_nbi5y_4prim,
        'НБI5ь*****': present_future_nbi5y_5prim,
        'НБI5ь******': present_future_nbi5y_6prim,
        'НБI5ь!': present_future_nbi5y_excl,
        'НБI5ь*!': present_future_nbi5y_prim_excl,
        'НБI5ь**!': present_future_nbi5y_2prim_excl,
        'НБI5ь***!': present_future_nbi5y_3prim_excl,
        'НБI6д': present_future_nbi6d,
        'НБI6е': present_future_nbi6e,
        'НБI6ж': present_future_nbi6g,
        'НБI6й': present_future_nbi6j,
        'НБI6м': present_future_nbi6m,
        'НБI6о': present_future_nbi6o,
        'НБI6т': present_future_nbi6t,
        'НБI6ч': present_future_nbi6ch,
        'НБI6ч-': present_future_nbi6ch_dash,
        'НБI6ш': present_future_nbi6sh,
        'НБI6щ': present_future_nbi6zsh,
        'НБI6ы': present_future_nbi6ji,
        'НБI6я': present_future_nbi6ja,
        'НБI6е*': present_future_nbi6e_prim,
        'НБI6е**': present_future_nbi6e_2prim,
        'НБI6е***': present_future_nbi6e_3prim,
        'НБI6е****': present_future_nbi6e_4prim,
        'НБI6е*****': present_future_nbi6e_5prim,
        'НБI6е**!': present_future_nbi6e_2prim_excl,
        'НБI6й*': present_future_nbi6j_prim,
        'НБI6о*': present_future_nbi6o_prim,
        'НБI6о**': present_future_nbi6o_2prim,
        'НБI6т*': present_future_nbi6t_prim,
        'НБI6т**': present_future_nbi6t_2prim,
        'НБI6т***!': present_future_nbi6t_3prim_excl,
        'НБI7': present_future_nbi7,
        'НБI7-': present_future_nbi7_dash,
        'НБI7е': present_future_nbi7e,
        'НБI7е*': present_future_nbi7e_prim,
        'НБI7е**!': present_future_nbi7e_2prim_excl,
        'НБI7е***!': present_future_nbi7e_3prim_excl,
        'НБI8щ': present_future_nbi8shch,
        'НБI8#': present_future_nbi8_sharp,
        'НБI8#*': present_future_nbi8_sharp_prim,
        'НБI8#**': present_future_nbi8_sharp_2prim,
        'НБI8#***': present_future_nbi8_sharp_3prim,
        'НБI8#****': present_future_nbi8_sharp_4prim,
        'НБI8#*!': present_future_nbi8_sharp_prim_excl,
        'НБI8#**!': present_future_nbi8_sharp_2prim_excl,
        'НБI8#***!': present_future_nbi8_sharp_3prim_excl,
        'НБI8#****!': present_future_nbi8_sharp_4prim_excl,
        'НБI9е': present_future_nbi9e,
        'НБI9у': present_future_nbi9u,
        'НБI9у-': present_future_nbi9u_dash,
        'НБI9ш': present_future_nbi9sh,
        'НБI9ю': present_future_nbi9yu,
        'НБII1': present_future_nbii1,
        'НБII1-': present_future_nbii1_dash,
        'НБII2': present_future_nbii2,
        'НБII2л': present_future_nbii2l,
        'НБII3ж': present_future_nbii3g,
        'НБII3ч': present_future_nbii3ch,
        'НБII3ш': present_future_nbii3sh,
        'НБII3щ': present_future_nbii3shch,
        'НБII3-': present_future_nbii3_dash,
        'НБII4о': present_future_nbii4o,
        'НБII4о*': present_future_nbii4o_prim,
        'НБII4о**': present_future_nbii4o_2prim,
        'НБII4о***': present_future_nbii4o_3prim,
        'НБII4о****': present_future_nbii4o_4prim,
        'НБII5щ': present_future_nbii5shch,
        'НБII6щ': present_future_nbii6shch,
        'НБII*д': present_future_nbii_prim_d,
        'НБI-II3': present_future_nbi_ii3,
        'НБI-II4ч': present_future_nbi_ii4ch,
        'НБI-II5г': present_future_nbi_ii5g,
        'НБI-II*д': present_future_nbi_ii_prim_d,

        'НБI3&6ч': present_future_nbi3_6ch,
        'НБI3&6ш': present_future_nbi3_6sh,
        'НБI5л&I-II1': present_future_nbi5l_and_i_ii1,
        'НБII2+3ж': present_future_nbii2_and_3g,
    }
    return present_future_tmpl[src_dict['Inf_3']](src_dict)


# НБI1
def present_future_nbi1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-1]}у', '.ГНБ1е'),
            WordForm(f'{name[:-1]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-1]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-1]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-1]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-1]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-3]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-3]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2
def present_future_nbi2(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}у', '.ГНБ1е'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2в
def present_future_nbi2v(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ву', '.ГНБ1е'),
            WordForm(f'{name[:-2]}вешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}вет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}вем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}вете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}вут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}вешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}вется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}вемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ветесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}вутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2в-
def present_future_nbi2v_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}вет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}вется', '.ГНБ3е'),
        ]
    return word_forms


# НБI2г
def present_future_nbi2g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}гу', '.ГНБ1е'),
            WordForm(f'{name[:-2]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2г*
def present_future_nbi2g_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}гну', '.ГНБ1е'),
            WordForm(f'{name[:-2]}гнешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}гнет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}гнем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}гнете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}гнут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2д
def present_future_nbi2d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ду', '.ГНБ1е'),
            WordForm(f'{name[:-2]}дешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}дет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}дем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}дете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}дусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}дешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}дется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}демся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}детесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2ж-
def present_future_nbi2zh_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}жет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}жется', '.ГНБ3е'),
        ]
    return word_forms


# НБI2к
def present_future_nbi2k(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ку', '.ГНБ1е'),
            WordForm(f'{name[:-2]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}чем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}чете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}кут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}кусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}чемся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}четесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}кутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2н
def present_future_nbi2n(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ну', '.ГНБ1е'),
            WordForm(f'{name[:-2]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}нет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}нется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI2н-
def present_future_nbi2n_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}нет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}нется', '.ГНБ3е'),
        ]
    return word_forms


# НБI3
def present_future_nbi3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI3-
def present_future_nbi3_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}ется', '.ГНБ3е'),
        ]
    return word_forms


# НБI4
def present_future_nbi4(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4-
def present_future_nbi4_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
        ]
    return word_forms


# НБI4б
def present_future_nbi4b(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}бу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}бешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}бет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}бем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}бете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}бут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}бусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}бешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}бется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}бемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}бетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}бутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4г
def present_future_nbi4g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}гу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4д
def present_future_nbi4d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ду', '.ГНБ1е'),
            WordForm(f'{name[:-3]}дешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}дет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}дем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}дете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}дусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}дешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}дется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}демся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}детесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4д-
def present_future_nbi4d_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}дет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}дется', '.ГНБ3е'),
        ]
    return word_forms


# НБI4ж
def present_future_nbi4zh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4и
def present_future_nbi4i(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}иму', '.ГНБ1е'),
            WordForm(f'{name[:-3]}имешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}имет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}имем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}имете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}имут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}имусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}имешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}имется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}иметесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}имутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4к
def present_future_nbi4k(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ку', '.ГНБ1е'),
            WordForm(f'{name[:-3]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}чем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}чете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}кут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}кусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}чемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}четесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}кутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4м
def present_future_nbi4m(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}му', '.ГНБ1е'),
            WordForm(f'{name[:-3]}мешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}мет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}мем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}мете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}мусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}мешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}мется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н
def present_future_nbi4n(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4т
def present_future_nbi4t(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ту', '.ГНБ1е'),
            WordForm(f'{name[:-3]}тешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}тет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}тем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}тете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}тут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}тусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}тешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}тется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}темся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}тетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}тутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4т-
def present_future_nbi4t_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}тет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}тется', '.ГНБ3е'),
        ]
    return word_forms


# НБI4у
def present_future_nbi4u(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}уду', '.ГНБ1е'),
            WordForm(f'{name[:-3]}удешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}удет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}удем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}удете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}удут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}удусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}удешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}удется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}удемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}удетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}удутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4я
def present_future_nbi4j(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ягу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}яжешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}яжет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}яжем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}яжете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ягут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ягусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}яжешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}яжется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}яжемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}яжетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ягутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4г*
def present_future_nbi4g_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-3]}гу', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-3]}жешь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-3]}жет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-3]}жем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-3]}жете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-3]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-5]}гусь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-5]}жешься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-5]}жется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-5]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-5]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-5]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4г**
def present_future_nbi4g_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-3]}гу', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-3]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-3]}жет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-3]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}жется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4г***
def present_future_nbi4g_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-3]}гу', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-3]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-3]}жет', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-3]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-5]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-5]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-5]}жется', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-5]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4д*
def present_future_nbi4d_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-3]}ду', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-3]}дешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-3]}дет', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-3]}дем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-3]}дете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-3]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-5]}дусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-5]}дешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-5]}дется', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-5]}демся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-5]}детесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-5]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4м*
def present_future_nbi4m_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-3]}му', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-3]}мешь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-3]}мет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-3]}мем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-3]}мете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-3]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-5]}мусь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-5]}мешься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-5]}мется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-5]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-5]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-5]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4м**
def present_future_nbi4m_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-3]}му', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-3]}мешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-3]}мет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-3]}мем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}мете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}мусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}мешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}мется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4м***
def present_future_nbi4m_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-3]}му', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-3]}мешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-3]}мет', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-3]}мем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}мете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-5]}мусь', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-5]}мешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-5]}мется', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-5]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н*
def present_future_nbi4n_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н**
def present_future_nbi4n_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н***
def present_future_nbi4n_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н****
def present_future_nbi4n_4prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4н*****
def present_future_nbi4n_5prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:5]}о{name[5:-3]}ну', '.ГНБ1е'),
            WordForm(f'{name[:5]}о{name[5:-3]}нешь', '.ГНБ2е'),
            WordForm(f'{name[:5]}о{name[5:-3]}нет', '.ГНБ3е'),
            WordForm(f'{name[:5]}о{name[5:-3]}нем', '.ГНБ1мн'),
            WordForm(f'{name[:5]}о{name[5:-3]}нете', '.ГНБ2мн'),
            WordForm(f'{name[:5]}о{name[5:-3]}нут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:5]}о{name[5:-5]}нусь', '.ГНБ1е'),
            WordForm(f'{name[:5]}о{name[5:-5]}нешься', '.ГНБ2е'),
            WordForm(f'{name[:5]}о{name[5:-5]}нется', '.ГНБ3е'),
            WordForm(f'{name[:5]}о{name[5:-5]}немся', '.ГНБ1мн'),
            WordForm(f'{name[:5]}о{name[5:-5]}нетесь', '.ГНБ2мн'),
            WordForm(f'{name[:5]}о{name[5:-5]}нутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5
def present_future_nbi5(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5е
def present_future_nbi5e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ею', '.ГНБ1е'),
            WordForm(f'{name[:-3]}еешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}еет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}еем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}еете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}еют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}еюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}еешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}еется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}еемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}еетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}еются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5л
def present_future_nbi5l(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}лешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}лет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}лем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}лете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}лют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}люсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}лешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}лется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}лемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}летесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}лются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5л-
def present_future_nbi5l_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}лется', '.ГНБ3е'),
        ]
    return word_forms


# НБI5о
def present_future_nbi5o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ою', '.ГНБ1е'),
            WordForm(f'{name[:-3]}оешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}оет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}оем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}оете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}оют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}оюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}оешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}оется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}оемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}оетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}оются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5у
def present_future_nbi5u(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ую', '.ГНБ1е'),
            WordForm(f'{name[:-3]}уешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ует', '.ГНБ3е'),
            WordForm(f'{name[:-3]}уем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}уете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}уют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}уюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}уешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}уется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}уемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}уетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}уются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь
def present_future_nbi5y(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь*
def present_future_nbi5y_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь**
def present_future_nbi5y_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь***
def present_future_nbi5y_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь****
def present_future_nbi5y_4prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь*****
def present_future_nbi5y_5prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:5]}о{name[5:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:5]}о{name[5:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:5]}о{name[5:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:5]}о{name[5:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:5]}о{name[5:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:5]}о{name[5:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:5]}о{name[5:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:5]}о{name[5:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:5]}о{name[5:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:5]}о{name[5:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:5]}о{name[5:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:5]}о{name[5:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь******
def present_future_nbi5y_6prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:7]}о{name[7:-3]}ью', '.ГНБ1е'),
            WordForm(f'{name[:7]}о{name[7:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'{name[:7]}о{name[7:-3]}ьет', '.ГНБ3е'),
            WordForm(f'{name[:7]}о{name[7:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'{name[:7]}о{name[7:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'{name[:7]}о{name[7:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:7]}о{name[7:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'{name[:7]}о{name[7:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'{name[:7]}о{name[7:-5]}ьется', '.ГНБ3е'),
            WordForm(f'{name[:7]}о{name[7:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'{name[:7]}о{name[7:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'{name[:7]}о{name[7:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь!
def present_future_nbi5y_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'обо{name[1:-3]}ью', '.ГНБ1е'),
            WordForm(f'обо{name[1:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'обо{name[1:-3]}ьет', '.ГНБ3е'),
            WordForm(f'обо{name[1:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'обо{name[1:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'обо{name[1:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'обо{name[1:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'обо{name[1:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'обо{name[1:-5]}ьется', '.ГНБ3е'),
            WordForm(f'обо{name[1:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'обо{name[1:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'обо{name[1:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь*!
def present_future_nbi5y_prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'обоб{name[2:-3]}ью', '.ГНБ1е'),
            WordForm(f'обоб{name[2:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'обоб{name[2:-3]}ьет', '.ГНБ3е'),
            WordForm(f'обоб{name[2:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'обоб{name[2:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'обоб{name[2:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'обоб{name[2:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'обоб{name[2:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'обоб{name[2:-5]}ьется', '.ГНБ3е'),
            WordForm(f'обоб{name[2:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'обоб{name[2:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'обоб{name[2:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь**!
def present_future_nbi5y_2prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'изо{name[2:-3]}ью', '.ГНБ1е'),
            WordForm(f'изо{name[2:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'изо{name[2:-3]}ьет', '.ГНБ3е'),
            WordForm(f'изо{name[2:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'изо{name[2:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'изо{name[2:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'изо{name[2:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'изо{name[2:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'изо{name[2:-5]}ьется', '.ГНБ3е'),
            WordForm(f'изо{name[2:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'изо{name[2:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'изо{name[2:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI5ь***!
def present_future_nbi5y_3prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'разо{name[3:-3]}ью', '.ГНБ1е'),
            WordForm(f'разо{name[3:-3]}ьешь', '.ГНБ2е'),
            WordForm(f'разо{name[3:-3]}ьет', '.ГНБ3е'),
            WordForm(f'разо{name[3:-3]}ьем', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-3]}ьете', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-3]}ьют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'разо{name[3:-5]}ьюсь', '.ГНБ1е'),
            WordForm(f'разо{name[3:-5]}ьешься', '.ГНБ2е'),
            WordForm(f'разо{name[3:-5]}ьется', '.ГНБ3е'),
            WordForm(f'разо{name[3:-5]}ьемся', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-5]}ьетесь', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-5]}ьются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6д
def present_future_nbi6d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ду', '.ГНБ1е'),
            WordForm(f'{name[:-4]}дешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}дет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}дем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}дете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}дусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}дешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}дется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}демся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}детесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е
def present_future_nbi6e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ж
def present_future_nbi6g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}жу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}жешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}жет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}жем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}жете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}жут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}жешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}жется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}жемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}жетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}жутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6й
def present_future_nbi6j(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}йму', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ймешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ймет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ймем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ймете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ймут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}ймусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ймешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ймется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}ймемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}йметесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ймутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6м
def present_future_nbi6m(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}му', '.ГНБ1е'),
            WordForm(f'{name[:-4]}мешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}мет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}мем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}мете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}мут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}мусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}мешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}мется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}мемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}метесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}мутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6о
def present_future_nbi6o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ову', '.ГНБ1е'),
            WordForm(f'{name[:-4]}овешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}овет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}овем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}овете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}овут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}овусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}овешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}овется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}овемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}оветесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}овутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6т
def present_future_nbi6t(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ту', '.ГНБ1е'),
            WordForm(f'{name[:-4]}тешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}тет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}тем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}тете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}тут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}тусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}тешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}тется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}темся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}тетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}тутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ч
def present_future_nbi6ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}чем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}чете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}чут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}чемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}четесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}чутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ч-
def present_future_nbi6ch_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
        ]
    return word_forms


# НБI6ш
def present_future_nbi6sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}шу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}шешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}шет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}шем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}шете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}шут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}шешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}шется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}шемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}шетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}шутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6щ
def present_future_nbi6zsh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}щешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}щет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}щем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}щете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}щут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}щешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}щется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}щемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}щетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}щутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6ы
def present_future_nbi6ji(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ыму', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ымешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ымет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ымем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ымете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ымут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}ымусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ымешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ымется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}ымемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}ыметесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ымутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6я
def present_future_nbi6ja(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}яду', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ядешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ядет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ядем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ядете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ядут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}ядусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ядешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ядется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}ядемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}ядетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ядутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е*
def present_future_nbi6e_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}{name[2:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[0]}{name[2:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[0]}{name[2:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[0]}{name[2:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[0]}{name[2:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[0]}{name[2:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}{name[2:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[0]}{name[2:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[0]}{name[2:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[0]}{name[2:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[0]}{name[2:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}{name[2:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е**
def present_future_nbi6e_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е***
def present_future_nbi6e_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е****
def present_future_nbi6e_4prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:4]}{name[5:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[:4]}{name[5:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[:4]}{name[5:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[:4]}{name[5:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[:4]}{name[5:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[:4]}{name[5:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:4]}{name[5:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[:4]}{name[5:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[:4]}{name[5:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[:4]}{name[5:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[:4]}{name[5:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[:4]}{name[5:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е*****
def present_future_nbi6e_5prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:5]}{name[6:-4]}еру', '.ГНБ1е'),
            WordForm(f'{name[:5]}{name[6:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'{name[:5]}{name[6:-4]}ерет', '.ГНБ3е'),
            WordForm(f'{name[:5]}{name[6:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'{name[:5]}{name[6:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'{name[:5]}{name[6:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:5]}{name[6:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'{name[:5]}{name[6:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'{name[:5]}{name[6:-6]}ерется', '.ГНБ3е'),
            WordForm(f'{name[:5]}{name[6:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'{name[:5]}{name[6:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'{name[:5]}{name[6:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6е**!
def present_future_nbi6e_2prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'о{name[3:-4]}еру', '.ГНБ1е'),
            WordForm(f'о{name[3:-4]}ерешь', '.ГНБ2е'),
            WordForm(f'о{name[3:-4]}ерет', '.ГНБ3е'),
            WordForm(f'о{name[3:-4]}ерем', '.ГНБ1мн'),
            WordForm(f'о{name[3:-4]}ерете', '.ГНБ2мн'),
            WordForm(f'о{name[3:-4]}ерут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'о{name[3:-6]}ерусь', '.ГНБ1е'),
            WordForm(f'о{name[3:-6]}ерешься', '.ГНБ2е'),
            WordForm(f'о{name[3:-6]}ерется', '.ГНБ3е'),
            WordForm(f'о{name[3:-6]}еремся', '.ГНБ1мн'),
            WordForm(f'о{name[3:-6]}еретесь', '.ГНБ2мн'),
            WordForm(f'о{name[3:-6]}ерутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6й*
def present_future_nbi6j_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-4]}йму', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-4]}ймешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-4]}ймет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-4]}ймем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-4]}ймете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-4]}ймут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-6]}ймусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-6]}ймешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-6]}ймется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-6]}ймемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-6]}йметесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-6]}ймутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6о*
def present_future_nbi6o_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-4]}ову', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-4]}овешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-4]}овет', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-4]}овем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-4]}овете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-4]}овут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-6]}овусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-6]}овешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-6]}овется', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-6]}овемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-6]}оветесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-6]}овутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6о**
def present_future_nbi6o_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-4]}ову', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-4]}овешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-4]}овет', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-4]}овем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-4]}овете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-4]}овут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-6]}овусь', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-6]}овешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-6]}овется', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-6]}овемся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-6]}оветесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-6]}овутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6т*
def present_future_nbi6t_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-4]}ту', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-4]}тешь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-4]}тет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-4]}тем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-4]}тете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-4]}тут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-6]}тусь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-6]}тешься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-6]}тется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-6]}темся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-6]}тетесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-6]}тутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6т**
def present_future_nbi6t_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-4]}ту', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-4]}тешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-4]}тет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-4]}тем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-4]}тете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-4]}тут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-6]}тусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-6]}тешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-6]}тется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-6]}темся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-6]}тетесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-6]}тутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI6т***!
def present_future_nbi6t_3prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'разо{name[3:-4]}ту', '.ГНБ1е'),
            WordForm(f'разо{name[3:-4]}тешь', '.ГНБ2е'),
            WordForm(f'разо{name[3:-4]}тет', '.ГНБ3е'),
            WordForm(f'разо{name[3:-4]}тем', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-4]}тете', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-4]}тут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'разо{name[3:-6]}тусь', '.ГНБ1е'),
            WordForm(f'разо{name[3:-6]}тешься', '.ГНБ2е'),
            WordForm(f'разо{name[3:-6]}тется', '.ГНБ3е'),
            WordForm(f'разо{name[3:-6]}темся', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-6]}тетесь', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-6]}тутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7
def present_future_nbi7(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-4]}ешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}ет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}ем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}ете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}ют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}ешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}ется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}емся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}етесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}ются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7-
def present_future_nbi7_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}ет', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}ется', '.ГНБ3е'),
        ]
    return word_forms


# НБI7е
def present_future_nbi7e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}елю', '.ГНБ1е'),
            WordForm(f'{name[:-4]}елешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}елет', '.ГНБ3е'),
            WordForm(f'{name[:-4]}елем', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}елете', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}елюсь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}елешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}елется', '.ГНБ3е'),
            WordForm(f'{name[:-6]}елемся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}елетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7е*
def present_future_nbi7e_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-4]}елю', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-4]}елешь', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-4]}елет', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-4]}елем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-4]}елете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-4]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-6]}елюсь', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-6]}елешься', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-6]}елется', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-6]}елемся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-6]}елетесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-6]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7е**!
def present_future_nbi7e_2prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[3:-4]}елю', '.ГНБ1е'),
            WordForm(f'ис{name[3:-4]}елешь', '.ГНБ2е'),
            WordForm(f'ис{name[3:-4]}елет', '.ГНБ3е'),
            WordForm(f'ис{name[3:-4]}елем', '.ГНБ1мн'),
            WordForm(f'ис{name[3:-4]}елете', '.ГНБ2мн'),
            WordForm(f'ис{name[3:-4]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[3:-6]}елюсь', '.ГНБ1е'),
            WordForm(f'ис{name[3:-6]}елешься', '.ГНБ2е'),
            WordForm(f'ис{name[3:-6]}елется', '.ГНБ3е'),
            WordForm(f'ис{name[3:-6]}елемся', '.ГНБ1мн'),
            WordForm(f'ис{name[3:-6]}елетесь', '.ГНБ2мн'),
            WordForm(f'ис{name[3:-6]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI7е***!
def present_future_nbi7e_3prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[4:-4]}елю', '.ГНБ1е'),
            WordForm(f'рас{name[4:-4]}елешь', '.ГНБ2е'),
            WordForm(f'рас{name[4:-4]}елет', '.ГНБ3е'),
            WordForm(f'рас{name[4:-4]}елем', '.ГНБ1мн'),
            WordForm(f'рас{name[4:-4]}елете', '.ГНБ2мн'),
            WordForm(f'рас{name[4:-4]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[4:-6]}елюсь', '.ГНБ1е'),
            WordForm(f'рас{name[4:-6]}елешься', '.ГНБ2е'),
            WordForm(f'рас{name[4:-6]}елется', '.ГНБ3е'),
            WordForm(f'рас{name[4:-6]}елемся', '.ГНБ1мн'),
            WordForm(f'рас{name[4:-6]}елетесь', '.ГНБ2мн'),
            WordForm(f'рас{name[4:-6]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8щ
def present_future_nbi8shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-5]}щешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}щет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}щем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}щете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}щут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}щешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}щется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}щемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}щетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}щутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#
def present_future_nbi8_sharp(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}ру', '.ГНБ1е'),
            WordForm(f'{name[:-5]}решь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}рет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}рем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}рете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}русь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}решься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}рется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#*
def present_future_nbi8_sharp_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-5]}ру', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-5]}решь', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-5]}рет', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-5]}рем', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-5]}рете', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}о{name[1:-7]}русь', '.ГНБ1е'),
            WordForm(f'{name[0]}о{name[1:-7]}решься', '.ГНБ2е'),
            WordForm(f'{name[0]}о{name[1:-7]}рется', '.ГНБ3е'),
            WordForm(f'{name[0]}о{name[1:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'{name[0]}о{name[1:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}о{name[1:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#**
def present_future_nbi8_sharp_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}ру', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}решь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}рет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}рем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}рете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-7]}русь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-7]}решься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-7]}рется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#***
def present_future_nbi8_sharp_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-5]}ру', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-5]}решь', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-5]}рет', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-5]}рем', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}рете', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}о{name[3:-7]}русь', '.ГНБ1е'),
            WordForm(f'{name[:3]}о{name[3:-7]}решься', '.ГНБ2е'),
            WordForm(f'{name[:3]}о{name[3:-7]}рется', '.ГНБ3е'),
            WordForm(f'{name[:3]}о{name[3:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}о{name[3:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}о{name[3:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#****
def present_future_nbi8_sharp_4prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-5]}ру', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-5]}решь', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-5]}рет', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-5]}рем', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}рете', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:4]}о{name[4:-7]}русь', '.ГНБ1е'),
            WordForm(f'{name[:4]}о{name[4:-7]}решься', '.ГНБ2е'),
            WordForm(f'{name[:4]}о{name[4:-7]}рется', '.ГНБ3е'),
            WordForm(f'{name[:4]}о{name[4:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'{name[:4]}о{name[4:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'{name[:4]}о{name[4:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#*!
def present_future_nbi8_sharp_prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'обо{name[1:-5]}ру', '.ГНБ1е'),
            WordForm(f'обо{name[1:-5]}решь', '.ГНБ2е'),
            WordForm(f'обо{name[1:-5]}рет', '.ГНБ3е'),
            WordForm(f'обо{name[1:-5]}рем', '.ГНБ1мн'),
            WordForm(f'обо{name[1:-5]}рете', '.ГНБ2мн'),
            WordForm(f'обо{name[1:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'обо{name[1:-7]}русь', '.ГНБ1е'),
            WordForm(f'обо{name[1:-7]}решься', '.ГНБ2е'),
            WordForm(f'обо{name[1:-7]}рется', '.ГНБ3е'),
            WordForm(f'обо{name[1:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'обо{name[1:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'обо{name[1:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#**!
def present_future_nbi8_sharp_2prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'изо{name[2:-5]}ру', '.ГНБ1е'),
            WordForm(f'изо{name[2:-5]}решь', '.ГНБ2е'),
            WordForm(f'изо{name[2:-5]}рет', '.ГНБ3е'),
            WordForm(f'изо{name[2:-5]}рем', '.ГНБ1мн'),
            WordForm(f'изо{name[2:-5]}рете', '.ГНБ2мн'),
            WordForm(f'изо{name[2:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'изо{name[2:-7]}русь', '.ГНБ1е'),
            WordForm(f'изо{name[2:-7]}решься', '.ГНБ2е'),
            WordForm(f'изо{name[2:-7]}рется', '.ГНБ3е'),
            WordForm(f'изо{name[2:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'изо{name[2:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'изо{name[2:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#***!
def present_future_nbi8_sharp_3prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'разо{name[3:-5]}ру', '.ГНБ1е'),
            WordForm(f'разо{name[3:-5]}решь', '.ГНБ2е'),
            WordForm(f'разо{name[3:-5]}рет', '.ГНБ3е'),
            WordForm(f'разо{name[3:-5]}рем', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-5]}рете', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'разо{name[3:-7]}русь', '.ГНБ1е'),
            WordForm(f'разо{name[3:-7]}решься', '.ГНБ2е'),
            WordForm(f'разо{name[3:-7]}рется', '.ГНБ3е'),
            WordForm(f'разо{name[3:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'разо{name[3:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'разо{name[3:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI8#****!
def present_future_nbi8_sharp_4prim_excl(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'поизо{name[4:-5]}ру', '.ГНБ1е'),
            WordForm(f'поизо{name[4:-5]}решь', '.ГНБ2е'),
            WordForm(f'поизо{name[4:-5]}рет', '.ГНБ3е'),
            WordForm(f'поизо{name[4:-5]}рем', '.ГНБ1мн'),
            WordForm(f'поизо{name[4:-5]}рете', '.ГНБ2мн'),
            WordForm(f'поизо{name[4:-5]}рут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'поизо{name[4:-7]}русь', '.ГНБ1е'),
            WordForm(f'поизо{name[4:-7]}решься', '.ГНБ2е'),
            WordForm(f'поизо{name[4:-7]}рется', '.ГНБ3е'),
            WordForm(f'поизо{name[4:-7]}ремся', '.ГНБ1мн'),
            WordForm(f'поизо{name[4:-7]}ретесь', '.ГНБ2мн'),
            WordForm(f'поизо{name[4:-7]}рутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9е
def present_future_nbi9e(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}елю', '.ГНБ1е'),
            WordForm(f'{name[:-5]}елешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}елет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}елем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}елете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}елют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}елюсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}елешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}елется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}елемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}елетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}елются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9у
def present_future_nbi9u(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}ую', '.ГНБ1е'),
            WordForm(f'{name[:-5]}уешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ует', '.ГНБ3е'),
            WordForm(f'{name[:-5]}уем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}уете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}уют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}уюсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}уешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}уется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}уемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}уетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}уются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9у-
def present_future_nbi9u_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}ует', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}уется', '.ГНБ3е'),
        ]
    return word_forms


# НБI9ш
def present_future_nbi9sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}шлю', '.ГНБ1е'),
            WordForm(f'{name[:-5]}шлешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}шлет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}шлем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}шлете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}шлют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}шлюсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}шлешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}шлется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}шлемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}шлетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}шлются', '.ГНБ3мн'),
        ]
    return word_forms


# НБI9ю
def present_future_nbi9yu(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}юю', '.ГНБ1е'),
            WordForm(f'{name[:-5]}юешь', '.ГНБ2е'),
            WordForm(f'{name[:-5]}юет', '.ГНБ3е'),
            WordForm(f'{name[:-5]}юем', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}юете', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}юют', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}ююсь', '.ГНБ1е'),
            WordForm(f'{name[:-7]}юешься', '.ГНБ2е'),
            WordForm(f'{name[:-7]}юется', '.ГНБ3е'),
            WordForm(f'{name[:-7]}юемся', '.ГНБ1мн'),
            WordForm(f'{name[:-7]}юетесь', '.ГНБ2мн'),
            WordForm(f'{name[:-7]}юются', '.ГНБ3мн'),
        ]
    return word_forms


# НБII1
def present_future_nbii1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ат', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}атся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII1-
def present_future_nbii1_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
        ]
    return word_forms


# НБII2
def present_future_nbii2(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII2л
def present_future_nbii2l(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}люсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ж
def present_future_nbii3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}жу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ч
def present_future_nbii3ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3ш
def present_future_nbii3sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}шу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3щ
def present_future_nbii3shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII3-
def present_future_nbii3_dash(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII4о
def present_future_nbii4o(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}оню', '.ГНБ1е'),
            WordForm(f'{name[:-4]}онишь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}онит', '.ГНБ3е'),
            WordForm(f'{name[:-4]}оним', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}оните', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}онят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}онюсь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}онишься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}онится', '.ГНБ3е'),
            WordForm(f'{name[:-6]}онимся', '.ГНБ1мн'),
            WordForm(f'{name[:-6]}онитесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}онятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII4о*
def present_future_nbii4o_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[0]}{name[2:-4]}оню', '.ГНБ1е'),
            WordForm(f'{name[0]}{name[2:-4]}онишь', '.ГНБ2е'),
            WordForm(f'{name[0]}{name[2:-4]}онит', '.ГНБ3е'),
            WordForm(f'{name[0]}{name[2:-4]}оним', '.ГНБ1мн'),
            WordForm(f'{name[0]}{name[2:-4]}оните', '.ГНБ2мн'),
            WordForm(f'{name[0]}{name[2:-4]}онят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[0]}{name[2:-6]}онюсь', '.ГНБ1е'),
            WordForm(f'{name[0]}{name[2:-6]}онишься', '.ГНБ2е'),
            WordForm(f'{name[0]}{name[2:-6]}онится', '.ГНБ3е'),
            WordForm(f'{name[0]}{name[2:-6]}онимся', '.ГНБ1мн'),
            WordForm(f'{name[0]}{name[2:-6]}онитесь', '.ГНБ2мн'),
            WordForm(f'{name[0]}{name[2:-6]}онятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII4о**
def present_future_nbii4o_2prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-4]}оню', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-4]}онишь', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-4]}онит', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-4]}оним', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-4]}оните', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-4]}онят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}{name[3:-6]}онюсь', '.ГНБ1е'),
            WordForm(f'{name[:2]}{name[3:-6]}онишься', '.ГНБ2е'),
            WordForm(f'{name[:2]}{name[3:-6]}онится', '.ГНБ3е'),
            WordForm(f'{name[:2]}{name[3:-6]}онимся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}{name[3:-6]}онитесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}{name[3:-6]}онятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII4о***
def present_future_nbii4o_3prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-4]}оню', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-4]}онишь', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-4]}онит', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-4]}оним', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-4]}оните', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-4]}онят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:3]}{name[4:-6]}онюсь', '.ГНБ1е'),
            WordForm(f'{name[:3]}{name[4:-6]}онишься', '.ГНБ2е'),
            WordForm(f'{name[:3]}{name[4:-6]}онится', '.ГНБ3е'),
            WordForm(f'{name[:3]}{name[4:-6]}онимся', '.ГНБ1мн'),
            WordForm(f'{name[:3]}{name[4:-6]}онитесь', '.ГНБ2мн'),
            WordForm(f'{name[:3]}{name[4:-6]}онятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII4о****
def present_future_nbii4o_4prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:5]}{name[6:-4]}оню', '.ГНБ1е'),
            WordForm(f'{name[:5]}{name[6:-4]}онишь', '.ГНБ2е'),
            WordForm(f'{name[:5]}{name[6:-4]}онит', '.ГНБ3е'),
            WordForm(f'{name[:5]}{name[6:-4]}оним', '.ГНБ1мн'),
            WordForm(f'{name[:5]}{name[6:-4]}оните', '.ГНБ2мн'),
            WordForm(f'{name[:5]}{name[6:-4]}онят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:5]}{name[6:-6]}онюсь', '.ГНБ1е'),
            WordForm(f'{name[:5]}{name[6:-6]}онишься', '.ГНБ2е'),
            WordForm(f'{name[:5]}{name[6:-6]}онится', '.ГНБ3е'),
            WordForm(f'{name[:5]}{name[6:-6]}онимся', '.ГНБ1мн'),
            WordForm(f'{name[:5]}{name[6:-6]}онитесь', '.ГНБ2мн'),
            WordForm(f'{name[:5]}{name[6:-6]}онятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII5щ
def present_future_nbii5shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}щу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}щусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII6щ
def present_future_nbii6shch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-5]}щвлю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-7]}щвлюсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБII*д
def present_future_nbii_prim_d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}м', '.ГНБ1е'),
            WordForm(f'{name[:-3]}шь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ст', '.ГНБ3е'),
            WordForm(f'{name[:-3]}дим', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}дите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}дят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}мся', '.ГНБ1е'),
            WordForm(f'{name[:-5]}шься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}стся', '.ГНБ3е'),
            WordForm(f'{name[:-5]}димся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}дитесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}дятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI-II3
def present_future_nbi_ii3(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}у', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ышь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ыт', '.ГНБ3е'),
            WordForm(f'{name[:-3]}ым', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ыте', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}усь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ышься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ытся', '.ГНБ3е'),
            WordForm(f'{name[:-5]}ымся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}ытесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}утся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI-II4ч
def present_future_nbi_ii4ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}чу', '.ГНБ1е'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI-II5г
def present_future_nbi_ii5g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-4]}гу', '.ГНБ1е'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}гут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-6]}гусь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-6]}гутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI-II*д
def present_future_nbi_ii_prim_d(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}м', '.ГНБ1е'),
            WordForm(f'{name[:-2]}шь', '.ГНБ2е'),
            WordForm(f'{name[:-2]}ст', '.ГНБ3е'),
            WordForm(f'{name[:-2]}дим', '.ГНБ1мн'),
            WordForm(f'{name[:-2]}дите', '.ГНБ2мн'),
            WordForm(f'{name[:-2]}дут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}мся', '.ГНБ1е'),
            WordForm(f'{name[:-4]}шься', '.ГНБ2е'),
            WordForm(f'{name[:-4]}стся', '.ГНБ3е'),
            WordForm(f'{name[:-4]}димся', '.ГНБ1мн'),
            WordForm(f'{name[:-4]}дитесь', '.ГНБ2мн'),
            WordForm(f'{name[:-4]}дутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI4ь*
def present_future_nbi4y_prim(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-3]}ьму', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьмешь', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьмет', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьмем', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьмете', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-3]}ьмут', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:2]}о{name[2:-5]}ьмусь', '.ГНБ1е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьмешься', '.ГНБ2е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьмется', '.ГНБ3е'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьмемся', '.ГНБ1мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьметесь', '.ГНБ2мн'),
            WordForm(f'{name[:2]}о{name[2:-5]}ьмутся', '.ГНБ3мн'),
        ]
    return word_forms


# НБI3&6ч
def present_future_nbi3_6ch(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}чу', '.ГНБ1е2'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е1'),
            WordForm(f'{name[:-4]}чешь', '.ГНБ2е2'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е1'),
            WordForm(f'{name[:-4]}чет', '.ГНБ3е2'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн1'),
            WordForm(f'{name[:-4]}чем', '.ГНБ1мн2'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн1'),
            WordForm(f'{name[:-4]}чете', '.ГНБ2мн2'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн1'),
            WordForm(f'{name[:-4]}чут', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}чусь', '.ГНБ1е2'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е1'),
            WordForm(f'{name[:-6]}чешься', '.ГНБ2е2'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е1'),
            WordForm(f'{name[:-6]}чется', '.ГНБ3е2'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн1'),
            WordForm(f'{name[:-6]}чемся', '.ГНБ1мн2'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-6]}четесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн1'),
            WordForm(f'{name[:-6]}чутся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБI3&6ш
def present_future_nbi3_6sh(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-2]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}шу', '.ГНБ1е2'),
            WordForm(f'{name[:-2]}ешь', '.ГНБ2е1'),
            WordForm(f'{name[:-4]}шешь', '.ГНБ2е2'),
            WordForm(f'{name[:-2]}ет', '.ГНБ3е1'),
            WordForm(f'{name[:-4]}шет', '.ГНБ3е2'),
            WordForm(f'{name[:-2]}ем', '.ГНБ1мн1'),
            WordForm(f'{name[:-4]}шем', '.ГНБ1мн2'),
            WordForm(f'{name[:-2]}ете', '.ГНБ2мн1'),
            WordForm(f'{name[:-4]}шете', '.ГНБ2мн2'),
            WordForm(f'{name[:-2]}ют', '.ГНБ3мн1'),
            WordForm(f'{name[:-4]}шут', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-4]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}шусь', '.ГНБ1е2'),
            WordForm(f'{name[:-4]}ешься', '.ГНБ2е1'),
            WordForm(f'{name[:-6]}шешься', '.ГНБ2е2'),
            WordForm(f'{name[:-4]}ется', '.ГНБ3е1'),
            WordForm(f'{name[:-6]}шется', '.ГНБ3е2'),
            WordForm(f'{name[:-4]}емся', '.ГНБ1мн1'),
            WordForm(f'{name[:-6]}шемся', '.ГНБ1мн2'),
            WordForm(f'{name[:-4]}етесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-6]}шетесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-4]}ются', '.ГНБ3мн1'),
            WordForm(f'{name[:-6]}шутся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБI5л&I-II1
def present_future_nbi5l_and_i_ii1(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}лю', '.ГНБ1е'),
            WordForm(f'{name[:-3]}лешь', '.ГНБ2е1'),
            WordForm(f'{name[:-3]}ешь', '.ГНБ2е2'),
            WordForm(f'{name[:-3]}лет', '.ГНБ3е1'),
            WordForm(f'{name[:-3]}ет', '.ГНБ3е2'),
            WordForm(f'{name[:-3]}лем', '.ГНБ1мн1'),
            WordForm(f'{name[:-3]}ем', '.ГНБ1мн2'),
            WordForm(f'{name[:-3]}лете', '.ГНБ2мн1'),
            WordForm(f'{name[:-3]}ете', '.ГНБ2мн2'),
            WordForm(f'{name[:-3]}лют', '.ГНБ3мн1'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн2'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}люсь', '.ГНБ1е'),
            WordForm(f'{name[:-5]}лешься', '.ГНБ2е1'),
            WordForm(f'{name[:-5]}ешься', '.ГНБ2е2'),
            WordForm(f'{name[:-5]}лется', '.ГНБ3е1'),
            WordForm(f'{name[:-5]}ется', '.ГНБ3е2'),
            WordForm(f'{name[:-5]}лемся', '.ГНБ1мн1'),
            WordForm(f'{name[:-5]}емся', '.ГНБ1мн2'),
            WordForm(f'{name[:-5]}летесь', '.ГНБ2мн1'),
            WordForm(f'{name[:-5]}етесь', '.ГНБ2мн2'),
            WordForm(f'{name[:-5]}лются', '.ГНБ3мн1'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн2'),
        ]
    return word_forms


# НБII2+3ж
def present_future_nbii2_and_3g(src_dict) -> list:
    name = src_dict['name']
    if not name.endswith(('ся', 'сь')):
        word_forms = [
            WordForm(f'{name[:-3]}ю', '.ГНБ1е1'),
            WordForm(f'{name[:-4]}жу', '.ГНБ1е2'),
            WordForm(f'{name[:-3]}ишь', '.ГНБ2е'),
            WordForm(f'{name[:-3]}ит', '.ГНБ3е'),
            WordForm(f'{name[:-3]}им', '.ГНБ1мн'),
            WordForm(f'{name[:-3]}ите', '.ГНБ2мн'),
            WordForm(f'{name[:-3]}ят', '.ГНБ3мн'),
        ]
    else:
        word_forms = [
            WordForm(f'{name[:-5]}юсь', '.ГНБ1е1'),
            WordForm(f'{name[:-6]}жусь', '.ГНБ1е2'),
            WordForm(f'{name[:-5]}ишься', '.ГНБ2е'),
            WordForm(f'{name[:-5]}ится', '.ГНБ3е'),
            WordForm(f'{name[:-5]}имся', '.ГНБ1мн'),
            WordForm(f'{name[:-5]}итесь', '.ГНБ2мн'),
            WordForm(f'{name[:-5]}ятся', '.ГНБ3мн'),
        ]
    return word_forms
