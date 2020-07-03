from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='vertica-parser',
    version='9.2.8',
    description='vertica sql parser',
    author='Alexander Filatov',
    author_email='asfilatov@avito.ru',
    packages=['vertica_parser', 'vertica_catalog'],
    install_requires=required,
)
