# coding: utf8
import jinja2
import aiohttp_jinja2


def setup_jinja2(jinja2_variables, app):
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader(
            package_name=jinja2_variables['JINJA2_PACKAGE_NAME'],
            package_path=jinja2_variables['JINJA2_PACKAGE_PATH'],
            encoding=jinja2_variables["JINJA2_ENCODING"]
        )
    )
