import re
import operator
from functools import reduce
from bisect import bisect_left


def prod(*iterables):
    return reduce(operator.mul, *iterables)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def pfloats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s):
    return re.findall(r"[a-zA-Z]+", s)


def ints(s):
    return lmap(int, re.findall("-?\d+", s))


def pints(s):
    return lmap(int, re.findall("\d+", s))


def alphanum(s):
    return re.findall(r"-?\w+", s)


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1


# Pairs should be list of (ai,ni); outputs x such that x is congruent to ai mod ni for all i
def chinese_remainder(pairs):
    res = 0
    _, N = zip(*pairs)
    P = reduce(lambda x, y: x * y, N)
    for a, n in pairs:
        p = P // n
        res += (
            a * pow(p, -1, n) * p
        )  # could also use Fermat's little theorem pow(p,n-2,n)
    return res % P
