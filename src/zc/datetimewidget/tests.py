##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
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
"""Datetime Widget unittests

$Id$
"""
__docformat__ = "reStructuredText"
import os
import doctest
import unittest
import zc.datetimewidget
from doctest import DocFileSuite

from zope.app.wsgi import testlayer


DTWidgetLayer = testlayer.BrowserLayer(
    zc.datetimewidget,
    os.path.join(os.path.dirname(__file__), 'ftesting.zcml'),
    name='DTWidgetLayer',
    allowTearDown=True)


def test_suite():
    # XXX Use DocFileSuite instead?
    DemoSuite = DocFileSuite(
        'demo/README.txt',
        globs={'layer': DTWidgetLayer})
    DemoSuite.layer = DTWidgetLayer
    return unittest.TestSuite((
        DocFileSuite(
            'widgets.txt',
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        DocFileSuite(
            'datetimewidget.txt',
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        DemoSuite
        ))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
