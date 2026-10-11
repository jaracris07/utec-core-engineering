#!/usr/bin/env python3
alphabet = ""
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != 'e' and letter != 'q':
        alphabet += letter
print("{}".format(alphabet), end="")
