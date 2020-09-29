#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Bence Bial <gbenceg@gmail.com>
#
# Distributed under terms of the MIT license.

from lab_solutions.lab02_03_is_matrix import is_matrix
from lab_solutions.lab02_09_transpose import transpose
from lab_solutions.lab02_14_l2_disctance import l2_distance


def pairwise_row_distance(A):
    if not is_matrix(A):
        raise ValueError("Not a valid matrix")
        
    l2s = [[0 for _ in range(len(A))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            l2s[i][j] = l2s[j][i] = l2_distance(A[i], A[j])
        
    return l2s


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
