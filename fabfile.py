# coding=utf-8

from fabric.api import (
    local,
)


def test():
    local(
        'PYTHONPATH=./ coverage run tests/runtests.py'
    )
