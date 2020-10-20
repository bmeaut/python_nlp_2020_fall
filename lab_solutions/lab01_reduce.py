#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.


def reduce(list_to_reduce, acc_func, accumulator=None):
    if accumulator is not None:
        accumulated = acc_func(accumulator, list_to_reduce[0])
        ll = list_to_reduce[1:]
    else:
        accumulated = acc_func(list_to_reduce[0], list_to_reduce[1])
        ll = list_to_reduce[2:]
    for item in ll:
        accumulated = acc_func(accumulated, item)
    return accumulated


def add(x, y):
    return x + y


def string_len_add(acc, s):
    return acc + len(s)


def main():
    l1 = [1, 2, -1, 5]

    reduce(l1, add)

    assert (reduce(l1, add) == 7)
    assert (reduce(l1, add, 10) == 17)
    assert (reduce(l1, max) == 5)
    assert (reduce(l1, max, 12) == 12)

    l2 = ["foo", "bar", "hello"]

    assert (reduce(l2, string_len_add, 0) == 11)
    assert (reduce(l2, string_len_add, 0) == 11)

    # Testing that the original lists are unchanged
    assert (l1 == [1, 2, -1, 5])
    assert (l2 == ["foo", "bar", "hello"])

    print("Tests passed.")


if __name__ == '__main__':
    main()
