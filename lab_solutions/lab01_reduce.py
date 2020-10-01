#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.


def reduce(l, acc_func, accumulator=None):
    if accumulator is not None:
        l.insert(0, accumulator)
    accumulated = acc_func(l[0], l[1])
    ll = l[2:]
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

    l2 = ["foo", "bar", "hello"]

    assert (reduce(l2, string_len_add, 0) == 11)

    print("Tests passed.")


if __name__ == '__main__':
    main()
