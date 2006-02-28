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
"""Message IDs.

$Id$
"""
import zope.deprecation
zope.deprecation.deprecated('MessageID',
                            'Mutable i18n messages ("message ids") have been '
                            'deprecated in favour of immutable ones and will '
                            'be removed in Zope 3.3.  Please use '
                            'zope.i18nmessageid.Message instead.')
zope.deprecation.deprecated('MessageIDFactory',
                            'Mutable i18n messages ("message ids") have been '
                            'deprecated in favour of immutable ones and will '
                            'be removed in Zope 3.3.  Please use '
                            'use zope.i18nmessageid.MessageFactory instead.')

class MessageID(unicode):
    """Message ID.

    This is a string used as a message ID.  It has a domain attribute that is
    its source domain, and a default attribute that is its default text to
    display when there is no translation.  domain may be None meaning there is
    no translation domain.  default may also be None, in which case the
    message id itself implicitly serves as the default text.

    MessageID objects also have a mapping attribute which must be set after
    construction of the object.  This is used when translating and
    substituting variables.

    To instanciate MessageIDs, it is recommended to use MessageIDFactory:

    >>> fact = MessageIDFactory('test')

    Now we can use the factory to make MessageIDs. Note that MessageID
    is a subclass of unicode:

    >>> id = fact(u'this is a test')
    >>> isinstance(id, MessageID)
    True
    >>> isinstance(id, unicode)
    True

    Additional parameters, such as the i18n domain and the default
    text are available through attributes:

    >>> id.domain
    'test'
    >>> id.default
    u'this is a test'

    You can also reset the default text:

    >>> id.default = u'blah'
    >>> id.default
    u'blah'

    It is quite common to pass an abstract identifier as message id
    and then a default text:

    >>> id = fact(u'test-id', 'default test')
    >>> id
    u'test-id'
    >>> id.default
    u'default test'
    >>> id.domain
    'test'
    """

    __slots__ = ('domain', 'default', 'mapping')

    def __new__(cls, ustr, domain=None, default=None):
        self = unicode.__new__(cls, ustr)
        self.domain = domain
        if default is None:
            self.default = ustr
        else:
            self.default = unicode(default)
        self.mapping = {}
        return self

    def __getstate__(self):
        return unicode(self), self.domain, self.default, self.mapping

    def __setstate__(self, (ustr, domain, default, mapping)):
        super(MessageID, self).__init__(ustr)
        self.domain = domain
        if default is None:
            self.default = ustr
        else:
            self.default = default
        self.mapping = mapping


class MessageIDFactory(object):
    """Factory for creating MessageIDs."""

    def __init__(self, domain):
        self._domain = domain

    def __call__(self, ustr, default=None):
        return MessageID(ustr, self._domain, default)
