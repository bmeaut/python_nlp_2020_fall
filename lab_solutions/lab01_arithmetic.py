#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.


def arithmetic(a, b, arg='+'):
    if arg == '+':
        return a+b
    elif arg == '-':
        return a-b
    elif arg == '*':
        return a*b
    elif arg == '/':
        return a/b


def main():
    assert (arithmetic(2, 3) == 5)
    assert (arithmetic(2, 3, "-") == -1)
    assert (arithmetic(2, 3, "*") == 6)
    assert (arithmetic(2, 3, "/") == 2 / 3)

    print("Tests passed.")


if __name__ == '__main__':
    main()
