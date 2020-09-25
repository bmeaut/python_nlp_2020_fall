#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def is_symmetric(l):
    return list(reversed(l)) == list(l)


def is_symmetric_opt(l):
    length = len(l)
    first = 0
    last = length - 1
    is_sym = True
    while first < last:
        if l[first] == l[last]:
            first = first + 1
            last = last - 1
        else:
            is_sym = False
            break

    return is_sym


def main():
    assert is_symmetric([1]) == True
    assert is_symmetric([]) == True
    assert is_symmetric([1, 2, 3, 1]) == False
    assert is_symmetric([1, "foo", "bar", "foo", 1]) == True
    assert is_symmetric("abcba") == True

    assert is_symmetric_opt([1]) == True
    assert is_symmetric_opt([]) == True
    assert is_symmetric_opt([1, 2, 3, 1]) == False
    assert is_symmetric_opt([1, "foo", "bar", "foo", 1]) == True
    assert is_symmetric_opt("abcba") == True

    print("Tests passed.")


if __name__ == '__main__':
    main()
