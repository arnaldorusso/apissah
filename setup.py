#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='https://github.com/arnaldorusso/apissah',
    version='0.1.0',
    description='"Apiçá" is a Tupi-Guarani word meaning "Atention". Apiçá is a regressive clock.',
    long_description=readme + '\n\n' + history,
    author='Arnaldo Russo',
    author_email='arnaldorusso@gmail.com',
    url='https://github.com/arnaldorusso/https://github.com/arnaldorusso/apissah',
    packages=[
        'https://github.com/arnaldorusso/apissah',
    ],
    package_dir={'https://github.com/arnaldorusso/apissah': 'https://github.com/arnaldorusso/apissah'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='https://github.com/arnaldorusso/apissah',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)