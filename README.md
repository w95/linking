#linking

[![Badge](https://badge.fury.io/py/linking.svg "Badge")](https://badge.fury.io/py/linking "Badge")

linking is easy to use linkifier that converts URLs and emails to HTML hyperlinks

| <!-- -->  | <!-- --> |
| ------------ | ------------ |
| Code | https://github.com/w95/linking |
| Issue tracker | https://github.com/w95/linking/issues |
| License | MIT License; see LICENSE file |



###Installing linking

linking is available on [PyPI](https://pypi.org/project/linking/), so you can install it with ``pip``::

    $ pip install linking


###Basic use

The simplest way to use linking is:

```python
import linking

linking.text('some text tesla.com, ...')
# -> 'some text <a href="http://tesla.com">tesla.com</a>, ...'

linking.text('https://tesla.com', {'rel': 'nofollow'})
# -> '<a href="https://tesla.com" rel="nofollow">https://tesla.com</a>'

linking.text('elon@tesla.com')
# -> '<a href="mailto:elon@tesla.com">elon@tesla.com</a>'
```
