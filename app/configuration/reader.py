# coding: utf-8
import os
from typing import AnyStr, NoReturn, Dict, List

import yaml
from .exceptions import ConfigFileIsNotRead

DEFAULT_ENVIRONMENT = 'develop'


class ConfigReader:
    """
    Отвечает за получение данных из файла с конфигурациями.

    Тип конфигурационного файла должен быть YAML.
    """

    def __init__(self):
        self.config_path: AnyStr = os.path.join(__file__, '/')
        self.environment: AnyStr = DEFAULT_ENVIRONMENT
        self.data: Dict[AnyStr, AnyStr] = dict()
        self.database: Dict[AnyStr, AnyStr] = dict()
        self.server: Dict[AnyStr, AnyStr] = dict()
        self.jinja2: Dict[AnyStr, AnyStr] = dict()
        self.logging: Dict[AnyStr, AnyStr] = dict()

    @staticmethod
    def _get_from_environ(environ_name: AnyStr) -> AnyStr:
        return os.environ.get(environ_name)

    def read(self) -> NoReturn:
        self.config_path = self._get_from_environ("CONFIG_PATH")
        self.environment = self._get_from_environ("ENVIRONMENT")

        with open(self.config_path, 'r') as stream_file:
            file = yaml.SafeLoader(stream_file).get_data()
        self.data.update(file[self.environment.lower()])

    def version(self):
        if not self.data:
            raise ConfigFileIsNotRead()
        return self.data['version']

    def _get_section_variables(
            self, section_name: AnyStr, variables_name:
            List[AnyStr], section_store: Dict[AnyStr, AnyStr]) -> NoReturn:

        if not self.data:
            raise ConfigFileIsNotRead()

        if section_store:
            return

        for name in variables_name:
            section_store[name] = self._get_from_environ(name)

        section_store.update(self.data[section_name])

    def server_variables(self) -> Dict[AnyStr, AnyStr]:
        section_name = 'server'
        variables_name = ['SERVER_PORT']

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

        self._get_section_variables(
            section_name, variables_name, self.database)
        return self.database

    def jinja2_variables(self) -> Dict[AnyStr, AnyStr]:
        section_name = 'jinja2'
        variables_name = []

        self._get_section_variables(
            section_name, variables_name, self.jinja2)
        return self.jinja2

    def logging_variables(self) -> Dict[AnyStr, AnyStr]:
        section_name = 'logging'
        variables_name = []
        self._get_section_variables(
            section_name, variables_name, self.logging
        )
        return self.logging
