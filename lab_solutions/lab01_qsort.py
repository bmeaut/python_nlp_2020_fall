#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.


def swap(l, idx1, idx2):
    temp = l[idx1]
    l[idx1] = l[idx2]
    l[idx2] = temp


def qsort(l):
    # unpack

    if type(l) is list:
        start = 0
        end = len(l)
    else:
        start = l[1][0]
        end = l[1][1]
        l = l[0]
    if end - start <= 1:
        return

    # sort partitions in place

    pivot_idx = start
    pivot = l[pivot_idx]
    for i in range(start + 1, end):
        current_idx = i
        if l[current_idx] < l[pivot_idx]:
            while current_idx > pivot_idx:
                swap(l, current_idx - 1, current_idx)
                current_idx -= 1
            pivot_idx += 1

    # call next partitions

    qsort((l, (0, pivot_idx)))
    if pivot_idx < len(l) - 1:
        qsort((l, (pivot_idx + 1, end)))


def main():
    l = [10, -1, 2, 11, 0]

    qsort(l)

    assert (l == [-1, 0, 2, 10, 11])

    print("Tests passed.")


if __name__ == '__main__':
    main()
