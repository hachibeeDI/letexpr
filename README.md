
[![Build Status](https://travis-ci.org/hachibeeDI/letexpr.png?branch=master)](https://travis-ci.org/hachibeeDI/letexpr)

# letexpr

That is python module imitate `let expression` like a Haskell.

And support lazy evaluation.


# Installation

```bash
$ pip install https://github.com/hachibeeDI/letexpr/archive/master.zip
```


# Example

```python
from letexpr import let, expr

# expr(x) = lambda x: lambda: x

answer = (
    let()
        | ('x', expr(10))
        | ('y', expr(20))
        | ('size', lambda x, y: x * y)
        | ('hoge', lambda x, y: 'fooo')
    ).in_(lambda x, y, size:
        'x = {x}, y = {y}, x * y = {size}'.format(x=x, y=y, size=size))
print answer
#  => 'x = 10, y = 20, x * y = 200'


# with List Comprehensions
even_or_odd = [
    (let()
        | ('_i', expr(str(i)))
        | ('r', expr('even' if i % 2 == 0 else 'odd'))
    ).in_(lambda _i, r:
        _i + ' is an ' + r  + ' number.')
            for i in range(1, 5)]
print even_or_odd
#  => ['1 is odd number.', '2 is even number.', '3 is odd number.', '4 is even number.']


# with anonymous function
let_ = (let()
    | ('x', expr('x'))
    | ('y', expr('y'))
)
@let_.in_()
def _(x, y):
    return x + y
print let_.end
#  => 'xy'

```

# Testing


```bash
$ pip install nose
$ nosetests --with-doctest
```
