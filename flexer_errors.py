def get_error_message(message):
    return ('В Н И М А Н И Е !\n'
            'Аварийное завершение.\n'
            f'{message}\n'
            'Для выхода нажмите Enter')


class InputDataError(Exception):
    pass
