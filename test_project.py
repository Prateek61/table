import pytest

from modules.parser import parser

def test_parser():
    assert parser.parse_args([]).w == None
    assert parser.parse_args(['-w', 'hello']).w == 'hello'
    assert parser.parse_args(['-w']).w == None