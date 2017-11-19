# rec documentation

## Basic

All methods have two basic parameters:

* **text**: String, the source text.
* **ret**: String, the type of data returned.
  * **list**(default): Matched results.
  * **bool**: Return whether the result is matched.
  * **object**: Return `re.compile` object of the match rule.

```python
In [1]: import rec

In [2]: rec.domain('https://google.com')
Out[2]: [u'google.com']

In [3]: rec.domain('https://google.com', ret='bool')
Out[3]: True

In [4]: rec.domain('https://google.com', ret='object')
Out[4]:
re.compile(...)
```

The following methods list no longer separately write the meaning of these two parameters.

## methods list

### domain(text, ret='list', root=True)

Get the domain name from a URL

**Parameters**:

  * **root**: Boolean, default `True`, whether the result needs to include the root domain name.

```python
In [1]: import rec

In [2]: rec.domain('https://google.com')
Out[2]: [u'google.com']

In [3]: rec.domain('https://google.com', root=False)
Out[3]: ['google']

In [4]: rec.domain('https://google.com', ret='bool')
Out[4]: True
```

