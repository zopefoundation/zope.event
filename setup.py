##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
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
"""Setup for zope.i18nmessageid package

$Id$
"""

import os

try:
    from setuptools import setup, Extension, find_packages
    packages = find_packages('src', exclude=['zope.testing',
                                             'zope.testing.*',
                                             'zope.deprecation'])

except ImportError, e:
    from distutils.core import setup, Extension
    packages = ['zope', 'zope.i18nmessageid']

setup(name='zope_i18nmessageid',
      version='3.0',

      url='http://svn.zope.org/zope.i18nmessageid',
      license='ZPL 2.1',
      description='Zope 3 i18n Message Identifier',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description='',
      
      packages=packages,
      package_dir = {'': 'src'},

      ext_modules=[Extension("zope.i18nmessageid._zope_i18nmessageid_message",
                             [os.path.join('src', 'zope', 'i18nmessageid',
                                           "_zope_i18nmessageid_message.c")
                              ]),
                   ],

      namespace_packages=['zope',],
      tests_require = ['zope_testing'],
      install_requires=['zope_deprecation'],
      include_package_data = True,

      zip_safe = False,
      )
