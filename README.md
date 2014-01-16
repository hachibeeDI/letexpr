
# letexpr

That is python module imitate 'let expression' like a Haskell.


# Installation

```
$ pip install https://github.com/hachibeeDI/letexpr/archive/master.zip
```

# Usage

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
# => 'x = 10, y = 20, x * y = 200'
```

# Testing


