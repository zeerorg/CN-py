"""
Test bit stuffing algo
"""
from algo.bitstuffing import stuff_bit, to_bitarray

def test_stuff_bit():
    """
    Test stuff_bit
    """
    assert stuff_bit(to_bitarray('001101111101')).bin == to_bitarray('0011011111001').bin
    assert stuff_bit(to_bitarray('011111')).bin == to_bitarray('0111110').bin
    assert stuff_bit(to_bitarray('0011')).bin == to_bitarray('0011').bin
    assert stuff_bit(to_bitarray('0')).bin == to_bitarray('0').bin


def test_to_bitarray():
    """
    Test to_bitarray
    """
    assert to_bitarray('001101111101').bin == '001101111101'
    assert to_bitarray('').bin == '0'
