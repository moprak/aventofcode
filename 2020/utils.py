import re
def lmap(func, *iterables):
    return list(map(func, *iterables))

def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))

def pfloats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

def words(s):
    return re.findall(r"[a-zA-Z]+", s)

def ints(s):
    return lmap(int,re.findall('-?\d+', s))

def pints(s):
    return lmap(int,re.findall('\d+', s))

def alphanum(s):
    return re.findall(r'-?\w+',s)

from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1

