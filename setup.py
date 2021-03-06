#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Setup module for the Python-based Jenkins Utilities.
#
# March 20202

import platform
from setuptools import setup, find_packages


def get_long_description():
    return open('README.rst').read()


setup(

    name='im-jenkins-utils',
    version='1.3.0',
    author='Alan Christie',
    author_email='achristie@informaticsmatters.com',
    url='https://github.com/InformaticsMatters/jenkins-utils',
    license='Copyright (C) 2020 Informatics Matters Ltd. All rights reserved.',
    description='Utilities for Informatics Matters CI/CD configuration',
    long_description=get_long_description(),
    keywords='jenkins',
    platforms=['any'],

    # Our modules to package
    packages=find_packages(exclude=['*.test', '*.test.*', 'test.*', 'test']),
    py_modules=['im_jenkins_server'],

    # Essential dependencies
    install_requires=[
        'python-jenkins == 1.3.*'
    ],
    # Supported Python versions
    python_requires='>=3, <4',

    # Project classification:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
    ],

    zip_safe=False,

)
