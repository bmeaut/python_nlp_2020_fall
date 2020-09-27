#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def is_symmetric(l):
    length = len(l)
    first = 0
    last = length - 1
    for i in range(length//2):
        if l[first] == l[last]:
            first = first + 1
            last = last - 1
        else:
            return False

    return True


def main():
    assert is_symmetric([1]) == True
    assert is_symmetric([]) == True
    assert is_symmetric([1, 2, 3, 1]) == False
    assert is_symmetric([1, "foo", "bar", "foo", 1]) == True
    assert is_symmetric("abcba") == True

    print("Tests passed.")


if __name__ == '__main__':
    main()
