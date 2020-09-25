#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab2._02_03_is_matrix import is_matrix
from lab_solutions.lab2._02_14_l2_disctance import l2_distance
from lab_solutions.lab2._02_09_transpose import transpose


def pairwise_row_distance(A):
    if not is_matrix(A):
        raise ValueError('Oh no :(')

    dist_mx = [[0 for j in range(len(A))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            dist_mx[i][j] = l2_distance(A[i], A[j])

    return dist_mx


def main():
    D = pairwise_row_distance([[1, 0, 2], [0, 2, 1]])
    # should be a symmetric matrix
    assert is_matrix(D) == True
    assert len(D) == 2
    assert len(D[0]) == 2

    # should be symmetric
    assert transpose(D) == D

    print("Tests passed.")


if __name__ == '__main__':
    main()
