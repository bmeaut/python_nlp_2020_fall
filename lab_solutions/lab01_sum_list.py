#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys@2000@gmail.com>
#
# Distributed under terms of the MIT license.


def sum_list(list_to_sum, start=0):
    total = start
    for i in list_to_sum:
        total += i
    return total


def main():
    assert (sum_list([1, 2, 3]) == 6)
    assert (sum_list([1, 2, 3], 5) == 11)

    print("Tests passed.")


if __name__ == '__main__':
    main()
