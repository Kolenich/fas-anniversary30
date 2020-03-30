"""Файл дополнительных утилит общих для проекта."""

import os


def delete_empty_dirs(path: str):
    """
    Функция для рекурсивного удаления всех пустых папок.

    :param path: абсолютный путь до папки, с которой начинать удаление
    """
    # Если переданное значение не является папкой, выходим из функции
    if not os.path.isdir(path):
        return

    children_dirs = [
        os.path.join(path, child_dir) for child_dir in os.listdir(path)
        if os.path.isdir(os.path.join(path, child_dir))
    ]

    if len(children_dirs):
        for child_dir in children_dirs:
            delete_empty_dirs(child_dir)

    # Саму папку media не удаляем
    if not len(os.listdir(path)) and path[-5:] != 'media':
        os.rmdir(path)
