#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Bence Bial <gbenceg@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_04_char_freq import char_freq


def are_anagrams(word1, word2):
    return char_freq(word1) == char_freq(word2)


def main():
    assert are_anagrams("abc", "bac") == True
    assert are_anagrams("aabb", "abab") == True
    assert are_anagrams("abab", "aaab") == False
    print("Tests passed.")


if __name__ == '__main__':
    main()
