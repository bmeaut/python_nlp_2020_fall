#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys@2000@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab01_get_nth_fibonacci import get_nth_fibonacci


def get_n_fibonacci(N):
    return [get_nth_fibonacci(i+1) for i in range(N)]


def main():
    assert (get_n_fibonacci(4) == [1, 1, 2, 3])
    assert (get_n_fibonacci(0) == [])

    print("Tests passed.")


if __name__ == '__main__':
    main()
