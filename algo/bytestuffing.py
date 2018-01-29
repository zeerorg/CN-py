"""
Implements byte stuffing
"""

FLAG_CHAR = 'F'
ESC_CHAR = '/'

def stuff_byte(input_str: str) -> str:
    """
    Byte stuffing function
    """
    ans = []
    for char in input_str:
        if char in [FLAG_CHAR, ESC_CHAR]:
            ans.append(ESC_CHAR)
        ans.append(char)
    return ''.join(ans)
