#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_03_is_matrix import is_matrix


def rowwise_max(M):
    if not is_matrix(M):
        raise ValueError('Oh no :(')
    return [max(row) for row in M]


def main():
    assert rowwise_max(
        [
            [1, 2, 3],
            [1, 4, 3],
            [1, 5, 3],
        ]
    ) == [3, 4, 5]

    print("Tests passed.")


if __name__ == '__main__':
    main()
