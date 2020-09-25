#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def get_char_bigrams(s):
    bigram_counts = {}

    for i in range(len(s) - 1):
        key = s[i:i + 2]
        if key not in bigram_counts:
            bigram_counts[key] = 1
        else:
            bigram_counts[key] += 1
    return bigram_counts


def main():
    assert get_char_bigrams("apple") == {'ap': 1, 'pp': 1, 'pl': 1, 'le': 1}
    assert get_char_bigrams("apple apple") == {'ap': 2, 'pp': 2, 'pl': 2, 'le': 2, 'e ': 1, ' a': 1}

    print("Tests passed.")


if __name__ == '__main__':
    main()
