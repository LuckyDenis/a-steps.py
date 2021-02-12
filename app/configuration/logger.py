# coding: utf8
import logging.config

from typing import Dict, AnyStr


def setup_logging(logging_variables: Dict[AnyStr, AnyStr]):
    logging.config.dictConfig(logging_variables)
