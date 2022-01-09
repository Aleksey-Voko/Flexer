"""Местоимения"""

from pathlib import Path

from bs_lists.picking import sorting_by_case, sorting_by_gender
from utils import save_list_to_file


# Поиск местоимений с определённым шаблоном
# Напр. Местоимения II3ь.txt
def get_pronouns_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в спец. информации указан искомый шаблон.
    Название этого шаблона вставляется в название документа после Местоимения
    """

    idfs = Path(task).stem.split()[-1]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and idfs in group.title_word_form.info
        )
    ]
    return word_forms


# Местоимения.txt
def get_pronouns(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.М')
    ]
    return word_forms


# Местоимения. Нет мн. ч.txt
def get_pronouns_no_plural(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в группе имеется словоформа с идентификатором .МР / .МР-
    (кроме ЗС с шаблонами I3, I4, I7, I7-).
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and not any(map(lambda x: x in group.title_word_form.info,
                                ('I3', 'I4', 'I7', 'I7-')))
                and any(map(lambda x: x in group.idf_list, ('.МР', '.МР-')))
        )
    ]
    return word_forms


# Местоимения. Нет ед. ч.txt
def get_pronouns_no_singular(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в спец. информации указан шаблон I3 / I4 / I7 / I7- .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and any(map(lambda x: x in group.title_word_form.info,
                            ('I3', 'I4', 'I7', 'I7-')))
        )
    ]
    return word_forms


# Местоимения ед. и мн. ч.txt
def get_pronouns_singular_and_plural(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М ,
    и в группе имеются словоформа с идентификатором .МмИ / .МмИ- / .МмИ-МмИ
    и словоформа с идентификатором .МмнИ / .МмнИ- / .МмнИ-МмнИ .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and any(map(lambda x: x in group.idf_list,
                            ('.МмИ', '.МмИ-', '.МмИ-МмИ')))
                and any(map(lambda x: x in group.idf_list,
                            ('.МмнИ', '.МмнИ-', '.МмнИ-МмнИ')))
        )
    ]
    return word_forms


# Местоимения с дефисом.txt
def get_pronouns_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .М,
    и в ЗС имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.М')
                and '-' in group.title_word_form.name
        )
    ]
    return word_forms


# Мест-ния с дефисом. Изм. первая часть.txt
def get_pronouns_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС
    и часть слова до первого дефиса в следующей после строки ЗС строке разные;
    часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[1:]
                        ),
                        [
                            '-'.join(x.name.split('-')[1:])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Мест-ния с дефисом. Изм. последняя часть.txt
def get_pronouns_hyphenated_ch_last_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова после последнего дефиса в строке ЗС и часть слова после
    последнего дефиса в следующей после строки ЗС строке разные;
    часть слова до последнего дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[:-1]
                        ),
                        [
                            '-'.join(x.name.split('-')[:-1])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Мест-ния с дефисом. Изм. обе части.txt
def get_pronouns_hyphenated_ch_both_parts(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .М;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова до первого дефиса
    в следующей после строки ЗС строке разные;
    часть слова после последнего дефиса в строке ЗС
    и часть слова после последнего дефиса в
    следующей после строки ЗС строке разные.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.М')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Местоимения. Идентификаторы.txt
def get_pronouns_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Мест-ния с дефисом. Изм. обе части.txt .
    2. Найти в БС группы с ЗС, идентификатор которых содержит .М
        (кроме ЗС из документа Мест-ния с дефисом. Изм. обе части.txt).
    3. Создать документ Местоимения. Идентификаторы.txt и вставить в него
        все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком остальных элементов
        идентификаторов.
    6. Сохранить документ Местоимения. Идентификаторы.txt .
    """

    # Мест-ния с дефисом. Изм. обе части.txt
    pronouns_hyphenated_ch_both_parts = get_pronouns_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(pronouns_hyphenated_ch_both_parts,
                      'Мест-ния с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Мест-ния с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    m_idf = set()  # .М
    m_gen_idf = set()  # .М(м)(ж)(с)
    m_mn_idf = set()  # .Ммн

    identifiers = []

    for group in word_forms_bases:
        if (str(group.title_word_form) not in pronouns_hyphenated_ch_both_parts
                and group.title_word_form.idf.startswith('.М')):
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier[2:4] == 'мн':
                    m_mn_idf.add(identifier)
                elif identifier[2] in ('м', 'ж', 'с'):
                    m_gen_idf.add(identifier)
                else:
                    m_idf.add(identifier)

    identifiers += sorted(list(m_idf),
                          key=lambda x: (sorting_by_case[x[2]], x))
    identifiers += sorted(list(m_gen_idf),
                          key=lambda x: (
                              sorting_by_gender[x[2]],
                              sorting_by_case[x[3]], x))
    identifiers += sorted(list(m_mn_idf),
                          key=lambda x: (sorting_by_case[x[4]], x))

    return identifiers


# Мест-ния с дефисом. Изм. обе части. Идентификаторы.txt
def get_pronouns_hyphenated_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Мест-ния с дефисом. Изм. обе части.txt .
    2. Найти в БС группы с ЗС из документа
        Мест-ния с дефисом. Изм. обе части.txt .
    3. Создать документ Мест-ния с дефисом. Изм. обе части. Идентификаторы.txt
        и вставить в него все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком
        остальных элементов идентификаторов.
    6. Сохранить документ
        Мест-ния с дефисом. Изм. обе части. Идентификаторы.txt .
    """

    # Мест-ния с дефисом. Изм. обе части.txt
    pronouns_hyphenated_ch_both_parts = get_pronouns_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(pronouns_hyphenated_ch_both_parts,
                      'Мест-ния с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Мест-ния с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    m_idf = set()  # .М
    m_gen_idf = set()  # .М(м)(ж)(с)
    m_mn_idf = set()  # .Ммн

    identifiers = []

    for group in word_forms_bases:
        if (str(group.title_word_form) in pronouns_hyphenated_ch_both_parts
                and group.title_word_form.idf.startswith('.М')):
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier[2:4] == 'мн':
                    m_mn_idf.add(identifier)
                elif identifier[2] in ('м', 'ж', 'с'):
                    m_gen_idf.add(identifier)
                else:
                    m_idf.add(identifier)

    identifiers += sorted(list(m_idf),
                          key=lambda x: (sorting_by_case[x[2]], x))
    identifiers += sorted(list(m_gen_idf),
                          key=lambda x: (
                              sorting_by_gender[x[2]],
                              sorting_by_case[x[3]], x))
    identifiers += sorted(list(m_mn_idf),
                          key=lambda x: (sorting_by_case[x[4]], x))

    return identifiers
