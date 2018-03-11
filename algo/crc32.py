"""
CRC 32 algorithm implementation
"""
from collections import deque
from toolz import compose
from functools import reduce, partial
from operator import __xor__


def calculate_crc(input_data: str, polynomial: str) -> str:
    """
    Takes input data and polynomial and calculates CRC which can then be chaecked
    >>> calculate_crc("1101011011", "10011")
    '11010110111110'

    """
    poly_len = polynomial.__len__()
    input_arr = compose(list, partial(map, int)) (input_data) + ([0] * (poly_len-1))
    polynomial = compose(list, partial(map, int)) (polynomial)
    remainder = get_remainder_list(input_arr, polynomial)
    ans = input_data + ''.join(map(str, remainder[-poly_len+1:]))
    return ans


def get_remainder_list(dividend: list, divisor: list) -> list:
    og_divisor = ([0] * (dividend.__len__() - divisor.__len__())) + list(x for x in divisor)
    divisor.extend([0] * (dividend.__len__() - divisor.__len__()))
    assert og_divisor.__len__() == dividend.__len__() == divisor.__len__()
    while dividend >= og_divisor:
        if dividend >= divisor:
            dividend = subtract_nums(dividend, divisor)
        divisor = [0] + divisor[:-1]

    return dividend


def subtract_nums(num1: list, num2: list) -> list:
    assert num1.__len__() == num2.__len__()
    assert num1 > num2
    borrow = 0
    ans = deque()
    for pos in range(1, num1.__len__() + 1):
        pos = -pos
        if num1[pos] != num2[pos]:
            ans.appendleft(1)
        else:
            ans.appendleft(0)

    return list(ans)

calculate_crc("1101011011", "10011")