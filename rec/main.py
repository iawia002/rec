# coding=utf-8

from __future__ import unicode_literals

import re


__all__ = ['domain']


class Base(object):
    rule = None

    def __call__(self, text, ret='list'):
        '''
        ret:
            list: return all match results
            bool: return if match
            other return the re rule object
        '''
        if not self.rule:
            raise NotImplementedError()

        if ret not in ['list', 'bool']:
            return self.rule

        results = self.rule.findall(text)
        if ret == 'list':
            return results
        if ret == 'bool':
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
        r'('
        r'cn|com\.cn|com\.hk|com|net|edu|gov|biz|org|info|pro|name|xxx|xyz|'
        r'me|top|cc|tv'
        r')(?!\.)',  # can't be a dot after root domain
        re.I
    )

    def __call__(self, text, ret='list', root=True):
        results = super(Domain, self).__call__(text, ret)
        if ret != 'list':
            return results
        if root:
            return ['.'.join(item) for item in results]
        return [item[0] for item in results]


domain = Domain()


if __name__ == '__main__':
    __import__('ipdb').set_trace()
