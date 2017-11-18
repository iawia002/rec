rec
===

.. image:: https://travis-ci.org/iawia002/rec.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/iawia002/rec


a collection of some useful regular expressions.

Hello, world
------------

Installation

.. code-block:: bash

    pip install rec

Example

.. code-block:: python

    In [1]: import rec

    In [2]: rec.domain('http://bangumi.bilibili.com/anime/1089')
    Out[2]: [u'bilibili.com']

    In [3]: rec.domain('http://bangumi.bilibili.com/anime/1089', root=False)
    Out[3]: ['bilibili']


Documentation
-------------

TODO


🌙
