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
    from setuptools import setup, Extension
except ImportException, e:
    from distutils.core import setup, Extension
    
setup(name='zope.i18nmessageid',
      version='3.0',

      url='http://svn.zope.org/zope.i18nmessageid',
      license='ZPL 2.1',
      description='Zope 3 Interface Infrastructure',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description='The implementation of interface definitions for Zope 3.',
      
      packages=["zope", "zope.i18nmessageid"],
      package_dir = {'': 'src'},

      ext_modules=[Extension("zope.i18nmessageid._zope_i18nmessageid_message",
                             [os.path.join('src', 'zope', 'i18nmessageid',
                                           "_zope_i18nmessageid_message.c")
                              ]),
                   ],

      tests_require = ['zope_testing'],
      requires=['zope_deprecation'],
      include_package_data = True,
      zip_safe = False,
      )
