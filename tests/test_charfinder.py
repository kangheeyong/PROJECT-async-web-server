import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'src'))

from charfinder import tokenize, UnicodeNameIndex


def test_tokenize():
    assert list(tokenize('')) == []
    assert list(tokenize('a b')) == ['A', 'B']
    assert list(tokenize('a-b')) == ['A', 'B']
    assert list(tokenize('abc')) == ['ABC']
    assert list(tokenize('@ab-c')) == ['AB', 'C']


def test_index():
    index = UnicodeNameIndex().index
    assert len(index) > 10000


def test_find_no_word_match():
    result = UnicodeNameIndex().find_chars('kdjshfkjsd')
    assert result.count == 0


def test_find_word_match_1():
    result = UnicodeNameIndex().find_chars('chess black')
    assert result.count == 6


def test_find_word_match_2():
    result = UnicodeNameIndex().find_chars('sign')
    assert result.items[:2] == ['#', '$']


def test_find_description_match_1():
    result = UnicodeNameIndex().find_descriptions('sign', 0, 2)
    result = list(result)
    assert result[0].char == '#'
    assert result[1].char == '$'


def test_find_description_match_2():
    result = UnicodeNameIndex().find_descriptions('sign', 1, 3)
    result = list(result)
    assert result[0].char == '$'
    assert result[1].char == '%'




