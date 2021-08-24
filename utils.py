import csv
import re
from itertools import zip_longest
from pathlib import Path

from socket_base import SocketWordForm, SocketSubGroupWordForm, SocketGroupWordForm
from word_form import TitleWordForm, WordForm, GroupWordForm


def get_string_list_from_file(f_name, encoding='utf-8'):
    with open(Path(f_name), encoding=encoding) as f_in:
        for line in f_in:
            yield line.rstrip()


def save_list_to_file(input_list: list, out_file: str, encoding='utf-8'):
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        for line in input_list:
            f_out.write(str(line) + '\n')


def get_dicts_from_csv_file(f_name, encoding='cp1251',
                            newline='', delimiter=';'):
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def get_long_dicts_from_csv_file(f_name, num_fields=14, encoding='cp1251',
                                 newline='', delimiter=';'):
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.reader(f_in, delimiter=delimiter)
        fieldnames = [
            'name',
            'Inf_0',
            'Inf_1',
            'Inf_2',
            'Inf_3',
            'Inf_4',
            'Inf_5',
            'Inf_6',
            'Inf_7',
            'Inf_8',
            'Inf_9',
            'Inf_10',
            'Inf_11',
            'Inf_12',
        ]
        for row in csv_reader:
            if row[0]:
                yield dict(zip_longest(fieldnames[:num_fields],
                                       row, fillvalue=''))


def save_bs_dicts_to_txt(in_dicts: list, f_name, encoding='cp1251'):
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(f_name), 'w', encoding=encoding) as f_out:
        f_out.write('\n\n'.join(str(x) for x in in_dicts) + '\n')


def get_bs_title_word_form(src_title_word_form):
    if '.*' in src_title_word_form:
        src_title_word_form_w_note, src_note = [
            x.strip() for x in src_title_word_form.split(' .* ')]
        note = ' '.join(['.*', src_note])
    else:
        src_title_word_form_w_note = src_title_word_form
        note = ''
    name, *idf_info, = src_title_word_form_w_note.split()
    if idf_info:
        idf, *info = idf_info
    else:
        idf, *info = '', ''
    return TitleWordForm(name, idf, info, note)


def read_src_bs(f_name: str, encoding='cp1251'):
    with open(f_name, encoding=encoding) as f_in:
        src_group_word_form_list = (
            x.strip() for x in f_in.read().split('\n\n'))

        for src_group_word_form in src_group_word_form_list:
            src_title_word_form, *src_word_forms = src_group_word_form.split('\n')

            title_word_form = get_bs_title_word_form(src_title_word_form)

            # word_forms
            word_forms = []
            for src_word_form in src_word_forms:
                name, *idf_list, = src_word_form.split()
                word_forms.append(WordForm(name, ' '.join(idf_list)))

            # group_word_form
            group_word_form = GroupWordForm(title_word_form, word_forms)

            yield group_word_form


def get_socket_word_form(src_socket_form):
    # spec_note
    if ' < ' in src_socket_form:
        src_socket_form, src_spec_note = [
            x.strip() for x in src_socket_form.split(' < ')
        ]
        spec_note = ' '.join(['<', src_spec_note])
    else:
        spec_note = ''

    # etml_note
    pattern = re.compile(r'^.+ (\*\?|\*\?\?|\*!|\*\*)$')
    result = re.search(pattern, src_socket_form)
    if result:
        etml_note = result.group(1)
        l_res = len(result.group(1))
        src_socket_form = src_socket_form[:-l_res].strip()
    else:
        pattern = re.compile(r'^.+ (\* ?(<=|\|<=) ?.+)$')
        result = re.search(pattern, src_socket_form)
        if result:
            etml_note = result.group(1)
            l_res = len(result.group(1))
            src_socket_form = src_socket_form[:-l_res].strip()
        else:
            etml_note = ''

    # note
    if ' * ' in src_socket_form:
        src_socket_form, src_note = [
            x.strip() for x in src_socket_form.split(' * ')
        ]
        note = ' '.join(['*', src_note])
    else:
        note = ''

    # idf + info
    if ' .' in src_socket_form:
        src_socket_form, src_idf_info = [
            x.strip() for x in src_socket_form.split(' .')
        ]
        idf_info = ''.join(['.', src_idf_info])
        idf, *info, = idf_info.split()
    else:
        idf = ''
        info = []

    # invisible
    if src_socket_form.startswith('* '):
        invisible = '*'
        src_socket_form = src_socket_form[2:]
    else:
        invisible = ''

    # root_index
    pattern = re.compile(r'^.+ (\d(\**|!))$')
    result = re.search(pattern, src_socket_form)
    if result:
        root_index = result.group(1).strip()
        l_res = len(result.group(1))
        # name = src_socket_form[:-l_res].strip()
        name = ' '.join(filter(
            None, [
                invisible,
                src_socket_form[:-l_res].strip()
            ]
        ))
    else:
        root_index = ''
        # name = src_socket_form
        name = ' '.join(filter(
            None,
            [invisible, src_socket_form]
        ))

    return SocketWordForm(invisible, name, root_index, idf, info, note,
                          etml_note, spec_note)


def read_src_socket_bs(f_name: str, encoding='cp1251'):
    """
    Читает БГ.
    :param f_name: имя файла БГ
    :param encoding: encoding f_in
    :return: список объектов SocketGroupWordForm
    """
    with open(f_name, encoding=encoding) as f_in:
        src_socket_group_list = (
            x.strip() for x in f_in.read().split('---')
        )

        for src_socket_group in src_socket_group_list:
            if src_socket_group:
                src_socket_sub_group_list = (
                    x.strip() for x in src_socket_group.split('\n\n')
                )

                socket_group_list = []
                for src_socket_sub_group in src_socket_sub_group_list:
                    socket_word_form_list = []
                    for src_socket_form in src_socket_sub_group.split('\n'):
                        socket_word_form = get_socket_word_form(
                            src_socket_form
                        )
                        socket_word_form_list.append(socket_word_form)

                    socket_sub_group = SocketSubGroupWordForm(
                        socket_word_form_list
                    )
                    socket_group_list.append(socket_sub_group)

                yield SocketGroupWordForm(socket_group_list)
