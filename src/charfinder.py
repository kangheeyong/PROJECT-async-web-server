import re
import sys
import pickle
import functools
import unicodedata

from collections import defaultdict, namedtuple


RE_WORD = re.compile('\w+')

INDEX_NAME = 'charfinder_index.pickle'

CharDescription = namedtuple('CharDescription', 'code_str char name')
QueryResult = namedtuple('QueryResult', 'count items')


def tokenize(text):
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


class UnicodeNameIndex:
    def __init__(self):
        self._load()

    def _load(self):
        self.index = None
        try:
            with open(INDEX_NAME, 'rb') as fp:
                self.index = pickle.load(fp)
        except OSError:
            self._build_index()
            self._save()

    def _save(self):
        with open(INDEX_NAME, 'wb') as fp:
            pickle.dump(self.index, fp)

    def _build_index(self):
        chars = (chr(i) for i in range(32, sys.maxunicode))
        index = defaultdict(set)
        for char in chars:
            try:
                name = unicodedata.name(char)
            except ValueError:
                continue
            for word in tokenize(name):
                index[word].add(char)
        self.index = index

    def find_chars(self, query):
        result_sets = []
        for word in tokenize(query):
            chars = self.index[word]
            if not chars:
                return QueryResult(0, ())
            result_sets.append(chars)

        result = functools.reduce(set.intersection, result_sets)
        result = sorted(result)
        return QueryResult(len(result), result)

    def _describe(self, char):
        code_str = 'U+{:04X}'.format(ord(char))
        name = unicodedata.name(char)
        return CharDescription(code_str, char, name)

    def find_descriptions(self, query, start=0, stop=None):
        for char in self.find_chars(query).items[start:stop]:
            yield self._describe(char)


def main(*args):
    index = UnicodeNameIndex()

    index.find_chars('sign')
    breakpoint()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print('Usage: {} word1 [word2]...'.format(sys.argv[0]))
