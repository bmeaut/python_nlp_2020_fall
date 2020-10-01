#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys@2000@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab01_qsort import swap


def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                swap(l, j, j+1)


def main():
    l = [10, -1, 2, 11, 0]

    bubblesort(l)

    assert (l == [-1, 0, 2, 10, 11])

    print("Tests passed.")


if __name__ == '__main__':
    main()
