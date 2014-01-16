# -*- coding: utf-8 -*-

from inspect import getargspec


class let(object):
    '''
    >>> (let() \
            | ('x', lambda : 10) \
            | ('y', lambda : 20) \
            | ('size', lambda x, y: x * y) \
            | ('hoge', lambda x, y: 'fooo') \
        ).in_(lambda x, y, size: \
                 'x = {x}, y = {y}, x * y = {size}'.format(x=x, y=y, size=size))
    'x = 10, y = 20, x * y = 200'

    >>> [ \
        (let() \
            | ('_i', lambda : str(i)) \
            | ('r', lambda : 'even' if i % 2 == 0 else 'odd') \
        ).in_(lambda _i, r: \
            _i + ' is an ' + r  + ' number.') \
                for i in range(1, 5)]
    ['1 is an odd number.', '2 is an even number.', '3 is an odd number.', '4 is an even number.']
    '''

    def __init__(self, action=None):
        if action is not None:
            name, act = action
            self.lets = {name: act()}
        else:
            self.lets = {}

    def __or__(self, action):
        ''' :type action: (str, func) '''
        name, f = action
        require_arg_keys = getargspec(f).args
        self.lets[name] = f(
            **self.__extract_require_args(require_arg_keys)
        )
        return self

    def __extract_require_args(self, arg_keys):
        try:
            # I think it is dirty hack too, but now most people use python2.
            binded_items = self.lets.iteritems()
        except AttributeError:
            binded_items = self.lets.items()
        return dict((k, v) for k, v in binded_items if k in arg_keys)

    def in_(self, func):
        require_arg_keys = getargspec(func).args
        return func(
            **self.__extract_require_args(require_arg_keys)
        )


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
