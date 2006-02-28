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
"""I18n Messages

$Id$
"""
##############################################################################
# BBB 2005/10/10 -- MessageIDs are to be removed for Zope 3.3
#
import zope.deprecation
zope.deprecation.__show__.off()
from zope.i18nmessageid.messageid import MessageID, MessageIDFactory
zope.deprecation.__show__.on()
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
#
##############################################################################

from zope.i18nmessageid.message import Message, MessageFactory
