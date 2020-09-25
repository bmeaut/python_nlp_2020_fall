#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def word_freq(s):
    frequencies = {}
    words = s.split()

    for word in words:
        if word not in frequencies.keys():
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    return frequencies


def main():
    s = "the green tea and the black tea"
    assert (word_freq(s) == {"the": 2, "tea": 2, "green": 1, "black": 1, "and": 1})

    print("Tests passed.")


if __name__ == '__main__':
    main()
