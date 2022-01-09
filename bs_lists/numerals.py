"""Числительные"""

from pathlib import Path

from bs_lists.picking import sorting_by_case, sorting_by_gender
from utils import save_list_to_file


# Поиск числительных с определённым шаблоном
# Напр. Числительные II10.txt
def get_numerals_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч,
    и в спец. информации указан искомый шаблон.
    Название этого шаблона вставляется в название документа после Числительные
    """

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.Ч')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms


# Числительные.txt
def get_numerals(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч .
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.Ч')
    ]
    return word_forms


# Числительные с дефисом.txt
def get_numerals_hyphenated(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .Ч ,
    и в ЗС имеется хотя бы 1 дефис.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.Ч')
                and '-' in group.title_word_form.name
        )
    ]
    return word_forms


# Числ-ные с дефисом. Изм. первая часть.txt
def get_numerals_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .Ч ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова до первого дефиса
    в следующей после строки ЗС строке разные;
    часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Ч')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[1:]),
                        [
                            '-'.join(x.name.split('-')[1:])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Числ-ные с дефисом. Изм. последняя часть.txt
def get_numerals_hyphenated_ch_last_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .Ч ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова после последнего дефиса в строке ЗС и часть слова после
    последнего дефиса в следующей после строки ЗС строке разные;
    часть слова до последнего дефиса во всех строках группы одинаковая.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Ч')
            and '-' in group.title_word_form.name)
    ]

    for group in groups:
        if (
                group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
                and all(
                    map(
                        lambda x: x == '-'.join(
                            group.title_word_form.name.split('-')[:-1]),
                        [
                            '-'.join(x.name.split('-')[:-1])
                            for x in group.word_forms
                        ]
                    )
                )
        ):
            word_forms.append(str(group.title_word_form))

    return word_forms


# Числ-ные с дефисом. Изм. обе части.txt
def get_numerals_hyphenated_ch_both_parts(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
    идентификатор ЗС группы содержит .Ч ;
    в ЗС имеется хотя бы 1 дефис;
    часть слова до первого дефиса в строке ЗС и часть слова до первого дефиса
    в следующей после строки ЗС строке разные;
    часть слова после последнего дефиса в строке ЗС и часть слова после
    последнего дефиса в следующей после строки ЗС строке разные.
    """

    word_forms = []

    groups = [
        group for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.Ч')
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


# Числительные. Идентификаторы.txt
def get_numerals_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Числ-ные с дефисом. Изм. обе части.txt .
    2. Найти в БС группы с ЗС, идентификатор которых содержит .Ч
        (кроме ЗС из документа Числ-ные с дефисом. Изм. обе части.txt).
    3. Создать документ Числительные. Идентификаторы.txt и вставить в него
        все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком
        остальных элементов идентификаторов.
    6. Сохранить документ Числительные. Идентификаторы.txt .
    """

    # Мест-ния с дефисом. Изм. обе части.txt
    numerals_hyphenated_ch_both_parts = get_numerals_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(numerals_hyphenated_ch_both_parts,
                      'Числ-ные с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Числ-ные с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    ch_idf = set()  # .Ч
    ch_gen_idf = set()  # .Ч(м)(ж)(с)
    ch_mn_idf = set()  # .Чмн

    identifiers = []

    for group in word_forms_bases:
        if (str(group.title_word_form) not in numerals_hyphenated_ch_both_parts
                and group.title_word_form.idf.startswith('.Ч')):
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier[2:4] == 'мн':
                    ch_mn_idf.add(identifier)
                elif identifier[2] in ('м', 'ж', 'с'):
                    ch_gen_idf.add(identifier)
                else:
                    ch_idf.add(identifier)

    identifiers += sorted(list(ch_idf),
                          key=lambda x: (sorting_by_case[x[2]], x))
    identifiers += sorted(list(ch_gen_idf),
                          key=lambda x: (
                              sorting_by_gender[x[2]],
                              sorting_by_case[x[3]], x))
    identifiers += sorted(list(ch_mn_idf),
                          key=lambda x: (sorting_by_case[x[4]], x))

    return identifiers
