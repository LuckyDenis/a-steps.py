# coding: utf8


class ConfigFileIsNotRead(Exception):
    def __str__(self, *args, **kwargs):
        return (
            'The `ConfigReader` did not have any configuration '
            'data, use a call to the `read` method'
        )
