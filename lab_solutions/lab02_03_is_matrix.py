#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Attila Nagy <attila.nagy234@gmail.com>
#
# Distributed under terms of the MIT license.


def is_matrix(M):
    if len(M) == 0:
        return True
    else:
        return len(M[0]) == len(M[1])


def main():
    assert is_matrix([]) == True
    assert is_matrix([[], []]) == True
    assert is_matrix([[1, 2], [2, 1]]) == True
    assert is_matrix([[1], [2, 1]]) == False
    assert is_matrix([[1, 2], [2, 1], [3, 4]]) == True

    print("Tests passed.")


if __name__ == '__main__':
    main()
