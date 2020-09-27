#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def count_elements(sequence):
    counts = {}
    for i in sequence:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

    return counts


def main():
    # test for list
    assert count_elements([1, 2, 0, 1, 1]) == {1: 3, 2: 1, 0: 1}
    # test for tuple
    assert count_elements((1, 2, 0, 1, 1)) == {1: 3, 2: 1, 0: 1}
    # test empty list
    assert count_elements([]) == {}

    print("Tests passed.")


if __name__ == '__main__':
    main()
