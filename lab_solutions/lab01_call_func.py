#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab01_arithmetic import arithmetic


def call_func(a, b, func=arithmetic):
    return func(a, b)


def product(x, y):
    return x * y


def main():
    assert (call_func(3, 4, product) == 12)
    assert (call_func("foo", "bar") == "foobar")

    print("Tests passed.")


if __name__ == '__main__':
    main()
