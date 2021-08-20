from pathlib import Path

from bs_lists.filtered import get_filtered_list
from utils import read_src_bs, save_list_to_file


def main():
    in_bs = input('Имя файла БС:\n')
    print()

    print(f'... чтение {in_bs} ...\n')
    word_forms_bases = list(read_src_bs(in_bs))

    out_bs = input("Имя списка БС:\n")
    print()

    out_list = get_filtered_list(word_forms_bases, out_bs)

    print('... сортировка ...\n')
    save_list_to_file(sorted(out_list), out_bs, encoding='cp1251')

    print(f'Создан файл {out_bs}\n')
    print(f'Результатаы сохранены в текущей директории:')
    print(Path().resolve())
    print()

    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    main()

# compilation
# pyinstaller -F -i bs_lists/icon.ico bs_lists/BSLists.py
