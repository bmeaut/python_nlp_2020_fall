#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_09_transpose import transpose
from lab_solutions.lab02_10_rowwise_max import rowwise_max


def columnwise_max(M):
    transposed_mx = transpose(M)
    return rowwise_max(transposed_mx)


def main():
    assert columnwise_max(
        [
            [1, 2, 3],
            [1, 4, 3],
            [1, 5, 3],
        ]
    ) == [1, 5, 3]

    print("Tests passed.")


if __name__ == '__main__':
    main()
