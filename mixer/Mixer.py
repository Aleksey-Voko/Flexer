from pathlib import Path

from utils import get_string_list_from_file, read_src_bs, save_bs_dicts_to_txt


def add_groups_to_bs():
    definitions = 'definitions.txt'

    print('*' * 3)
    print('Настройки:')
    print(f'"{definitions}"\n')
    in_bs, add_groups, out_bs = get_string_list_from_file(
        definitions, encoding='cp1251')

    print('*' * 3)
    print('База словоформ:')
    print(f'"{in_bs}"\n')
    word_forms_bases = list(read_src_bs(in_bs))

    print('Группы:')
    print(f'"{add_groups}"\n')
    verbs = list(read_src_bs(add_groups))

    print('... сортировка ...\n')
    word_forms_bases += verbs
    save_bs_dicts_to_txt(sorted(word_forms_bases), out_bs)

    print('*' * 3)
    print(f'В БС добавлено {len(verbs)} групп словоформ\n')

    print('*' * 3)
    print(f'Файл с результатами "{out_bs}" сохранён в текущей директории:')
    print(Path().resolve())
    print()

    print('*' * 3)
    print('Для выхода нажмите любую клавишу')
    input()


if __name__ == '__main__':
    add_groups_to_bs()

# compilation
# pyinstaller -F mixer/Mixer.py
