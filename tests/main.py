# coding=utf-8

from __future__ import unicode_literals

import unittest

import rec


class MainTest(unittest.TestCase):

    def test_domain(self):
        self.assertEqual(rec.domain('aa.com'), ['aa.com'])
        self.assertEqual(rec.domain('aa.com', root=False), ['aa'])
        self.assertTrue(rec.domain('aa.com', ret='bool'))
        self.assertFalse(rec.domain('hello', ret='bool'))
        self.assertEqual(rec.domain('www.com.com'), ['com.com'])
        self.assertEqual(rec.domain('com.cn'), ['com.cn'])
        self.assertEqual(rec.domain('www.com.cn'), ['www.com.cn'])
        self.assertEqual(rec.domain('www.aa.com.cn'), ['aa.com.cn'])


if __name__ == '__main__':
    unittest.main()
