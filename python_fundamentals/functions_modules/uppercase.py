#!/usr/bin/env python3
def uppercase(str):
    res = ""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            res += chr(code - 32)
        else:
            res += c
    print("{}".format(res))
    