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
    r = (let()
         | ('x', lambda: 10)
         | ('y', lambda: 20)
         | ('size', lambda x, y: x * y)
         | ('hoge', lambda x, y: 'fooo')
         ).in_(lambda x, y, size: 'x = {x}, y = {y}, x * y = {size}'.format(x=x, y=y, size=size))
    assert r == 'x = 10, y = 20, x * y = 200'

    r = [
        (let()
            | ('_i', lambda: str(i))
            | ('r', lambda: 'even' if i % 2 == 0 else 'odd')
         ).in_(lambda _i, r: _i + ' is an ' + r + ' number.')
        for i in range(1, 5)
    ]
    assert r == \
        ['1 is an odd number.', '2 is an even number.', '3 is an odd number.', '4 is an even number.']


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
