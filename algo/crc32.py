"""
CRC 32 algorithm implementation
"""
from collections import deque
from functools import reduce
from operator import __xor__


def calculate_crc(input_data: str, ploynomial: str) -> str:
    """
    Takes input data and polynomial and calculates CRC which can then be chaecked
    # >>> calculate_crc("1101011011", "10011")
    # '11010110111110'

    """
    appended_data = input_data + ("0" * len(ploynomial[1:]))

    return strip_bits(add_bits(appended_data, get_rem_2(appended_data, ploynomial)))

def get_rem_2(dividend: str, divisor: str) -> str:
    """
    Take dividend and divisor and get remainder
    # >>> get_rem_2("10", "10")
    # '0'
    # >>> get_rem_2("1110", "101")
    # '100'

    >>> get_rem_2("1100100", "11")
    '1'
    """
    portion = len(divisor)
    og_divisor = divisor
    divisor += "0" * (len(dividend) - len(divisor))
    assert len(divisor) == len(dividend)
    while bit_gt(dividend, og_divisor) or dividend == og_divisor:
        if bit_gt(dividend, divisor) or dividend[:portion] == divisor[:portion]:
            dividend = strip_bits(get_difference(dividend, divisor))
        divisor = divisor[:-1]
    return dividend if dividend else '0', dividend, divisor


def add_bits(first: str, second: str) -> str:
    """
    Adds two bit strings
    >>> add_bits("10", "10")
    '100'
    >>> add_bits("10", "1")
    '011'
    >>> add_bits("1001", "10")
    '01011'
    """
    ans = deque()
    new_first = ("0" * (max(len(first), len(second)) - len(first) + 1)) + first
    new_second = ("0" * (max(len(first), len(second)) - len(second) + 1)) + second
    first, second = new_first, new_second
    assert len(first) == len(second)
    carry = "0"
    for pos in range(1, len(first)+1):
        ans.appendleft(str(reduce(__xor__, map(int, [first[-pos], second[-pos], carry]))))
        carry = str(int([first[-pos], second[-pos], carry].count("1") > 1))

    return ''.join(ans)

def get_difference(first: str, second: str) -> str:
    """
    Calculates difference between two bit strings
    >>> strip_bits(get_difference("10", "1"))
    '1'
    >>> strip_bits(get_difference("10110", "1"))
    '10101'
    >>> strip_bits(get_difference("1001011", "101"))
    '1000110'
    """
    # ans = deque()
    # second = add_bits(get_complement(second), "1")

    new_first = ("0" * (max(len(first), len(second)) - len(first))) + first
    new_second = ("0" * (max(len(first), len(second)) - len(second))) + second
    first, second = new_first, new_second

    # assert len(first) == len(second)
    # carry = "0"
    # for pos in range(1, len(first)+1):
    #     ans.appendleft(str(reduce(__xor__, map(int, [first[-pos], second[-pos], carry]))))
    #     carry = int([first[-pos], second[-pos], carry].count("1") > 1)
    ans = add_bits(first, strip_bits(add_bits(get_complement(second), "1")))

    return ans[1:]

def get_complement(bin_str: str) -> str:
    """
    Complement a binary string and return it
    >>> get_complement("100")
    '011'
    >>> get_complement("1")
    '0'
    """
    custom_dict = {"1": "0", "0": "1"}
    return ''.join(map(custom_dict.__getitem__, bin_str))

def strip_bits(bit_string: str) -> str:
    """
    Strips the most significant bit if it's '0'
    >>> strip_bits("001")
    '1'
    >>> strip_bits("0101")
    '101'
    >>> strip_bits("1100")
    '1100'
    """
    ctr = 0
    for pos in bit_string:
        if pos == "1":
            break
        ctr += 1
    return bit_string[ctr:]

def bit_gt(bigger: str, smaller: str) -> bool:
    """
    Compares two bit strings and tells if left is bigger
    >>> bit_gt("101", "01")
    True
    >>> bit_gt("1", "1")
    False
    >>> bit_gt("0", "1")
    False
    >>> bit_gt("0011", "00001")
    True
    """
    flag = None
    for bit1, bit2 in zip(*get_paded(bigger, smaller)):
        if bit1 != bit2:
            flag = bit1 == "1"
            break

    return bool(flag)


def get_paded(first: str, second: str) -> str:
    """
    Take unpaded bit string and return paded sring of equal length
    >>> get_paded("1", "1001")
    ('0001', '1001')
    >>> get_paded("100101", "001")
    ('100101', '000001')

    >>> get_paded("", "00")
    ('00', '00')
    """
    return ("0" * (max(len(first), len(second)) - len(first))) + first, \
            ("0" * (max(len(first), len(second)) - len(second))) + second

if __name__ == "__main__":
    import doctest
    doctest.testmod()
