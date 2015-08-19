#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages

deps = ['yowsup2==2.3.185', 'yowlayer-store==0.1', 'cleverbot']

setup(
    name='yowlayer-cleverbot',
    version="0.1",
    tests_require=[],
    install_requires = deps,
    dependency_links = [
        'https://github.com/tgalal/yowsup/archive/develop.zip#egg=yowsup2-2.3.185',
        'https://github.com/tgalal/yowlayer-store/archive/master.zip#egg=yowlayer-store-0.1'
    ],
    packages= find_packages(),
    include_package_data=True,
    platforms='any',
    namespace_packages = ['yowsup_ext', 'yowsup_ext.layers'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
