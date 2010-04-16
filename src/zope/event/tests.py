##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
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
""" Test the event system
"""
import unittest
import doctest

class Test_notify(unittest.TestCase):

    def setUp(self):
        from zope.event import subscribers
        self._old_subscribers = subscribers[:]
        subscribers[:] = []

    def tearDown(self):
        from zope.event import subscribers
        subscribers[:] = self._old_subscribers

    def _callFUT(self, event):
        from zope.event import notify
        notify(event)

    def test_empty(self):
        event = object()
        self._callFUT(event)

    def test_not_empty(self):
        from zope.event import subscribers
        dummy = []
        subscribers.append(dummy.append)
        event = object()
        self._callFUT(event)
        self.assertEqual(dummy, [event])

def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(Test_notify),
        doctest.DocFileSuite('README.txt'),
        ))
