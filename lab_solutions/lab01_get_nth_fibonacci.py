#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys@2000@gmail.com>
#
# Distributed under terms of the MIT license.


def get_nth_fibonacci(N):
    if N < 0:
        raise ValueError('Negative value not allowed!')
    if N == 0:
        return 0
    if N == 1:
        return 1
    return get_nth_fibonacci(N-1) + get_nth_fibonacci(N-2)


def main():
    assert (get_nth_fibonacci(0) == 0)
    assert (get_nth_fibonacci(1) == 1)
    assert (get_nth_fibonacci(2) == 1)
    assert (get_nth_fibonacci(5) == 5)
    assert (get_nth_fibonacci(7) == 13)

    try:
        get_nth_fibonacci(-2)
    except ValueError:
        pass
    else:
        print("TEST FAILS. Negative index should raise a ValueError.")

    print("Tests passed.")


if __name__ == '__main__':
    main()
