#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab01_get_nth_fibonacci import get_nth_fibonacci


def get_range_fibonacci(A, B):
    numbers = []
    for i in range(A, B):
        numbers.append(get_nth_fibonacci(i))
    return numbers


def main():
    assert (get_range_fibonacci(2, 5) == [1, 2, 3])
    assert (get_range_fibonacci(5, 5) == [])
    assert (get_range_fibonacci(1, 5) == [1, 1, 2, 3])

    print("Tests passed.")


if __name__ == '__main__':
    main()
