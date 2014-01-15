#!/usr/bin/env python

import os
from setuptools import setup

LICENSE = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')).read().strip()

DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.md')).read().strip()

setup(
    name='letexpr',
    version='0.1',
    description='imitation of let expression like a Haskell',
    author='OGURA_Daiki',
    author_email='8hachibee125@gmail.com',
    url='https://github.com/hachibeeDI/letexpr',
    py_modules=['letexpr'],
    keywords=['letexpression', ],
    install_requires=[''],
    license=LICENSE,
    long_description=DESCRIPTION,
    test_suite='')