##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.event package

$Id$
"""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='zope.event',
    version='3.4.1',
    url='http://pypi.python.org/pypi/zope.event',
    license='ZPL 2.1',
    description='Very basic event publishing system',
    author='Zope Corporation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=(
        read('README.txt')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'zope', 'event', 'README.txt')
        + '\n' +
        'Download\n'
        '********\n'
        ),
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope',],
      include_package_data=True,
      install_requires=['setuptools'],
      zip_safe=False,
      )
