# coding=utf-8

from __future__ import unicode_literals


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


if __name__ == '__main__':
    __import__('ipdb').set_trace()
