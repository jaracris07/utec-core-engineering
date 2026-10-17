#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1
    negative_exp = False
    if b < 0:
        negative_exp = True
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    if negative_exp:
        return 1 / result
    return result
