# coding: utf-8
"""
Содержит ошибки для модуля `app.configuration`
"""


class ConfigurationBaseError(Exception):
    """
    Базовый класс для ошибок конфигурации
    """


class VariableEnvNotFoundError(ConfigurationBaseError):
    """
    Переманная окружения не найдена
    """


class FileTypeError(ConfigurationBaseError):
    """
    Неверный тип файла
    """


class ValueVariableEnvError(ConfigurationBaseError):
    """
    Значение переменной не коректно
    """
