#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Bence Bial <gbenceg@gmail.com>
#
# Distributed under terms of the MIT license.


def get_char_bigrams(s):
    counts = {}
    for i in range(len(s)-1):
        bigram = s[i:i+2]
        counts[bigram] = counts.get(bigram, 0) + 1
    return counts


def main():
    assert get_char_bigrams("apple") == {'ap': 1, 'pp': 1, 'pl': 1, 'le': 1}
    assert get_char_bigrams("apple apple") == {'ap': 2, 'pp': 2, 'pl': 2, 'le': 2, 'e ': 1, ' a': 1}
    print("Tests passed.")
    
    print("Trying for user input.")
    s = input("String s = ")
    print(get_char_bigrams(s))


if __name__ == '__main__':
    main()
