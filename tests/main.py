# coding=utf-8

from __future__ import unicode_literals

import unittest

import rec


class MainTest(unittest.TestCase):

    def test_domain(self):
        self.assertEqual(rec.domain('aa.com'), ['aa.com'])
        self.assertEqual(rec.domain('aa.com', root=False), ['aa'])
        self.assertTrue(rec.domain('aa.com', result='boolean'))
        self.assertFalse(rec.domain('hello', result='boolean'))


if __name__ == '__main__':
    unittest.main()
