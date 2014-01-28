# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals,)

import sys
import unittest
if sys.version_info[0] == 2:
    from itertools import izip_longest as zip_longest
else:
    from itertools import zip_longest


from letexpr import let

from nose.tools import eq_


suite = unittest.TestSuite()
loader = unittest.TestLoader()
# use `nosetests --with-doctest`
# suite.addTests(doctest.DocTestSuite(letexpr))


def test_executed():
    (let() | ('x', lambda: 10)
     ).in_(lambda x: eq_(x, 10))


def test_lazy_evalucated():
    '''
    The let-expr module evalucate the expression is demanded as arguments.
    And content of that expression would not be evalucated.
    '''
    watcher = LoadOrderWatcher()
    (let()
     | ('x', lambda: watcher.append('Iam x'))
     | ('y', lambda: watcher.append('Iam y'))
     | ('z', lambda y: watcher.append('Iam z'))
     | ('_a', lambda x: watcher.append('Iam _a'))
     ).in_(lambda _a, z: None)
    watcher.expected(
        'Iam y',
        'Iam x',
        'Iam z',
        'Iam _a',
    )


class LoadOrderWatcher(list):
    def __init__(self):
        super(LoadOrderWatcher, self).__init__()

    def append(self, var):
        super(LoadOrderWatcher, self).append(var)
        return var

    def expected(self, *orders):
        for expect, supplied in zip_longest(orders, self):
            eq_(expect, supplied)
