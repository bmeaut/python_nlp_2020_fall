#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys2000@gmail.com>
#
# Distributed under terms of the MIT license.


def filter_list(input_list, predicate):
    output_list = []
    for i in input_list:
        if predicate(i):
            output_list.append(i)
    return output_list


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    return True


def is_odd(n):
    return n % 2 == 1


def main():
    l1 = [1, 2, 3, 4, 19, 35, 11]

    assert (filter_list(l1, is_odd) == [1, 3, 19, 35, 11])
    assert (filter_list(l1, is_prime) == [2, 3, 19, 11])

    print("Tests passed.")


if __name__ == '__main__':
    main()
