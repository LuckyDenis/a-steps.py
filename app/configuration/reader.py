# coding: utf-8
"""
Читатель для конфигурационного файла.
"""

import os

import yaml

from app.configuration.exception import FileTypeError
from app.configuration.exception import ValueVariableEnvError
from app.configuration.exception import VariableEnvNotFoundError


class ConfigReader:  # pylint: disable=too-few-public-methods
    """
    Отвечает за получение и проверку данных из файла с конфигурациями.

    Тип конфигурационного файла должен быть YAML.
    Прочитанные данные хранятся в `ConfigReader("$CONFIG_PATH").data`
    в формате `dict`.
    """

    def __init__(self):
        config_path = os.environ.get("CONFIG_PATH")
        environment = os.environ.get("ENVIRONMENT")

        self._is_config_path(config_path, environment)
        self._is_environment(config_path, environment)
        self._config_file_is_yaml(config_path, environment)
        self._is_environment(config_path, environment)

        with open(config_path, 'r') as stream_file:
            file = yaml.SafeLoader(stream_file)
        self.data = file.get_data()[environment.lower()]

    @staticmethod
    def _is_config_path(config_path, environment):
        if not config_path:
            raise VariableEnvNotFoundError(
                f"Не указан путь до конфигурационного файла`\n"
                f"\tCONFIG_PATH: {config_path}"
                f"\tENVIRONMENT: {environment}")

    @staticmethod
    def _is_environment(config_path, environment):
        if not environment:
            raise VariableEnvNotFoundError(
                f"Не задан тип рабочего окружения: develop, testing, production\n"
                f"\tCONFIG_PATH: {config_path}"
                f"\tENVIRONMENT: {environment}"
            )

    @staticmethod
    def _config_file_is_yaml(config_path, environment):
        _, extension = os.path.splitext(config_path)
        if extension not in ('.yaml', 'yml'):
            raise FileTypeError(
                f"Конфигурационный файл должен быть типа YAML\n "
                f"\tCONFIG_PATH: {config_path}"
                f"\tCONFIG_TYPE: {extension}"
                f"\tENVIRONMENT: {environment}")

    @staticmethod
    def _environment_is_correct(config_path, environment):
        if environment not in ("develop", "testing", "production"):
            raise ValueVariableEnvError(
                f"Не верный тип рабочего окружения: develop, testing, production\n"
                f"\tCONFIG_PATH: {config_path}"
                f"\tENVIRONMENT: {environment}"
            )
