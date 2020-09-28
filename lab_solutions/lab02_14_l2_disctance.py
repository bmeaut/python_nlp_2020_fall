#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def l2_distance(vector1, vector2):
    dim1 = len(vector1)
    dim2 = len(vector2)
    dim_diff = abs(dim1 - dim2)
    if dim_diff != 0:
        raise ValueError('Vectors dimensions must be equal')
    square_sum = 0
    for i in range(len(vector1)):
        square_sum += (vector1[i] - vector2[i]) ** 2
    return square_sum ** 0.5


def main():
    assert abs(l2_distance([1, 0], [1, 0]) - 0) < 1e-5
    assert abs(l2_distance([1, 0], [0, 1]) - 2 ** 0.5) < 1e-5

    print("Tests passed.")


if __name__ == '__main__':
    main()
