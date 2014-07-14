# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals,)


from types import FunctionType, LambdaType
from inspect import getargspec


def expr(x):
    ''' x -> (void -> x) '''
    return lambda: x


class let(object):
    '''
    '''

    def __init__(self):
        self.lets = {}
        self.end = None

    def __or__(self, action):
        ''' :type action: (str, func) '''
        name, f = action
        require_arg_keys = getargspec(f).args
        self.lets[name] = MemoizedLazyFunction(
            f,
            **self.__extract_require_args(require_arg_keys)
        )
        return self

    def __extract_require_args(self, arg_keys):
        try:
            # I think it is dirty hack too, but now most people use python2.
            binded_items = self.lets.iteritems()
        except AttributeError:
            binded_items = self.lets.items()
        return dict((k, func()) for k, func in binded_items if k in arg_keys)

    def in_(self, func=None):
        if func is not None and not isinstance(func, (LambdaType, FunctionType, )):
            raise TypeError('argument "func" should be lambda or function.')


        def in_expr_as_decorator(func):
            require_arg_keys = getargspec(func).args
            self.end = func(
                **self.__extract_require_args(require_arg_keys)
            )

        if func is None:
            # used as decorator
            return in_expr_as_decorator
        else:
            require_arg_keys = getargspec(func).args
            return func(
                **self.__extract_require_args(require_arg_keys)
            )


class MemoizedLazyFunction(object):
    def __init__(self, func, **require_args):
        self.func = func
        self.args = require_args
        self.result = None  # Option?

    def __call__(self):
        if self.result is None:
            self.result = self.func(**self.args)
        return self.result


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
