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


# Прилагательные. Идентификаторы.txt
def get_adjectives_identifiers(word_forms_bases, _) -> list:
    """
    1. Создать документ Прил-ные с дефисом. Изм. обе части.txt .
    2. Найти в БС группы с ЗС, идентификатор которых содержит .П
        (кроме ЗС из документа Прил-ные с дефисом. Изм. обе части.txt).
    3. Создать документ Прилагательные. Идентификаторы.txt
        и вставить в него все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала с учётом формы (сначала идентификаторы полной формы,
        затем краткой формы, затем сравнительной степени,
        затем превосходной степени);
        затем с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем с учётом рода (сначала идентификаторы мужского рода,
        затем женского, затем среднего);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком остальных
        элементов идентификаторов.
    6. Сохранить документ Прилагательные. Идентификаторы.txt .
    """

    # Прил-ные с дефисом. Изм. обе части.txt
    adjectives_hyphenated = get_adjectives_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(adjectives_hyphenated,
                      'Прил-ные с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Прил-ные с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    pmi_idf = set()  # .ПмИ
    pmr_idf = set()  # .ПмР
    pmd_idf = set()  # .ПмД
    pmv_idf = set()  # .ПмВ
    pmt_idf = set()  # .ПмТ
    pmp_idf = set()  # .ПмП

    pzi_idf = set()  # .ПжИ
    pzr_idf = set()  # .ПжР
    pzd_idf = set()  # .ПжД
    pzv_idf = set()  # .ПжВ
    pzt_idf = set()  # .ПжТ
    pzp_idf = set()  # .ПжП

    psi_idf = set()  # .ПсИ
    psr_idf = set()  # .ПсР
    psd_idf = set()  # .ПсД
    psv_idf = set()  # .ПсВ
    pst_idf = set()  # .ПсТ
    psp_idf = set()  # .ПсП

    pmni_idf = set()  # .ПмнИ
    pmnr_idf = set()  # .ПмнР
    pmnd_idf = set()  # .ПмнД
    pmnv_idf = set()  # .ПмнВ
    pmnt_idf = set()  # .ПмнТ
    pmnp_idf = set()  # .ПмнП

    pkm_idf = set()  # .ПКм
    pkz_idf = set()  # .ПКж
    pks_idf = set()  # .ПКс
    pkmn_idf = set()  # .ПКмн

    ps_idf = set()  # .ПС

    ppmi_idf = set()  # .ППмИ
    ppmr_idf = set()  # .ППмР
    ppmd_idf = set()  # .ППмД
    ppmv_idf = set()  # .ППмВ
    ppmt_idf = set()  # .ППмТ
    ppmp_idf = set()  # .ППмП

    ppzi_idf = set()  # .ППжИ
    ppzr_idf = set()  # .ППжР
    ppzd_idf = set()  # .ППжД
    ppzv_idf = set()  # .ППжВ
    ppzt_idf = set()  # .ППжТ
    ppzp_idf = set()  # .ППжП

    ppsi_idf = set()  # .ППсИ
    ppsr_idf = set()  # .ППсР
    ppsd_idf = set()  # .ППсД
    ppsv_idf = set()  # .ППсВ
    ppst_idf = set()  # .ППсТ
    ppsp_idf = set()  # .ППсП

    ppmni_idf = set()  # .ППмнИ
    ppmnr_idf = set()  # .ППмнР
    ppmnd_idf = set()  # .ППмнД
    ppmnv_idf = set()  # .ППмнВ
    ppmnt_idf = set()  # .ППмнТ
    ppmnp_idf = set()  # .ППмнП

    identifiers = []

    for group in word_forms_bases:
        if (str(group.title_word_form) not in adjectives_hyphenated
                and group.title_word_form.idf.startswith('.П')):
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                # полная форма
                if identifier[2] not in ('К', 'С', 'П'):
                    if not identifier.find('мн') > 0:
                        if identifier.startswith('.ПмИ'):
                            pmi_idf.add(identifier)
                        elif identifier.startswith('.ПмР'):
                            pmr_idf.add(identifier)
                        elif identifier.startswith('.ПмД'):
                            pmd_idf.add(identifier)
                        elif identifier.startswith('.ПмВ'):
                            pmv_idf.add(identifier)
                        elif identifier.startswith('.ПмТ'):
                            pmt_idf.add(identifier)
                        elif identifier.startswith('.ПмП'):
                            pmp_idf.add(identifier)

                        elif identifier.startswith('.ПжИ'):
                            pzi_idf.add(identifier)
                        elif identifier.startswith('.ПжР'):
                            pzr_idf.add(identifier)
                        elif identifier.startswith('.ПжД'):
                            pzd_idf.add(identifier)
                        elif identifier.startswith('.ПжВ'):
                            pzv_idf.add(identifier)
                        elif identifier.startswith('.ПжТ'):
                            pzt_idf.add(identifier)
                        elif identifier.startswith('.ПжП'):
                            pzp_idf.add(identifier)

                        elif identifier.startswith('.ПсИ'):
                            psi_idf.add(identifier)
                        elif identifier.startswith('.ПсР'):
                            psr_idf.add(identifier)
                        elif identifier.startswith('.ПсД'):
                            psd_idf.add(identifier)
                        elif identifier.startswith('.ПсВ'):
                            psv_idf.add(identifier)
                        elif identifier.startswith('.ПсТ'):
                            pst_idf.add(identifier)
                        elif identifier.startswith('.ПсП'):
                            psp_idf.add(identifier)
                    else:
                        if identifier.startswith('.ПмнИ'):
                            pmni_idf.add(identifier)
                        elif identifier.startswith('.ПмнР'):
                            pmnr_idf.add(identifier)
                        elif identifier.startswith('.ПмнД'):
                            pmnd_idf.add(identifier)
                        elif identifier.startswith('.ПмнВ'):
                            pmnv_idf.add(identifier)
                        elif identifier.startswith('.ПмнТ'):
                            pmnt_idf.add(identifier)
                        elif identifier.startswith('.ПмнП'):
                            pmnp_idf.add(identifier)

                # краткая форма
                elif identifier[2] == 'К':
                    if not identifier.find('мн') > 0:
                        if identifier.startswith('.ПКм'):
                            pkm_idf.add(identifier)
                        elif identifier.startswith('.ПКж'):
                            pkz_idf.add(identifier)
                        elif identifier.startswith('.ПКс'):
                            pks_idf.add(identifier)
                    elif identifier.startswith('.ПКмн'):
                        pkmn_idf.add(identifier)

                # сравинтельная степень
                elif identifier[2] == 'С':
                    ps_idf.add(identifier)

                # превосходная степень
                elif identifier[2] == 'П':
                    if not identifier.find('мн') > 0:
                        if identifier.startswith('.ППмИ'):
                            ppmi_idf.add(identifier)
                        elif identifier.startswith('.ППмР'):
                            ppmr_idf.add(identifier)
                        elif identifier.startswith('.ППмД'):
                            ppmd_idf.add(identifier)
                        elif identifier.startswith('.ППмВ'):
                            ppmv_idf.add(identifier)
                        elif identifier.startswith('.ППмТ'):
                            ppmt_idf.add(identifier)
                        elif identifier.startswith('.ППмП'):
                            ppmp_idf.add(identifier)

                        elif identifier.startswith('.ППжИ'):
                            ppzi_idf.add(identifier)
                        elif identifier.startswith('.ППжР'):
                            ppzr_idf.add(identifier)
                        elif identifier.startswith('.ППжД'):
                            ppzd_idf.add(identifier)
                        elif identifier.startswith('.ППжВ'):
                            ppzv_idf.add(identifier)
                        elif identifier.startswith('.ППжТ'):
                            ppzt_idf.add(identifier)
                        elif identifier.startswith('.ППжП'):
                            ppzp_idf.add(identifier)

                        elif identifier.startswith('.ППсИ'):
                            ppsi_idf.add(identifier)
                        elif identifier.startswith('.ППсР'):
                            ppsr_idf.add(identifier)
                        elif identifier.startswith('.ППсД'):
                            ppsd_idf.add(identifier)
                        elif identifier.startswith('.ППсВ'):
                            ppsv_idf.add(identifier)
                        elif identifier.startswith('.ППсТ'):
                            ppst_idf.add(identifier)
                        elif identifier.startswith('.ППсП'):
                            ppsp_idf.add(identifier)
                    else:
                        if identifier.startswith('.ППмнИ'):
                            ppmni_idf.add(identifier)
                        elif identifier.startswith('.ППмнР'):
                            ppmnr_idf.add(identifier)
                        elif identifier.startswith('.ППмнД'):
                            ppmnd_idf.add(identifier)
                        elif identifier.startswith('.ППмнВ'):
                            ppmnv_idf.add(identifier)
                        elif identifier.startswith('.ППмнТ'):
                            ppmnt_idf.add(identifier)
                        elif identifier.startswith('.ППмнП'):
                            ppmnp_idf.add(identifier)

    identifiers += sorted(list(pmi_idf))
    identifiers += sorted(list(pmr_idf))
    identifiers += sorted(list(pmd_idf))
    identifiers += sorted(list(pmv_idf))
    identifiers += sorted(list(pmt_idf))
    identifiers += sorted(list(pmp_idf))

    identifiers += sorted(list(pzi_idf))
    identifiers += sorted(list(pzr_idf))
    identifiers += sorted(list(pzd_idf))
    identifiers += sorted(list(pzv_idf))
    identifiers += sorted(list(pzt_idf))
    identifiers += sorted(list(pzp_idf))

    identifiers += sorted(list(pzi_idf))
    identifiers += sorted(list(psr_idf))
    identifiers += sorted(list(psd_idf))
    identifiers += sorted(list(psv_idf))
    identifiers += sorted(list(pst_idf))
    identifiers += sorted(list(psp_idf))

    identifiers += sorted(list(pmni_idf))
    identifiers += sorted(list(pmnr_idf))
    identifiers += sorted(list(pmnd_idf))
    identifiers += sorted(list(pmnv_idf))
    identifiers += sorted(list(pmnt_idf))
    identifiers += sorted(list(pmnp_idf))

    identifiers += sorted(list(pkm_idf))
    identifiers += sorted(list(pkz_idf))
    identifiers += sorted(list(pks_idf))
    identifiers += sorted(list(pkmn_idf))

    identifiers += sorted(list(ps_idf))

    identifiers += sorted(list(ppmi_idf))
    identifiers += sorted(list(ppmr_idf))
    identifiers += sorted(list(ppmd_idf))
    identifiers += sorted(list(ppmv_idf))
    identifiers += sorted(list(ppmt_idf))
    identifiers += sorted(list(ppmp_idf))

    identifiers += sorted(list(ppzi_idf))
    identifiers += sorted(list(ppzr_idf))
    identifiers += sorted(list(ppzd_idf))
    identifiers += sorted(list(ppzv_idf))
    identifiers += sorted(list(ppzt_idf))
    identifiers += sorted(list(ppzp_idf))

    identifiers += sorted(list(ppzi_idf))
    identifiers += sorted(list(ppsr_idf))
    identifiers += sorted(list(ppsd_idf))
    identifiers += sorted(list(ppsv_idf))
    identifiers += sorted(list(ppst_idf))
    identifiers += sorted(list(ppsp_idf))

    identifiers += sorted(list(ppmni_idf))
    identifiers += sorted(list(ppmnr_idf))
    identifiers += sorted(list(ppmnd_idf))
    identifiers += sorted(list(ppmnv_idf))
    identifiers += sorted(list(ppmnt_idf))
    identifiers += sorted(list(ppmnp_idf))

    return identifiers


# Прил-ные с дефисом. Изм. обе части. Идентификаторы.txt
def get_adjectives_ch_both_parts_identifiers(word_forms_bases, _) -> list:
    """1. Создать документ Прил-ные с дефисом. Изм. обе части.txt .
    2. Найти в БС группы с ЗС из документа
        Прил-ные с дефисом. Изм. обе части.txt .
    3. Создать документ Прилагательные. Идентификаторы.txt
        и вставить в него все идентификаторы из найденных согласно п. 2 групп.
    4. Удалить повторы одинаковых идентификаторов, оставив только уникальные.
    5. Упорядочить идентификаторы следующим образом:
        сначала с учётом числа (сначала идентификаторы единственного числа,
        затем - множественного);
        затем учитывая порядок падежей: И Р Д В Т П ;
        затем - в соответствии с алфавитным порядком
        остальных элементов идентификаторов.
    6. Сохранить документ Прилагательные. Идентификаторы.txt ."""

    # Прил-ные с дефисом. Изм. обе части.txt
    adjectives_hyphenated = get_adjectives_hyphenated_ch_both_parts(
        word_forms_bases, _)
    save_list_to_file(adjectives_hyphenated,
                      'Прил-ные с дефисом. Изм. обе части.txt',
                      encoding='cp1251')
    print(f'Создан документ: Прил-ные с дефисом. Изм. обе части.txt')
    print(f'... сортировка ...')

    pmi_idf = set()  # .ПмИ
    pmr_idf = set()  # .ПмР
    pmd_idf = set()  # .ПмД
    pmv_idf = set()  # .ПмВ
    pmt_idf = set()  # .ПмТ
    pmp_idf = set()  # .ПмП

    pzi_idf = set()  # .ПжИ
    pzr_idf = set()  # .ПжР
    pzd_idf = set()  # .ПжД
    pzv_idf = set()  # .ПжВ
    pzt_idf = set()  # .ПжТ
    pzp_idf = set()  # .ПжП

    psi_idf = set()  # .ПсИ
    psr_idf = set()  # .ПсР
    psd_idf = set()  # .ПсД
    psv_idf = set()  # .ПсВ
    pst_idf = set()  # .ПсТ
    psp_idf = set()  # .ПсП

    pmni_idf = set()  # .ПмнИ
    pmnr_idf = set()  # .ПмнР
    pmnd_idf = set()  # .ПмнД
    pmnv_idf = set()  # .ПмнВ
    pmnt_idf = set()  # .ПмнТ
    pmnp_idf = set()  # .ПмнП

    identifiers = []

    for group in word_forms_bases:
        if str(group.title_word_form) in adjectives_hyphenated:
            forms = [group.title_word_form] + group.word_forms
            idfs = [x.idf for x in forms]

            for identifier in idfs:
                if identifier.startswith('.ПмИ'):
                    pmi_idf.add(identifier)
                elif identifier.startswith('.ПмР'):
                    pmr_idf.add(identifier)
                elif identifier.startswith('.ПмД'):
                    pmd_idf.add(identifier)
                elif identifier.startswith('.ПмВ'):
                    pmv_idf.add(identifier)
                elif identifier.startswith('.ПмТ'):
                    pmt_idf.add(identifier)
                elif identifier.startswith('.ПмП'):
                    pmp_idf.add(identifier)

                elif identifier.startswith('.ПжИ'):
                    pzi_idf.add(identifier)
                elif identifier.startswith('.ПжР'):
                    pzr_idf.add(identifier)
                elif identifier.startswith('.ПжД'):
                    pzd_idf.add(identifier)
                elif identifier.startswith('.ПжВ'):
                    pzv_idf.add(identifier)
                elif identifier.startswith('.ПжТ'):
                    pzt_idf.add(identifier)
                elif identifier.startswith('.ПжП'):
                    pzp_idf.add(identifier)

                elif identifier.startswith('.ПсИ'):
                    psi_idf.add(identifier)
                elif identifier.startswith('.ПсР'):
                    psr_idf.add(identifier)
                elif identifier.startswith('.ПсД'):
                    psd_idf.add(identifier)
                elif identifier.startswith('.ПсВ'):
                    psv_idf.add(identifier)
                elif identifier.startswith('.ПсТ'):
                    pst_idf.add(identifier)
                elif identifier.startswith('.ПсП'):
                    psp_idf.add(identifier)

                elif identifier.startswith('.ПмнИ'):
                    pmni_idf.add(identifier)
                elif identifier.startswith('.ПмнР'):
                    pmnr_idf.add(identifier)
                elif identifier.startswith('.ПмнД'):
                    pmnd_idf.add(identifier)
                elif identifier.startswith('.ПмнВ'):
                    pmnv_idf.add(identifier)
                elif identifier.startswith('.ПмнТ'):
                    pmnt_idf.add(identifier)
                elif identifier.startswith('.ПмнП'):
                    pmnp_idf.add(identifier)

    identifiers += sorted(list(pmi_idf))
    identifiers += sorted(list(pmr_idf))
    identifiers += sorted(list(pmd_idf))
    identifiers += sorted(list(pmv_idf))
    identifiers += sorted(list(pmt_idf))
    identifiers += sorted(list(pmp_idf))

    identifiers += sorted(list(pzi_idf))
    identifiers += sorted(list(pzr_idf))
    identifiers += sorted(list(pzd_idf))
    identifiers += sorted(list(pzv_idf))
    identifiers += sorted(list(pzt_idf))
    identifiers += sorted(list(pzp_idf))

    identifiers += sorted(list(psi_idf))
    identifiers += sorted(list(psr_idf))
    identifiers += sorted(list(psd_idf))
    identifiers += sorted(list(psv_idf))
    identifiers += sorted(list(pst_idf))
    identifiers += sorted(list(psp_idf))

    identifiers += sorted(list(pmni_idf))
    identifiers += sorted(list(pmnr_idf))
    identifiers += sorted(list(pmnd_idf))
    identifiers += sorted(list(pmnv_idf))
    identifiers += sorted(list(pmnt_idf))
    identifiers += sorted(list(pmnp_idf))

    return identifiers


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
