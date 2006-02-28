##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
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
"""Message ID tests.

$Id$
"""
import unittest
from zope.testing.doctestunit import DocTestSuite, DocFileSuite

def test_suite():
    return unittest.TestSuite((
	    DocTestSuite('zope.i18nmessageid.messageid'),
	    DocTestSuite('zope.i18nmessageid.message'),
	    DocFileSuite('messages.txt', package='zope.i18nmessageid'),
	    ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
