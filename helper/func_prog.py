"""
Helper methods for functional programming
"""

import functools

def compose(*funcs):
    """
    Compose a list of functions into a single function
    """
    def main_func(*fargs, **fkeywords):
        """
        The composed function from list of functions provided
        The function at right runs first, so we need to reverse the list
        """

        return functools.reduce(lambda composed_ans, func: func(composed_ans),
                                funcs[::-1][1:],
                                funcs[-1](*fargs, **fkeywords))

    return main_func


def compose_wrapped_returns(*funcs):
    """
    A compose function for only monads
    The returned ans is unwraped before return
    """
    def main_func(*fargs, **fkeywords):
        """
        The real returned function
        """

        return functools.reduce(lambda composed_monad, func: func(*composed_monad.args),
                                funcs[::-1][1:],
                                funcs[-1](*fargs, **fkeywords)).args

    return main_func


def unwrap_monad(monad):
    return 
    pass


class Wrapped():
    """
    Wraps the return value so that compose knows what to pass
    It is a helper class for making monads
    """
    def __init__(self, to_wrap):
        self.args = to_wrap


def wrap_output(func):
    """
    HOF for wrapping the function output in `Wrapped`
    """
    def main_func(*fargs, **fkeywords):
        """
        Gets and wraps
        """
        ans = func(*fargs, **fkeywords)
        return Wrapped(ans)

    return main_func
