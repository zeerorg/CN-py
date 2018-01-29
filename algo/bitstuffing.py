"""
Implements bit stuffing algo
"""

import bitstring


def to_bitarray(input_str: str) -> bitstring.BitArray:
    """
    Converts 0's and 1's string to bitarray

    """
    return bitstring.BitArray('0b{}'.format(input_str)) if input_str else bitstring.BitArray('0b0')


def stuff_bit(data: bitstring.BitArray) -> bitstring.BitArray:
    """
    Takes data bitarray and stuffs bit into it.

    """
    ans = bitstring.BitArray('0b0')
    pattern = bitstring.BitArray(bin='0b011111')
    for bit in data:
        ans.append('0b{:d}'.format(bit))
        if ans.len > 5 and (ans[-6:] ^ pattern).int == 0:
            ans.append('0b0')

    return ans[1:]
