"""Все Глаголы"""


from collections import OrderedDict
from pathlib import Path

from rem import reminder_nouns
from utils import save_list_of_lists_to_csv_file, save_list_to_file
from word_form import TitleWordForm


# Глаголы.txt
def get_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Г')
    ]
    return word_forms


# Глаголы нес. вида.txt
def get_imperfective_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано нес ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and 'нес' in group.title_word_form.info)
    ]
    return word_forms


# Глаголы сов. вида.txt
def get_perfect_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано сов ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and 'сов' in group.title_word_form.info)
    ]
    return word_forms


# Двувидовые глаголы.txt
def get_two_species_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано 2в ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and '2в' in group.title_word_form.info)
    ]
    return word_forms


# Переходные глаголы.txt
def get_transitive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано пер ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and 'пер' in group.title_word_form.info)
    ]
    return word_forms


# Непереходные глаголы.txt
def get_intransitive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указано неп ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and 'неп' in group.title_word_form.info)
    ]
    return word_forms


# Безличные глаголы.txt
def get_impersonal_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации имеется индикатор безличности б ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and 'б' in group.title_word_form.info)
    ]
    return word_forms


# Возвратные глаголы.txt
def get_reflexive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается на -СЯ / -СЬ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and group.title_word_form.name.endswith(('ся', 'сь')))
    ]
    return word_forms


# Невозвратные глаголы.txt
def get_non_reflexive_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается не на -СЯ / -СЬ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and not group.title_word_form.name.endswith(('ся', 'сь')))
    ]
    return word_forms


# Глаголы -ШЕЛ(СЯ).txt
def get_walked_verbs(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и ЗС оканчивается на -ШЕЛ(СЯ) ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and group.title_word_form.name.endswith(('шел', 'шелся')))
    ]
    return word_forms


# Глаголы I спр.txt
def get_verbs_of_first_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит римскую цифру I
    (кроме шаблонов НБ вр., название которого содержит
    сочетание римских цифр I-II ,
    а также шаблонов НБ вр. I3&II2 / I3&II2л / I8щ&II5щ ,
    и кроме глаголов с дефисом, т.е.
    кроме ЗС групп, идентификатор которых содержит .Г , а также -Г)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_first_conj(group.title_word_form)
    ]
    return word_forms


def is_first_conj(form: TitleWordForm):
    """
    Для 'Глаголы I спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')
            and '-' not in form.idf
            and 'I-II' not in info_list[0]
            and info_list[0].startswith('НБI')
            and not info_list[0].startswith((
                'НБII', 'НБI3&II2', 'НБI3&II2л', 'НБI8щ&II5щ'))
    ):
        return True
    else:
        return False


# Глаголы II спр.txt
def get_verbs_of_second_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит римскую цифру II
    (кроме шаблонов НБ вр., название которого содержит
    сочетание римских цифр I-II ,
    а также шаблонов НБ вр. I3&II2 / I3&II2л / I8щ&II5щ ,
    и кроме глаголов с дефисом, т.е. кроме ЗС групп,
    идентификатор которых содержит .Г , а также -Г)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_second_conj(group.title_word_form)
    ]
    return word_forms


def is_second_conj(form: TitleWordForm):
    """
    Для 'Глаголы II спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')
            and '-' not in form.name
            and 'II' in info_list[0]
            and 'I-II' not in info_list[0]
            and '&' not in info_list[0]
    ):
        return True
    else:
        return False


# Глаголы смеш. спр.txt
def get_verbs_of_mixed_conj(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан шаблон НБ вр.,
    название которого содержит сочетание римских цифр I-II ,
    а также следующие шаблоны НБ вр.: I3&II2 / I3&II2л / I8щ&II5щ ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if is_mixed_conj(group.title_word_form)
    ]
    return word_forms


def is_mixed_conj(form: TitleWordForm):
    """
    Для 'Глаголы смеш. спр.txt'
    """

    info_list = [x for x in form.info if x.startswith('НБ')]
    if (
            info_list
            and form.idf.startswith('.Г')

            and (
                'I-II' in info_list[0]
                or
                ('II' in info_list[0] and '&' in info_list[0])
            )
    ):
        return True
    else:
        return False


# Глаголы с дефисом.txt
def get_verbs_hyphenated(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в ЗС имеется хотя бы 1 дефис."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Г')
            and '-' in group.title_word_form.name)
    ]
    return word_forms


# Глаголы. Сочетания шаблонов.csv
def save_verbs_pattern_combinations(word_forms_bases, _):
    """
    1. Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
        и в ЗС отсутствует дефис .

    2. Выбрать из найденных строк строки с уникальным сочетанием
        элементов спец. информации (ЭСИ).

        Примечание 1. Подробнее об ЭСИ - см. документ Структура строки.xlsx ,
        вкладка Структура спец. информации.

        Примечание 2. При наличии нескольких строк с одинаковым сочетанием ЭСИ
        выбирать первую (верхнюю) строку, т.е. строку,
        слово в которой идёт первым по алфавиту.

    3. Создать документ Глаголы. Сочетания шаблонов.csv .
        Вставить в 14 столбцов этого документа выбранные строки
        (слово - в первый столбец, ЭСИ - в другие 13 столбцов).

    4. Расположить строки следующим образом:
        сначала - учитывая наличие / отсутствие индикатора безличности;
        затем - в соответствии с алфавитным порядком названий шаблонов
        настоящего / будущего времени;
        затем - в соответствии с алфавитным порядком остальных
        ЭСИ, кроме вида и переходности;
        затем - в соответствии с алфавитным порядком указателя вида;
        затем - в соответствии с алфавитным порядком указателя переходности.

    5. Вставить в верхнюю часть документа "шапку"-памятку.

    6. Сохранить документ Глаголы. Сочетания шаблонов.csv .
    """

    word_forms = []
    unique_elements = []

    for group in word_forms_bases:
        if (
                group.title_word_form.idf.startswith('.Г')
                and '-' not in group.title_word_form.name
        ):
            elements = ' '.join(group.title_word_form.info)
            if elements not in unique_elements:
                unique_elements.append(elements)
                word_forms.append(group.title_word_form)

    header_1 = [
        '',
        'вид',
        'переходность',
        'безличность',
        'настоящее /\nбудущее время',
        'прошедшее время',
        'повелительное наклонение',
        'форма совместного действия',
        'причастие настоящего\nвремени действительное',
        'причастие настоящего\nвремени страдательное',
        'причастие прошедшего\nвремени действительное',
        'причастие прошедшего\nвремени страдательное',
        'деепричастие\nнастоящего времени',
        'деепричастие\nпрошедшего времени',
    ]

    header_2 = [
        '',
        '',
        '',
        '',
        'Глаголы,\nНЕ образующие НБ вр.,\nнужно вносить в список 1',
        'НЕ образуется для\nГРЯСТИ, ИДТИ, ИЗЫТИ',
        'НЕ образуется для\nМИНУТЬ\nи глаголов из списка 1',
        'Глаголы нес. вида,\nобразующие форму СД,\nнужно вносить в список 44',
        'НЕ образуется для\nБЫТЬ, ШЕЛ\nи глаголов из списка 1',
        'Глаголы,\nНЕ образующие ПНС,\nнужно вносить\nв список 46',
        'НЕ образуется для\nГРЯСТИ, ИДТИ, ИЗЫТИ',
        'Глаголы,\nНЕ образующие ППС,\nнужно вносить\nв списки 53, 54, 55, 56',
        'Глаголы,\nНЕ образующие ДН,\nнужно вносить\nв список 61',
        'Глаголы,\nНЕ образующие ДН,\nнужно вносить\nв список 63',
    ]

    header_3 = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        'НЕ образуется для\nглаголов сов. вида\nиз списка 1',
        '',
        'НЕ образуется для\nгл-ов из списка 1\nи для гл-ов I спр.\n'
        'с единственной словоформой\n.ГНБ3мн на\n-ЖУТ / -ЧУТ / -ШУТ / -ЩУТ',
        '',
        'НЕ образуется для\nГНЕВАТЬ ',
        'НЕ образуется для\nглаголов из списка 1',
        '',
    ]

    in_form_of_list = []

    for form in word_forms:
        indicators = OrderedDict({
            'name': form.name,
            'вид': '',  # нес сов 2в
            'переходность': '',  # пер неп
            'безличность': '',  # б (если есть)
            'шаблон НБ': '',  # НБ... (если есть)
            'шаблон П': '',  # П... (если есть)
            'шаблон Пв': '',  # Пв... (если есть)
            'шаблон С': '',  # С... (если есть)
            'шаблон ПНД': '',  # ПНД... (если есть)
            'шаблон ПНС': '',  # ПНС... (если есть)
            'шаблон ППД': '',  # ППД... (если есть)
            'шаблон ППС': '',  # ППС... (если есть)
            'шаблон ДН': '',  # ДН... (если есть)
            'шаблон ДП': '',  # ДП... (если есть)
        })

        for indicator in form.info:
            if indicator in ('нес', 'сов', '2в'):
                indicators['вид'] = indicator
            elif indicator in ('пер', 'неп'):
                indicators['переходность'] = indicator
            elif indicator == 'б':
                indicators['безличность'] = indicator
            elif indicator.startswith('НБ'):
                indicators['шаблон НБ'] = indicator
            elif (indicator.startswith('П')
                  and not indicator.startswith(('Пв', 'ПН', 'ПП'))):
                indicators['шаблон П'] = indicator
            elif indicator.startswith('Пв'):
                indicators['шаблон Пв'] = indicator
            elif indicator.startswith('С'):
                indicators['шаблон С'] = indicator
            elif indicator.startswith('ПНД'):
                indicators['шаблон ПНД'] = indicator
            elif indicator.startswith('ПНС'):
                indicators['шаблон ПНС'] = indicator
            elif indicator.startswith('ППД'):
                indicators['шаблон ППД'] = indicator
            elif indicator.startswith('ППС'):
                indicators['шаблон ППС'] = indicator
            elif indicator.startswith('ДН'):
                indicators['шаблон ДН'] = indicator
            elif indicator.startswith('ДП'):
                indicators['шаблон ДП'] = indicator

        in_form_of_list.append(list(indicators.values()))

    in_form_of_list = sorted(
        in_form_of_list,
        key=lambda x: (x[3], x[4], x[5], x[6], x[7], x[8],
                       x[9], x[10], x[11], x[12], x[13], x[1], x[2])
    )

    in_form_of_list.insert(0, header_3)
    in_form_of_list.insert(0, header_2)
    in_form_of_list.insert(0, header_1)

    print(f'\n{reminder_nouns}\n')

    save_list_of_lists_to_csv_file(
        in_form_of_list,
        'Глаголы. Сочетания шаблонов.csv',
        encoding='cp1251',
        delimiter=';'
    )


# Глаголы. Идентификаторы.txt
def get_verbs_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Глаголы с дефисом.txt .
    2. Найти в БС группы с ЗС, идентификатор которых содержит .Г
        (кроме ЗС из документа Глаголы с дефисом.txt).
    3. Создать документ Глаголы. Идентификаторы.txt и вставить в него
        все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала учитывая порядок форм (сначала идентификаторы инфинитива,
        затем настоящего / будущего времени, затем прошедшего времени и т. д.):
        И НБ П Пв СД ПНД ПНС ППД ППС ДН ДП ;
        затем с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем с учётом лица (сначала идентификаторы 1-ого лица, затем 2-ого,
        затем 3-его) - только для форм настоящего / будущего времени;
        затем с учётом рода (сначала идентификаторы мужского рода,
        затем женского, затем среднего);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком
        остальных элементов идентификаторов.
    6. Сохранить документ Глаголы. Идентификаторы.txt .
    """

    # Глаголы с дефисом.txt
    verbs_hyphenated = get_verbs_hyphenated(word_forms_bases, _)
    save_list_to_file(verbs_hyphenated, 'Глаголы с дефисом.txt',
                      encoding='cp1251')
    print(f'Создан документ: Глаголы с дефисом.txt')
    print(f'... сортировка ...')

    sorting_by_case = {
        'И': 1,
        'Р': 2,
        'Д': 3,
        'В': 4,
        'Т': 5,
        'Т1': 6,
        'Т2': 7,
        'Т3': 8,
        'П': 9,
    }

    sorting_by_gender = {
        'м': 1,
        'м1': 2,
        'м2': 3,
        'м3': 4,
        'ж': 5,
        'ж1': 6,
        'ж2': 7,
        'ж3': 8,
        'с': 9,
        'с1': 10,
        'с2': 11,
        'с3': 12,
        'мн': 13,
        'мн1': 14,
        'мн2': 15,
        'мн3': 16,
    }

    gi_idf = set()  # .ГИ
    gnb_idf = set()  # .ГНБ
    gp_idf = set()  # .ГП
    gpv_idf = set()  # .ГПв
    gs_idf = set()  # .ГС

    pndm_idf = set()  # .ПНДм
    pndz_idf = set()  # .ПНДж
    pnds_idf = set()  # .ПНДс
    pndmn_idf = set()  # .ПНДмн

    pndk_idf = set()  # .ПНДК

    pnd1m_idf = set()  # .ПНД1м
    pnd1z_idf = set()  # .ПНД1ж
    pnd1s_idf = set()  # .ПНД1с
    pnd1mn_idf = set()  # .ПНД1мн

    pnd2m_idf = set()  # .ПНД2м
    pnd2z_idf = set()  # .ПНД2ж
    pnd2s_idf = set()  # .ПНД2с
    pnd2mn_idf = set()  # .ПНД2мн

    pnsm_idf = set()  # .ПНСм
    pnsz_idf = set()  # .ПНСж
    pnss_idf = set()  # .ПНСс
    pnsmn_idf = set()  # .ПНСмн

    pnsk_idf = set()  # .ПНСКм

    pns1m_idf = set()  # .ПНС1м
    pns1z_idf = set()  # .ПНС1ж
    pns1s_idf = set()  # .ПНС1с
    pns1mn_idf = set()  # .ПНС1мн

    pns2m_idf = set()  # .ПНС2м
    pns2z_idf = set()  # .ПНС2ж
    pns2s_idf = set()  # .ПНС2с
    pns2mn_idf = set()  # .ПНС2мн

    ppdm_idf = set()  # .ППДм
    ppdz_idf = set()  # .ППДж
    ppds_idf = set()  # .ППДс
    ppdmn_idf = set()  # .ППДмн

    ppd1m_idf = set()  # .ППД1м
    ppd1z_idf = set()  # .ППД1ж
    ppd1s_idf = set()  # .ППД1с
    ppd1mn_idf = set()  # .ППД1мн

    ppd2m_idf = set()  # .ППД2м
    ppd2z_idf = set()  # .ППД2ж
    ppd2s_idf = set()  # .ППД2с
    ppd2mn_idf = set()  # .ППД2мн

    ppsm_idf = set()  # .ППСм
    ppsz_idf = set()  # .ППСж
    ppss_idf = set()  # .ППСс
    ppsmn_idf = set()  # .ППСмн

    pps1m_idf = set()  # .ППС1м
    pps1z_idf = set()  # .ППС1ж
    pps1s_idf = set()  # .ППС1с
    pps1mn_idf = set()  # .ППС1мн

    pps2m_idf = set()  # .ППС2м
    pps2z_idf = set()  # .ППС2ж
    pps2s_idf = set()  # .ППС2с
    pps2mn_idf = set()  # .ППС2мн

    ppsk_idf = set()  # .ППСКм

    dn_idf = set()  # .ДН
    dp_idf = set()  # .ДП

    identifiers = []

    for group in word_forms_bases:
        if (str(group.title_word_form) not in verbs_hyphenated
                and group.title_word_form.idf.startswith('.Г')):
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier.startswith('.ГИ'):
                    gi_idf.add(identifier)
                elif identifier.startswith('.ГНБ'):
                    gnb_idf.add(identifier)
                elif identifier.startswith('.ГПв'):
                    gpv_idf.add(identifier)
                elif identifier.startswith('.ГС'):
                    gs_idf.add(identifier)

                elif (identifier.startswith('.ПНД1м')
                      and not identifier.startswith('.ПНД1мн')):
                    pnd1m_idf.add(identifier)
                elif identifier.startswith('.ПНД1ж'):
                    pnd1z_idf.add(identifier)
                elif identifier.startswith('.ПНД1с'):
                    pnd1s_idf.add(identifier)
                elif identifier.startswith('.ПНД1мн'):
                    pnd1mn_idf.add(identifier)

                elif (identifier.startswith('.ПНД2м')
                      and not identifier.startswith('.ПНД2мн')):
                    pnd2m_idf.add(identifier)
                elif identifier.startswith('.ПНД2ж'):
                    pnd2z_idf.add(identifier)
                elif identifier.startswith('.ПНД2с'):
                    pnd2s_idf.add(identifier)
                elif identifier.startswith('.ПНД2мн'):
                    pnd2mn_idf.add(identifier)

                elif identifier.startswith('.ПНДК'):
                    pndk_idf.add(identifier)

                elif (identifier.startswith('.ПНДм')
                      and not identifier.startswith('.ПНДмн')):
                    pndm_idf.add(identifier)
                elif identifier.startswith('.ПНДж'):
                    pndz_idf.add(identifier)
                elif identifier.startswith('.ПНДс'):
                    pnds_idf.add(identifier)
                elif identifier.startswith('.ПНДмн'):
                    pndmn_idf.add(identifier)

                elif (identifier.startswith('.ПНС1м')
                      and not identifier.startswith('.ПНС1мн')):
                    pns1m_idf.add(identifier)
                elif identifier.startswith('.ПНС1ж'):
                    pns1z_idf.add(identifier)
                elif identifier.startswith('.ПНС1с'):
                    pns1s_idf.add(identifier)
                elif identifier.startswith('.ПНС1мн'):
                    pns1mn_idf.add(identifier)

                elif (identifier.startswith('.ПНС2м')
                      and not identifier.startswith('.ПНС2мн')):
                    pns2m_idf.add(identifier)
                elif identifier.startswith('.ПНС2ж'):
                    pns2z_idf.add(identifier)
                elif identifier.startswith('.ПНС2с'):
                    pns2s_idf.add(identifier)
                elif identifier.startswith('.ПНС2мн'):
                    pns2mn_idf.add(identifier)

                elif identifier.startswith('.ПНСК'):
                    pnsk_idf.add(identifier)

                elif (identifier.startswith('.ПНСм')
                      and not identifier.startswith('.ПНСмн')):
                    pnsm_idf.add(identifier)
                elif identifier.startswith('.ПНСж'):
                    pnsz_idf.add(identifier)
                elif identifier.startswith('.ПНСс'):
                    pnss_idf.add(identifier)
                elif identifier.startswith('.ПНСмн'):
                    pnsmn_idf.add(identifier)

                elif (identifier.startswith('.ППД1м')
                      and not identifier.startswith('.ППД1мн')):
                    ppd1m_idf.add(identifier)
                elif identifier.startswith('.ППД1ж'):
                    ppd1z_idf.add(identifier)
                elif identifier.startswith('.ППД1с'):
                    ppd1s_idf.add(identifier)
                elif identifier.startswith('.ППД1мн'):
                    ppd1mn_idf.add(identifier)

                elif (identifier.startswith('.ППД2м')
                      and not identifier.startswith('.ППД2мн')):
                    ppd2m_idf.add(identifier)
                elif identifier.startswith('.ППД2ж'):
                    ppd2z_idf.add(identifier)
                elif identifier.startswith('.ППД2с'):
                    ppd2s_idf.add(identifier)
                elif identifier.startswith('.ППД2мн'):
                    ppd2mn_idf.add(identifier)

                elif (identifier.startswith('.ППДм')
                      and not identifier.startswith('.ППДмн')):
                    ppdm_idf.add(identifier)
                elif identifier.startswith('.ППДж'):
                    ppdz_idf.add(identifier)
                elif identifier.startswith('.ППДс'):
                    ppds_idf.add(identifier)
                elif identifier.startswith('.ППДмн'):
                    ppdmn_idf.add(identifier)

                elif (identifier.startswith('.ППС1м')
                      and not identifier.startswith('.ППС1мн')):
                    pps1m_idf.add(identifier)
                elif identifier.startswith('.ППС1ж'):
                    pps1z_idf.add(identifier)
                elif identifier.startswith('.ППС1с'):
                    pps1s_idf.add(identifier)
                elif identifier.startswith('.ППС1мн'):
                    pps1mn_idf.add(identifier)

                elif (identifier.startswith('.ППС2м')
                      and not identifier.startswith('.ППС2мн')):
                    pps2m_idf.add(identifier)
                elif identifier.startswith('.ППС2ж'):
                    pps2z_idf.add(identifier)
                elif identifier.startswith('.ППС2с'):
                    pps2s_idf.add(identifier)
                elif identifier.startswith('.ППС2мн'):
                    pps2mn_idf.add(identifier)

                elif identifier.startswith('.ППСК'):
                    ppsk_idf.add(identifier)

                elif (identifier.startswith('.ППСм')
                      and not identifier.startswith('.ППСмн')):
                    ppsm_idf.add(identifier)
                elif identifier.startswith('.ППСж'):
                    ppsz_idf.add(identifier)
                elif identifier.startswith('.ППСс'):
                    ppss_idf.add(identifier)
                elif identifier.startswith('.ППСмн'):
                    ppsmn_idf.add(identifier)

                elif identifier.startswith('.ДН'):
                    dn_idf.add(identifier)
                elif identifier.startswith('.ДП'):
                    dp_idf.add(identifier)

                elif identifier.startswith('.ГП'):
                    gp_idf.add(identifier)

    identifiers += sorted(list(gi_idf))
    identifiers += sorted(list(gnb_idf))
    identifiers += sorted(list(gp_idf), key=lambda x: sorting_by_gender[x[3:]])
    identifiers += sorted(list(gpv_idf))
    identifiers += sorted(list(gs_idf))

    identifiers += sorted(list(pndm_idf), key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pndz_idf), key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pnds_idf), key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pndmn_idf),
                          key=lambda x: sorting_by_case[x[6:]])

    identifiers += sorted(list(pndk_idf),
                          key=lambda x: sorting_by_gender[x[5:]])

    identifiers += sorted(list(pnd1m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd1z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd1s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd1mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(pnd2m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd2z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd2s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pnd2mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(pnsm_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pnsz_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pnss_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(pnsmn_idf),
                          key=lambda x: sorting_by_case[x[6:]])

    identifiers += sorted(list(pnsk_idf),
                          key=lambda x: sorting_by_gender[x[5:]])

    identifiers += sorted(list(pns1m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns1z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns1s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns1mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(pns2m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns2z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns2s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pns2mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(ppdm_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppdz_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppds_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppdmn_idf),
                          key=lambda x: sorting_by_case[x[6:]])

    identifiers += sorted(list(ppd1m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd1z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd1s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd1mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(ppd2m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd2z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd2s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(ppd2mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(ppsm_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppsz_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppss_idf),
                          key=lambda x: sorting_by_case[x[5:]])
    identifiers += sorted(list(ppsmn_idf),
                          key=lambda x: sorting_by_case[x[6:]])

    identifiers += sorted(list(pps1m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps1z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps1s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps1mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(pps2m_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps2z_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps2s_idf),
                          key=lambda x: sorting_by_case[x[6:]])
    identifiers += sorted(list(pps2mn_idf),
                          key=lambda x: sorting_by_case[x[7:]])

    identifiers += sorted(list(ppsk_idf),
                          key=lambda x: sorting_by_gender[x[5:]])

    identifiers += sorted(list(dn_idf))
    identifiers += sorted(list(dp_idf))

    return identifiers


# Глаголы с дефисом. Идентификаторы.txt
def get_verbs_hyphenated_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Глаголы с дефисом.txt .
    2. Найти в БС группы с ЗС из документа Глаголы с дефисом.txt .
    3. Создать документ Глаголы с дефисом. Идентификаторы.txt
        и вставить в него все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала учитывая порядок форм (сначала идентификаторы инфинитива,
        затем настоящего / будущего времени,
        затем прошедшего времени и т. д.): И НБ П Пв СД ПНД ПНС ППД ППС ДН ДП ;
        затем с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем с учётом лица (сначала идентификаторы 1-ого лица, затем 2-ого,
        затем 3-его) - только для форм настоящего / будущего времени;
        затем с учётом рода (сначала идентификаторы мужского рода,
        затем женского, затем среднего);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком
        остальных элементов идентификаторов.
    6. Сохранить документ Глаголы с дефисом. Идентификаторы.txt .
    """

    # Глаголы с дефисом.txt
    verbs_hyphenated = get_verbs_hyphenated(word_forms_bases, _)
    save_list_to_file(verbs_hyphenated, 'Глаголы с дефисом.txt',
                      encoding='cp1251')
    print(f'Создан документ: Глаголы с дефисом.txt')
    print(f'... сортировка ...')

    sorting_by_case = {
        'И': 1,
        'Р': 2,
        'Д': 3,
        'В': 4,
        'Т': 5,
        'Т1': 6,
        'Т2': 7,
        'Т3': 8,
        'П': 9,
    }

    sorting_by_gender = {
        'м': 1,
        'м1': 2,
        'м2': 3,
        'м3': 4,
        'ж': 5,
        'ж1': 6,
        'ж2': 7,
        'ж3': 8,
        'с': 9,
        'с1': 10,
        'с2': 11,
        'с3': 12,
        'мн': 13,
        'мн1': 14,
        'мн2': 15,
        'мн3': 16,
    }

    gi_idf = set()  # .ГИ
    gnb_idf = set()  # .ГНБ
    gp_idf = set()  # .ГП
    gpv_idf = set()  # .ГПв
    gs_idf = set()  # .ГС

    pndm_idf = set()  # .ПНДм
    pndz_idf = set()  # .ПНДж
    pnds_idf = set()  # .ПНДс
    pndmn_idf = set()  # .ПНДмн

    pndk_idf = set()  # .ПНДК

    pnd1m_idf = set()  # .ПНД1м
    pnd1z_idf = set()  # .ПНД1ж
    pnd1s_idf = set()  # .ПНД1с
    pnd1mn_idf = set()  # .ПНД1мн

    pnd2m_idf = set()  # .ПНД2м
    pnd2z_idf = set()  # .ПНД2ж
    pnd2s_idf = set()  # .ПНД2с
    pnd2mn_idf = set()  # .ПНД2мн

    pnsm_idf = set()  # .ПНСм
    pnsz_idf = set()  # .ПНСж
    pnss_idf = set()  # .ПНСс
    pnsmn_idf = set()  # .ПНСмн

    pnsk_idf = set()  # .ПНСКм

    pns1m_idf = set()  # .ПНС1м
    pns1z_idf = set()  # .ПНС1ж
    pns1s_idf = set()  # .ПНС1с
    pns1mn_idf = set()  # .ПНС1мн

    pns2m_idf = set()  # .ПНС2м
    pns2z_idf = set()  # .ПНС2ж
    pns2s_idf = set()  # .ПНС2с
    pns2mn_idf = set()  # .ПНС2мн

    ppdm_idf = set()  # .ППДм
    ppdz_idf = set()  # .ППДж
    ppds_idf = set()  # .ППДс
    ppdmn_idf = set()  # .ППДмн

    ppd1m_idf = set()  # .ППД1м
    ppd1z_idf = set()  # .ППД1ж
    ppd1s_idf = set()  # .ППД1с
    ppd1mn_idf = set()  # .ППД1мн

    ppd2m_idf = set()  # .ППД2м
    ppd2z_idf = set()  # .ППД2ж
    ppd2s_idf = set()  # .ППД2с
    ppd2mn_idf = set()  # .ППД2мн

    ppsm_idf = set()  # .ППСм
    ppsz_idf = set()  # .ППСж
    ppss_idf = set()  # .ППСс
    ppsmn_idf = set()  # .ППСмн

    pps1m_idf = set()  # .ППС1м
    pps1z_idf = set()  # .ППС1ж
    pps1s_idf = set()  # .ППС1с
    pps1mn_idf = set()  # .ППС1мн

    pps2m_idf = set()  # .ППС2м
    pps2z_idf = set()  # .ППС2ж
    pps2s_idf = set()  # .ППС2с
    pps2mn_idf = set()  # .ППС2мн

    ppsk_idf = set()  # .ППСКм

    dn_idf = set()  # .ДН
    dp_idf = set()  # .ДП

    identifiers = []

    for group in word_forms_bases:
        if str(group.title_word_form) in verbs_hyphenated:
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier.startswith('.ГИ'):
                    gi_idf.add(identifier)
                elif identifier.startswith('.ГНБ'):
                    gnb_idf.add(identifier)
                elif identifier.startswith('.ГПв'):
                    gpv_idf.add(identifier)
                elif identifier.startswith('.ГС'):
                    gs_idf.add(identifier)

                elif (identifier.startswith('.ПНД1м')
                      and not identifier.startswith('.ПНД1мн')):
                    pnd1m_idf.add(identifier)
                elif identifier.startswith('.ПНД1ж'):
                    pnd1z_idf.add(identifier)
                elif identifier.startswith('.ПНД1с'):
                    pnd1s_idf.add(identifier)
                elif identifier.startswith('.ПНД1мн'):
                    pnd1mn_idf.add(identifier)

                elif (identifier.startswith('.ПНД2м')
                      and not identifier.startswith('.ПНД2мн')):
                    pnd2m_idf.add(identifier)
                elif identifier.startswith('.ПНД2ж'):
                    pnd2z_idf.add(identifier)
                elif identifier.startswith('.ПНД2с'):
                    pnd2s_idf.add(identifier)
                elif identifier.startswith('.ПНД2мн'):
                    pnd2mn_idf.add(identifier)

                elif identifier.startswith('.ПНДК'):
                    pndk_idf.add(identifier)

                elif (identifier.startswith('.ПНДм')
                      and not identifier.startswith('.ПНДмн')):
                    pndm_idf.add(identifier)
                elif identifier.startswith('.ПНДж'):
                    pndz_idf.add(identifier)
                elif identifier.startswith('.ПНДс'):
                    pnds_idf.add(identifier)
                elif identifier.startswith('.ПНДмн'):
                    pndmn_idf.add(identifier)

                elif (identifier.startswith('.ПНС1м')
                      and not identifier.startswith('.ПНС1мн')):
                    pns1m_idf.add(identifier)
                elif identifier.startswith('.ПНС1ж'):
                    pns1z_idf.add(identifier)
                elif identifier.startswith('.ПНС1с'):
                    pns1s_idf.add(identifier)
                elif identifier.startswith('.ПНС1мн'):
                    pns1mn_idf.add(identifier)

                elif (identifier.startswith('.ПНС2м')
                      and not identifier.startswith('.ПНС2мн')):
                    pns2m_idf.add(identifier)
                elif identifier.startswith('.ПНС2ж'):
                    pns2z_idf.add(identifier)
                elif identifier.startswith('.ПНС2с'):
                    pns2s_idf.add(identifier)
                elif identifier.startswith('.ПНС2мн'):
                    pns2mn_idf.add(identifier)

                elif identifier.startswith('.ПНСК'):
                    pnsk_idf.add(identifier)

                elif (identifier.startswith('.ПНСм')
                      and not identifier.startswith('.ПНСмн')):
                    pnsm_idf.add(identifier)
                elif identifier.startswith('.ПНСж'):
                    pnsz_idf.add(identifier)
                elif identifier.startswith('.ПНСс'):
                    pnss_idf.add(identifier)
                elif identifier.startswith('.ПНСмн'):
                    pnsmn_idf.add(identifier)

                elif (identifier.startswith('.ППД1м')
                      and not identifier.startswith('.ППД1мн')):
                    ppd1m_idf.add(identifier)
                elif identifier.startswith('.ППД1ж'):
                    ppd1z_idf.add(identifier)
                elif identifier.startswith('.ППД1с'):
                    ppd1s_idf.add(identifier)
                elif identifier.startswith('.ППД1мн'):
                    ppd1mn_idf.add(identifier)

                elif (identifier.startswith('.ППД2м')
                      and not identifier.startswith('.ППД2мн')):
                    ppd2m_idf.add(identifier)
                elif identifier.startswith('.ППД2ж'):
                    ppd2z_idf.add(identifier)
                elif identifier.startswith('.ППД2с'):
                    ppd2s_idf.add(identifier)
                elif identifier.startswith('.ППД2мн'):
                    ppd2mn_idf.add(identifier)

                elif (identifier.startswith('.ППДм')
                      and not identifier.startswith('.ППДмн')):
                    ppdm_idf.add(identifier)
                elif identifier.startswith('.ППДж'):
                    ppdz_idf.add(identifier)
                elif identifier.startswith('.ППДс'):
                    ppds_idf.add(identifier)
                elif identifier.startswith('.ППДмн'):
                    ppdmn_idf.add(identifier)

                elif (identifier.startswith('.ППС1м')
                      and not identifier.startswith('.ППС1мн')):
                    pps1m_idf.add(identifier)
                elif identifier.startswith('.ППС1ж'):
                    pps1z_idf.add(identifier)
                elif identifier.startswith('.ППС1с'):
                    pps1s_idf.add(identifier)
                elif identifier.startswith('.ППС1мн'):
                    pps1mn_idf.add(identifier)

                elif (identifier.startswith('.ППС2м')
                      and not identifier.startswith('.ППС2мн')):
                    pps2m_idf.add(identifier)
                elif identifier.startswith('.ППС2ж'):
                    pps2z_idf.add(identifier)
                elif identifier.startswith('.ППС2с'):
                    pps2s_idf.add(identifier)
                elif identifier.startswith('.ППС2мн'):
                    pps2mn_idf.add(identifier)

                elif identifier.startswith('.ППСК'):
                    ppsk_idf.add(identifier)

                elif (identifier.startswith('.ППСм')
                      and not identifier.startswith('.ППСмн')):
                    ppsm_idf.add(identifier)
                elif identifier.startswith('.ППСж'):
                    ppsz_idf.add(identifier)
                elif identifier.startswith('.ППСс'):
                    ppss_idf.add(identifier)
                elif identifier.startswith('.ППСмн'):
                    ppsmn_idf.add(identifier)

                elif identifier.startswith('.ДН'):
                    dn_idf.add(identifier)
                elif identifier.startswith('.ДП'):
                    dp_idf.add(identifier)

                elif identifier.startswith('.ГП'):
                    gp_idf.add(identifier)

    identifiers += sorted(list(gi_idf))
    identifiers += sorted(list(gnb_idf))
    identifiers += sorted(list(gp_idf),
                          key=lambda x: sorting_by_gender[x.split('-')[0][3:]])
    identifiers += sorted(list(gpv_idf))
    identifiers += sorted(list(gs_idf))

    identifiers += sorted(list(pndm_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pndz_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pnds_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pndmn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])

    identifiers += sorted(list(pndk_idf),
                          key=lambda x: sorting_by_gender[x.split('-')[0][5:]])

    identifiers += sorted(list(pnd1m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd1z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd1s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd1mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(pnd2m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd2z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd2s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pnd2mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(pnsm_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pnsz_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pnss_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(pnsmn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])

    identifiers += sorted(list(pnsk_idf),
                          key=lambda x: sorting_by_gender[x.split('-')[0][5:]])

    identifiers += sorted(list(pns1m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns1z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns1s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns1mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(pns2m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns2z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns2s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pns2mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(ppdm_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppdz_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppds_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppdmn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])

    identifiers += sorted(list(ppd1m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd1z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd1s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd1mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(ppd2m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd2z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd2s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(ppd2mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(ppsm_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppsz_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppss_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][5:]])
    identifiers += sorted(list(ppsmn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])

    identifiers += sorted(list(pps1m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps1z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps1s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps1mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(pps2m_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps2z_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps2s_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][6:]])
    identifiers += sorted(list(pps2mn_idf),
                          key=lambda x: sorting_by_case[x.split('-')[0][7:]])

    identifiers += sorted(list(ppsk_idf),
                          key=lambda x: sorting_by_gender[x.split('-')[0][5:]])

    identifiers += sorted(list(dn_idf))
    identifiers += sorted(list(dp_idf))

    return identifiers


# Поиск глаголов с определённым элементом спец. информации (ЭСИ)
# или определённым сочетанием нескольких ЭСИ.
# Напр.
# Глаголы сов пер б НБII1- П1- Пв2-.txt
# Глаголы нес пер НБII3ч П1 Пв2! С ПНД1 ПНС2 ППД1в ППС2 ДН1 ДП1.txt
# *  Прочие примеры - см. ниже, под таблицей.
def get_verbs_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Г ,
    и в спец. информации указан искомый ЭСИ или искомое сочетание ЭСИ.
    Этот ЭСИ или это сочетание ЭСИ вставляется в название документа
    после Глаголы
    При этом происходит замена следующих символов:
        * заменяется на ^ ,
        | на ] ,
        / на [ .
    Примечание. ЭСИ могут быть 13 видов:
        1. указатель вида;
        2. указатель переходности;
        3. индикатор безличности;
        4. шаблон настоящего / будущего времени;
        5. шаблон прошедшего времени;
        6. шаблон повелительного наклонения;
        7. шаблон формы совместного действия;
        8. шаблон причастия настоящего времени действительного;
        9. шаблон причастия настоящего времени страдательного;
        10. шаблон причастия прошедшего времени действительного;
        11. шаблон причастия прошедшего времени страдательного;
        12. шаблон деепричастия настоящего времени;
        13. шаблон деепричастия прошедшего времени.
        """

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.Г')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms
