"""Файл с инструментами для отработки случаев изменения параметров внешнего конфига."""

import os

from yaml import safe_load


def cut_protocol(domain):
    """
    Функция, обрезающая из домена протокол и возвращающая только хост.

    :param domain: полный домен
    :return: хост без протокола
    """
    if domain != '' and domain.split('://')[0] in ('http', 'https'):
        return domain.split('://')[1]
    return domain


def get_config_from_file(file):
    """
    Функция для получения распасенного конфига из переданного файла.

    :param file: файл конфига
    :return: прочитанный конфиг
    """
    if not os.getenv('PROJECT_MODE'):
        with open('settings.sample.yml', 'r') as ymlfile:
            config = safe_load(ymlfile)
        return config
    if os.path.exists(file):
        with open(file, 'r') as ymlfile:
            config = safe_load(ymlfile)
        return config
    else:
        raise FileNotFoundError('Configuration file not found')
