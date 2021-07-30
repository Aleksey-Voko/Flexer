def get_error_message(message):
    return ('В Н И М А Н И Е !\n'
            'Аварийное завершение.\n'
            'Невозможные данные в строке:\n'
            f'{message}\n'
            'Для продолжения нажмите Enter')


class InputDataError(Exception):
    pass
