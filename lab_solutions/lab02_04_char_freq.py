#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def char_freq(s):
    frequencies = {}
    for char in s:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1

    return frequencies


def main():
    assert char_freq("aba") == {"a": 2, "b": 1}
    assert char_freq("") == {}

    print("Tests passed.")


if __name__ == '__main__':
    main()
