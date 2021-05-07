from pathlib import Path
from pprint import pprint

from utils import get_string_list_from_file, read_src_bs, save_bs_dicts_to_txt


def add_groups_to_bs():
    definitions = 'definitionsMixer.txt'

    print('*' * 3)
    print('Настройки:')
    print(f'"{definitions}"\n')
    in_bs, *add_groups_list, out_bs = get_string_list_from_file(
        definitions, encoding='cp1251')
    add_groups_list = add_groups_list[1:-1]

    print('*' * 3)
    print('База словоформ:')
    print(f'"{in_bs}"\n')
    word_forms_bases = list(read_src_bs(in_bs))

    print('Файлы с группами:')
    pprint(add_groups_list)
    print()

    count = 0

    print('... сортировка ...\n')

    for add_groups in add_groups_list:
        verbs = list(read_src_bs(add_groups))
        word_forms_bases += verbs
        count += len(verbs)

    save_bs_dicts_to_txt(sorted(word_forms_bases), out_bs)

    print('*' * 3)
    print(f'В БС добавлено {count} групп словоформ\n')

    print('*' * 3)
    print(f'Файл с результатами "{out_bs}" сохранён в текущей директории:')
    print(Path().resolve())
    print()

    print('*' * 3)
    print('Для выхода нажмите любую Enter')
    input()


if __name__ == '__main__':
    add_groups_to_bs()

# compilation
# pyinstaller -F mixer/Mixer.py
