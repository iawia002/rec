# coding=utf-8

from __future__ import unicode_literals

import re


__all__ = ['domain']


class Base(object):
    rule = None

    def __call__(self, text, result='list'):
        '''
        result:
            list: return all match results
            boolean: return if match
            other return the re rule object
        '''
        if not self.rule:
            raise NotImplementedError()

        if result not in ['list', 'boolean']:
            return self.rule

        results = self.rule.findall(text)
        if result == 'list':
            return results
        if result == 'boolean':
            if len(results):
                return True
            return False


class Domain(Base):
    '''
    Each domain name consists of letters(not case-sensitive), numbers and
    minus sign (can't be the first letter), the length doesn't exceed 63
    '''
    rule = re.compile(
        r'([a-z0-9][-a-z0-9]{0,62})\.'
        '(com\.cn|com|net|cn)',
        re.I
    )

    def __call__(self, text, result='list', root=True):
        results = super(Domain, self).__call__(text, result)
        if result != 'list':
            return results
        if root:
            return ['.'.join(item) for item in results]
        return [item[0] for item in results]


domain = Domain()


if __name__ == '__main__':
    __import__('ipdb').set_trace()
