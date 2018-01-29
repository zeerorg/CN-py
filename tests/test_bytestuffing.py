"""
Test byte stuffing module
"""
from algo.bytestuffing import stuff_byte

def test_stuff_byte():
    """
    Test stuff_byte function
    """
    assert stuff_byte('abF') == 'ab/F'
    assert stuff_byte('F') == '/F'
    assert stuff_byte('//F') == '/////F'
    assert stuff_byte('') == ''
