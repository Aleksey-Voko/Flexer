from pathlib import Path

from bs_lists.spreader import get_filtered_list
from utils import read_src_bs, save_list_to_file, get_string_list_from_file, read_src_socket_bs


def main():
    definitions = 'lists.txt'
    print('Настройки:')
    print(f'{definitions}\n')

    in_bs, in_bg, *out_tasks = [
        x for x in list(
            get_string_list_from_file(definitions, encoding='cp1251')
        ) if x
    ]

    print(f'БС файл: {in_bs}')
    print(f'БГ файл: {in_bg}')
    print()

    print('Создать списки:')
    for task in out_tasks:
        print(task)
    print()

    print(f'... чтение {in_bs} ...')
    word_forms_bases = list(read_src_bs(in_bs))

    print(f'... чтение {in_bg} ...')
    socket_group_list = list(read_src_socket_bs(in_bg))
    print()

    # Выполнение задач
    for task in out_tasks:
        print(f'{"* " * 38}*\n')
        print(f'Список: {task}')

        out_task = get_filtered_list(word_forms_bases, socket_group_list, task)
        if out_task:
            print(f'... сортировка ...')
            save_list_to_file(sorted(out_task), task.replace('*', '+'),
                              encoding='cp1251')
            print(f'Создан документ {task}\n')
            print('Для продолжения нажмите Enter')
            input()
        else:
            print('В Н И М А Н И Е !\nЗадача не определена или список пустой.')
            print('Для выхода нажмите Enter')
            input()

    # End task
    print(f'{"* " * 38}*\n')
    print(f'Результатаы сохранены в текущей директории:')
    print(Path().resolve())
    print()

    print('Для выхода нажмите Enter')
    input()


if __name__ == '__main__':
    main()

# compilation
# pyinstaller -F -i bs_lists/icon.ico bs_lists/BSLists.py
