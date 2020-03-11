#!/usr/bin/env python
# Copyright 2019 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
import os
from setuptools import setup, find_packages

desc = 'Broker to invoke the DEMO APIs'

# from pip.req import parse_requirements
# from pip.download import PipSession

# install_reqs = parse_requirements('requirements.txt', session=PipSession())
# reqs = [str(ir.req) for ir in install_reqs]

with open('requirements.txt') as fp:
    reqs = fp.read().splitlines()

setup(
    name='broker-demo',
    version='0.0.8',
    description=('DEMO Broker'),
    long_description=desc,
    url='https://github.ibm.com/fd4b-demo/broker-demo',
    author='Team Hermes',
    author_email='team-hermes@ibm.com',
    license='Apache v2',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=reqs,
    package_data={},
    data_files=['requirements.txt'],
    entry_points={
        'console_scripts': [
            'broker-demo = demo.__main__:main'
        ],
    },
)
