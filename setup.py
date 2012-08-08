#!/usr/bin/env python

from setuptools import setup

setup(
    name='komodo-python-dbgp',
    version='7.1.0',
    description='The ActiveState Komodo DBGP server',

    author="Shane Caraveo, Trent Mick",
    author_email="komodo-feedback@ActiveState.com",
    maintainer='Adam Groszer',
    maintainer_email='agroszer@gmail.com',

    url='http://github.com/agroszer/komodo-python-dbgp',
    packages=['dbgp'],
    scripts=['bin/pydbgp',
             'bin/pydbgpproxy'],
    zip_safe=False,
)
