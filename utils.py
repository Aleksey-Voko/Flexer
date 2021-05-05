import csv
from pathlib import Path


def get_string_list_from_file(f_name, encoding='utf-8'):
    with open(Path(f_name), encoding=encoding) as f_in:
        for line in f_in:
            yield line.rstrip()


def get_dicts_from_csv_file(f_name, encoding='utf-8',
                            newline='', delimiter=','):
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def save_bs_dicts_to_txt(in_dicts: list, f_name, encoding='cp1251'):
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(f_name), 'w', encoding=encoding) as f_out:
        f_out.write('\n\n'.join(str(x) for x in in_dicts) + '\n')
