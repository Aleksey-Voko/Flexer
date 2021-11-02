"""Все прилагательные"""


from collections import OrderedDict
from pathlib import Path

from rem import reminder_nouns
from utils import save_list_of_lists_to_csv_file, save_list_to_file


# Прилагательные.txt
def get_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
    ]
    return word_forms


# Прилагательные одуш.txt
def get_animate_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется индикатор одушевлённости о ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and 'о' in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Нет мн. ч.txt
def get_non_plural_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется индикатор ед. ч. е ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and 'е' in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Нет ед. ч.txt
def get_non_singular_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит мн ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('мн')
    ]
    return word_forms


# Прилагательные. Полная форма ед. и мн. ч.txt
def get_singular_and_plural_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    в спец. информации указан шаблон полной формы,
    название которого не содержит мн ,
    и отсутствует индикатор ед. ч. е ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and not group.title_word_form.info[0].endswith('мн')
           and 'е' not in group.title_word_form.info
    ]
    return word_forms


# Прилагательные. Только м. р.txt
def get_masculine_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит м (но не мн)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('м')
    ]
    return word_forms


# Прилагательные. Только ж. р.txt
def get_feminine_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит ж ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('ж')
    ]
    return word_forms


# Прилагательные. Только с. р.txt
def get_neuter_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит с (но не -с)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('с')
           and not group.title_word_form.info[0].endswith('-с')
    ]
    return word_forms


# Прилагательные. Нет с. р.txt
def get_non_neuter_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит -с ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].endswith('-с')
    ]
    return word_forms


# Притяжательные прилагательные.txt
def get_possessive_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы,
    название которого содержит римскую цифру III
    (кроме шаблонов полной формы IIIф и IIIфм)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].startswith('III')
           and not group.title_word_form.info[0].startswith('IIIф')
    ]
    return word_forms


# Русские фамилии.txt
def get_russian_surnames(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан шаблон полной формы IIIф (но не IIIфм)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and not group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and group.title_word_form.info[0].startswith('IIIф')
           and not group.title_word_form.info[0].startswith('IIIфм')
    ]
    return word_forms


# Адъектированные причастия.txt
def get_adjusted_participles(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и перед ЗС имеется поставленный(-ые) без пробела символ(ы) * / ** ."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and group.title_word_form.name.startswith('*')
    ]
    return word_forms


# Прилагательные. Нет полн. ф.txt
def get_no_full_form_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации отсутствует шаблон полной формы
    (кроме адъектированных причастий, т.е. ЗС,
    перед которыми имеется поставленный(-ые) без пробела символ(ы) * / ** )."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and group.title_word_form.info[0].startswith(('К', 'С', 'П'))
           and not group.title_word_form.name.startswith('*')
    ]
    return word_forms


# Прилагательные. Есть кр. ф.txt
def get_short_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон краткой формы
    (кроме прилагательных с дефисом, у которых изменяются обе части слова,
    т.е. кроме ЗС групп, идентификатор которых содержит .П , а также -П)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and '-П' not in group.title_word_form.idf
           and any(map(
               lambda x: x.startswith('К'),
               group.title_word_form.info
           ))
    ]
    return word_forms


# Прилагательные. Есть срав. ст.txt
def get_comparative_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон сравнительной степени
    (кроме прилагательных с дефисом, у которых изменяются обе части слова,
    т.е. кроме ЗС групп, идентификатор которых содержит .П , а также -П)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and '-П' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith('С'),
            group.title_word_form.info
            ))
    ]
    return word_forms


# Прилагательные. Есть прев. ст.txt
def get_superlative_adjectives(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации имеется шаблон превосходной степени
    (кроме прилагательных с дефисом, у которых изменяются обе части слова,
    т.е. кроме ЗС групп, идентификатор которых содержит .П , а также -П)."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and '-П' not in group.title_word_form.idf
           and any(map(
            lambda x: x.startswith('П'),
            group.title_word_form.info
            ))
    ]
    return word_forms


# Поиск прилагательных с определённым элементом спец. информации /
# определённым сочетанием идущих друг за другом
# элементов спец. информации
# Напр. Прилагательные К2о СII5ч.txt
def get_adjectives_implicit_pattern(word_forms_bases, _, task) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в спец. информации указан искомый элемент / указано искомое сочетание
    идущих друг за другом элементов.                                                                                                                                          Этот элемент спец. информации / сочетание элементов спец. информации вставляется в название документа после Прилагательные
    """

    idfs = Path(task).stem.split()[1:]
    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (
                group.title_word_form.idf.startswith('.П')
                and all(map(lambda x: x in group.title_word_form.info, idfs))
        )
    ]
    return word_forms


# Прилагательные с дефисом.txt
def get_adjectives_hyphenated(word_forms_bases, _) -> list:
    """Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в ЗС имеется хотя бы 1 дефис."""

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and '-' in group.title_word_form.name
    ]
    return word_forms


# Прил-ные с дефисом. Изм. первая часть.txt
def get_adjectives_hyphenated_ch_first_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
        идентификатор ЗС группы содержит .П ;
        в ЗС имеется хотя бы 1 дефис;
        часть слова до первого дефиса в строке ЗС
        и часть слова до первого дефиса в следующей после строки ЗС
        строке разные;
        часть слова после первого дефиса во всех строках группы одинаковая.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.П')
            and '-' in group.title_word_form.name)

            and (
                   group.title_word_form.name.split('-')[0]
                   != group.word_forms[0].name.split('-')[0]
           )

            and all(map(
                lambda x: x == '-'.join(
                    group.title_word_form.name.split('-')[1:]
                ),
                [
                    '-'.join(x.name.split('-')[1:])
                    for x in group.word_forms
                ]
            ))
    ]

    return word_forms


# Прил-ные с дефисом. Изм. последняя часть.txt
def get_adjectives_hyphenated_ch_last_part(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
        идентификатор ЗС группы содержит .П ;
        в ЗС имеется хотя бы 1 дефис;
        часть слова после последнего дефиса в строке ЗС
        и часть слова после последнего дефиса
        в следующей после строки ЗС строке разные;
        часть слова до последнего дефиса во всех строках группы одинаковая.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.П')
            and '-' in group.title_word_form.name)
            and group.title_word_form.name.split('-')[-1]
                != group.word_forms[0].name.split('-')[-1]
           and all(map(
               lambda x: x == '-'.join(
                   group.title_word_form.name.split('-')[:-1]
               ),
               [
                   '-'.join(x.name.split('-')[:-1])
                   for x in group.word_forms
               ]
           ))
    ]

    return word_forms


# Прил-ные с дефисом. Изм. обе части.txt
def get_adjectives_hyphenated_ch_both_parts(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, отвечающих следующим требованиям:
        идентификатор ЗС группы содержит .П ;
        в ЗС имеется хотя бы 1 дефис;

        часть слова до первого дефиса в строке ЗС
        и часть слова до первого дефиса
        в следующей после строки ЗС строке разные;

        часть слова после последнего дефиса в строке ЗС
        и часть слова после последнего дефиса
        в следующей после строки ЗС строке разные.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if (group.title_word_form.idf.startswith('.П')
            and '-' in group.title_word_form.name)

            and group.title_word_form.name.split('-')[0]
                != group.word_forms[0].name.split('-')[0]

           and group.title_word_form.name.split('-')[-1]
           != group.word_forms[0].name.split('-')[-1]
    ]

    return word_forms


# Прилагательные. Несколько дефисов.txt
def get_adjectives_multiple_hyphens(word_forms_bases, _) -> list:
    """
    Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и в ЗС имеется более 1 дефиса.
    """

    word_forms = [
        str(group.title_word_form) for group in word_forms_bases
        if group.title_word_form.idf.startswith('.П')
           and group.title_word_form.name.count('-') > 1
    ]

    return word_forms


# Прилагательные. Сочетания шаблонов.csv
def save_adjectives_pattern_combinations(word_forms_bases, _):
    """Создать документы:
        Прил-ные с дефисом. Изм. первая часть.txt
        и Прил-ные с дефисом. Изм. обе части.txt .

    Найти в БС строки с ЗС групп, идентификатор которых содержит .П ,
    и ЗС отсутствует в документах
        Прил-ные с дефисом. Изм. первая часть.txt
        и Прил-ные с дефисом. Изм. обе части.txt .

    Выбрать из найденных строк строки с уникальным сочетанием
    элементов спец. информации
    (подробнее об элементах спец. информации - см. док-т Структура строки.xlsx,
    вкладка Структура спец. информации).

    Примечание. При наличии нескольких строк с одинаковым
    сочетанием элементов спец. информации выбирать первую (верхнюю) строку,
    т.е. строку, слово в которой идёт первым по алфавиту.

    Создать документ Прилагательные. Сочетания шаблонов.csv .
    Вставить в 7 столбцов этого документа выбранные строки
    (слово - в первый столбец, элементы спец. информации - в другие,
    соответствующие им по типу 6 столбцов),
    располагая строки в соответствии с алфавитным порядком
    элементов спец. информации."""

    # Прил-ные с дефисом. Изм. первая часть.txt
    adjectives_ch_first_part = get_adjectives_hyphenated_ch_first_part(
        word_forms_bases, _)
    save_list_to_file(adjectives_ch_first_part,
                      'Прил-ные с дефисом. Изм. первая часть.txt',
                      encoding='cp1251')
    print(f'Создан документ: Прил-ные с дефисом. Изм. первая часть.txt')
    print(f'... сортировка ...')

    # Прил-ные с дефисом. Изм. обе части.txt
    adjectives_ch_both_parts = get_adjectives_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(adjectives_ch_both_parts,
                      'Прил-ные с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Прил-ные с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    unusual_words = (
            adjectives_ch_first_part
            + adjectives_ch_both_parts
    )

    word_forms = []
    unique_elements = []

    for group in word_forms_bases:
        if (
                group.title_word_form.idf.startswith('.П')
                and str(group.title_word_form) not in unusual_words
        ):
            elements = ' '.join(group.title_word_form.info)
            if elements not in unique_elements:
                unique_elements.append(elements)
                word_forms.append(group.title_word_form)

    in_form_of_list = []

    for form in word_forms:
        indicators = OrderedDict({
            'name': form.name,
            # 'idf': form.idf,
            'I': '',
            'К': '',
            'С': '',
            'П': '',
            'о': '',
            'е': '',
        })

        for indicator in form.info:
            if indicator.startswith('I'):
                indicators['I'] = indicator
            elif indicator.startswith('К'):
                indicators['К'] = indicator
            elif indicator.startswith('С'):
                indicators['С'] = indicator
            elif indicator.startswith('П'):
                indicators['П'] = indicator
            elif indicator == 'о':
                indicators['о'] = indicator
            elif indicator == 'е':
                indicators['е'] = indicator

        in_form_of_list.append(list(indicators.values()))

    in_form_of_list = sorted(
        in_form_of_list,
        key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6])
    )

    head_1 = [
        '',
        'полная\nформа',
        'краткая\nформа',
        'сравнительная\nстепень',
        'превосходная\nстепень',
        'одушевлённость',
        'только\nединственное\nчисло',
    ]

    head_2 = [
        '',
        'НЕ образуется для\nадъектированных причастий и\nГОРАЗД, РАД,\nПОЛНЫМ-ПОЛОН',
        'Новое прилагательное,\nобразующее краткую форму,\nнужно внести в список 12',
        'Новое прилагательное,\nобразующее сравнительную степень,\nнужно внести в список 22',
        'Новое прилагательное,\nобразующее превосходную степень,\nнужно внести в список 27',
        '', '',
    ]

    in_form_of_list = [head_1] + [head_2] + in_form_of_list

    print(f'\n{reminder_nouns}\n')

    save_list_of_lists_to_csv_file(
        in_form_of_list,
        'Прилагательные. Сочетания шаблонов.csv',
        encoding='cp1251',
        delimiter=';'
    )
