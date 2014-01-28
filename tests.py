# -*- coding: utf-8 -*-

import unittest
from letexpr import let

from nose.tools import eq_


suite = unittest.TestSuite()
loader = unittest.TestLoader()
# use `nosetests --with-doctest`
# suite.addTests(doctest.DocTestSuite(letexpr))


def test_initialize_with_func():
    (let() | ('x', lambda: 10)
     ).in_(lambda x: eq_(x, 10))
