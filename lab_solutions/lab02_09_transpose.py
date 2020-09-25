#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_03_is_matrix import is_matrix


def transpose(M):
    if not is_matrix(M):
        raise ValueError('Oh no :(')
    else:
        return [list(i) for i in zip(*M)]


def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[1, 4], [2, 5], [3, 6]]

    assert (transpose(m1) == m2)
    assert (transpose(transpose(m1)) == m1)

    print("Tests passed.")


if __name__ == '__main__':
    main()
