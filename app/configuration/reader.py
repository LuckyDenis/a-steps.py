# coding: utf-8
"""
Читатль конфигурационного файла.
"""
from typing import AnyStr, NoReturn, Dict, List

import os
import yaml


class ConfigReader:
    """
    Отвечает за получение данных из файла с конфигурациями.

    Тип конфигурационного файла должен быть YAML.
    """

    def __init__(self):
        self.config_path: AnyStr = ""
        self.environment: AnyStr = ""
        self.data: Dict = dict()
        self.database: Dict = dict()
        self.server: Dict = dict()

    @staticmethod
    def _get_environ(environ_name: AnyStr) -> AnyStr:
        return os.environ.get(environ_name)

    def read(self) -> NoReturn:
        self.config_path = self._get_environ("CONFIG_PATH")
        self.environment = self._get_environ("ENVIRONMENT")

        with open(self.config_path, 'r') as stream_file:
            file = yaml.SafeLoader(stream_file).get_data()
        self.data.update(file[self.environment.lower()])

    def _get_section_variables(
            self, section_name: AnyStr, variables_name:
            List[AnyStr], store: Dict[AnyStr, AnyStr]) -> NoReturn:

        for variable_name in variables_name:
            store[variable_name] = self._get_environ(variable_name)

        store.update(self.data[section_name])

    def server_variables(self) -> Dict[AnyStr, AnyStr]:
        section_name = 'server'
        variables_name = ['SERVER_PORT']

        if not self.server:
            self._get_section_variables(
                section_name, variables_name, self.server)
        return self.server

    def database_variables(self) -> Dict[AnyStr, AnyStr]:
        section_name = 'database'
        variables_name = [
            'DATABASE_PASSWORD',
            'DATABASE_USERNAME',
            'DATABASE_PORT',
            'DATABASE_HOST',
            'DATABASE_NAME'
        ]

        if not self.database:
            self._get_section_variables(
                section_name, variables_name, self.database)
        return self.database
