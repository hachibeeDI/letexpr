
[![Build Status](https://travis-ci.org/hachibeeDI/letexpr.png?branch=master)](https://travis-ci.org/hachibeeDI/letexpr)

# letexpr

That is python module imitate `let expression` like a Haskell.


# Installation

```bash
$ pip install https://github.com/hachibeeDI/letexpr/archive/master.zip
```


# Example

```python
from letexpr import let

answer = (
    let()
        | ('x', lambda : 10)
        | ('y', lambda : 20)
        | ('size', lambda x, y: x * y)
        | ('hoge', lambda x, y: 'fooo')
    ).in_(lambda x, y, size:
        'x = {x}, y = {y}, x * y = {size}'.format(x=x, y=y, size=size))
print answer
#  => 'x = 10, y = 20, x * y = 200'


# with List Comprehensions
even_or_odd = [
    (let()
        | ('_i', lambda : str(i))
        | ('r', lambda : 'even' if i % 2 == 0 else 'odd')
    ).in_(lambda _i, r:
        _i + ' is an ' + r  + ' number.')
            for i in range(1, 5)]
print even_or_odd
#  => ['1 is odd number.', '2 is even number.', '3 is odd number.', '4 is even number.']
```

# Testing


```bash
$ pip install nose
$ nosetests --with-doctest
```
